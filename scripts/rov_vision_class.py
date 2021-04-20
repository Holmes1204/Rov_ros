#!/usr/bin/python
# -*- coding:utf-8 -*-
# Environment: Ubuntu 18.04, Python 3.6.9, OpenCV 3.2.0, Numpy 1.19.2
# Author:Liu, Yuming
# Date:2021.04.19


import cv2
import numpy as np
import os
import threading
import time

import rospy
from topic_example.msg import  Img_fb 

def ROS_img():
    def __init__(self):
        rospy.init_node("img_fb_node")
        self.img_pub = rospy.Publisher('img_feedback',Img_fb,queue_size=1)
        self.img_fb = Img_fb()
    
    def send_msg(self,angle,dist):
        self.img_fb.angle_fb=round(angle, 7)
        self.img_fb.dist_fb=round(dist, 7)
        self.img_pub.publish(self.img_fb)

class RovVision:
    def __init__(self):
        self.thresh_val = 150
        self.pre_angle = 0
        self.line_var_min = 300
        self.line_var_max = 700
        self.line_var = 0
        self.start_move = True
        self.ros_node = ROS_img()
        # self.forward, self.bottom = self.selectCamera()    # for real camera
        cap_forward = cv2.VideoCapture("scripts/ROV_test1.mp4")    # test only
        cap_bottom = []                                    # test only
        thread_follow_line = threading.Thread(target=self.followLine)
        thread_auto_adapt = threading.Thread(target=self.autoAdapt)
        thread_detect_block = threading.Thread(target=self.detectBlock)
        thread_start_move = threading.Thread(target=self.startMove)

        thread_auto_adapt.start()
        thread_start_move.start()
        while not self.start_move:
            try:
                ret, img_forward = cap_forward.read()
                img_forward = cv2.flip(img_forward, 0)
                self.img_forward_src = cv2.flip(img_forward, 1)
                time.sleep(0.05)
            except:
                pass
        
        thread_detect_block.start()
        thread_follow_line.start()
        while True:
            try:
                ret, img_forward = cap_forward.read()
                img_forward = cv2.flip(img_forward, 0)
                self.img_forward_src = cv2.flip(img_forward, 1)
                time.sleep(0.05)
            except:
                pass

    def selectCamera(self):
        """
            In linux only
            cap_forward for autoAdapt and followLine, cap_bottom for detectBlock
            :return: cap_forward, cap_bottom
            """
        vid = os.listdir('/dev/')
        vid_num = []
        # find all the camera index
        for i in range(len(vid)):
            if 'video' in vid[i]:
                vid_num.append(int(vid[i][-1]))
        del vid
        # remove unavailable element
        for vid in vid_num:
            try:
                cap = cv2.VideoCapture(vid)
            except:
                vid_num.remove(vid)
        del cap
        # get two video streams
        cap_forward = cv2.VideoCapture(vid_num[0])
        cap_bottom = cv2.VideoCapture(vid_num[1])
        # if high resolution is bottom >
        # if high resolution is forward <
        if cap_forward.get(3) > cap_bottom.get(3):
            cap_tmp = cap_forward
            cap_forward = cap_bottom
            cap_bottom = cap_tmp
            del cap_tmp
        # set to low resolution
        cap_forward.set(3, 640)
        cap_forward.set(4, 480)
        cap_bottom.set(3, 640)
        cap_bottom.set(4, 480)
        return cap_forward, cap_bottom

    def detectBlock(self):
        pass

    def autoAdapt(self):
        while True:
            try:
                if abs(self.pre_angle) <= 0.35:  # 0.35rad == 20degree
                    img_src = self.img_forward_src
                    thresh_val_line, dis_mean_line, dis_var_line = self.fitLine(img_src)
                    self.thresh_val = thresh_val_line
                    self.line_var = dis_var_line
                    print("thresh_val=%d, dis_mean=%.5f, dis_var=%.5f" %
                          (thresh_val_line, dis_mean_line, dis_var_line))
            except:
                pass

    def fitLine(self, img_src):
        """
        to fit the track as line
        :param img_src: input img
        :return: none
        """
        cnt = 0
        dis_var_mean = 0
        dis_mean_mean = 0
        thresh_val_mean = 0
        for thresh_val_tmp in range(0, 255, 5):
            img_0 = cv2.resize(img_src, (int(img_src.shape[1] * 0.5), int(img_src.shape[0] * 0.5)))
            img_2 = img_0[:, :, 2]
            img_2 = cv2.GaussianBlur(img_2, (15, 15), 15)
            img_2 = cv2.blur(img_2, (15, 15))
            img_2 = cv2.medianBlur(img_2, 15)
            ret, img_2 = cv2.threshold(img_2, thresh_val_tmp, 255, cv2.THRESH_BINARY)
            track_img = np.where(img_2 == 255)
            track_x = (track_img[1]).T
            track_y = (track_img[0]).T
            if len(track_x) == 0 or len(track_y) == 0:
                continue
            # fit linear function according to the white region
            pre_fit = np.polyfit(img_0.shape[0] - track_y + 1, track_x + 1, 1)  # #col = f(#row)
            dis_mean = np.sum(((track_x + 1) - pre_fit[0] * (img_0.shape[0] - track_y + 1) - pre_fit[1]) \
                              / np.sqrt(pre_fit[0] ** 2 + 1)) * (1 / track_x.size)
            dis_var = ((track_x + 1) - pre_fit[0] * (img_0.shape[0] - track_y + 1) - pre_fit[1]) \
                      / np.sqrt(pre_fit[0] ** 2 + 1) - dis_mean
            dis_var = np.dot(dis_var, dis_var.T) * (1 / track_x.size)
            if self.line_var_min <= dis_var <= self.line_var_max:
                cnt += 1
                dis_var_mean += dis_var
                dis_mean_mean += dis_mean
                thresh_val_mean += thresh_val_tmp
        dis_var_mean /= cnt
        dis_mean_mean /= cnt
        thresh_val_mean /= cnt
        return thresh_val_mean, dis_mean_mean, dis_var_mean

    def followLine(self):
        """
        follow line
        input: global img img_forward_src
        output: global thresh_val and pre_angle
        :param: none
        :return: none
        """
        run_main = True
        rate = rospy.Rate(5)
        while True:  # and not rospy.is_shutdown()):
            try:
                img_src = self.img_forward_src
                img_src = cv2.resize(img_src, (int(img_src.shape[1] * 0.5), int(img_src.shape[0] * 0.5)))
                img_2 = img_src[:, :, 2]
                img_2 = cv2.GaussianBlur(img_2, (15, 15), 15)
                img_2 = cv2.blur(img_2, (15, 15))
                img_2 = cv2.medianBlur(img_2, 15)
                ret, img_2 = cv2.threshold(img_2, self.thresh_val, 255, cv2.THRESH_BINARY)
                track_img = np.where(img_2 == 255)
                track_x = (track_img[1]).T
                track_y = (track_img[0]).T

                img = cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR)
                # fit linear function according to the white region
                pre_fit = np.polyfit(img_src.shape[0] - track_y + 1, track_x + 1, 1)  # #col = f(#row)
                pre_val = np.polyval(pre_fit, [0, img_src.shape[0] - 1]).astype(np.int)  # #col = f(#row)
                output_img = cv2.line(img, (int((pre_val[0] + pre_val[1]) / 2), img.shape[0]),
                                      (int((pre_val[1] + pre_val[0]) / 2), 0), (0, 255, 0), 5)
                output_img = cv2.line(output_img, (pre_val[0], img_src.shape[0]),
                                      (pre_val[1], 0), (0, 0, 255), 5)  # point(#col(topmin butmax), # row)

                dis_mean = np.sum(((track_x + 1) - pre_fit[0] * (img.shape[0] - track_y + 1) - pre_fit[1]) \
                                  / np.sqrt(pre_fit[0] ** 2 + 1)) * (1 / track_x.size)
                dis_var = ((track_x + 1) - pre_fit[0] * (img.shape[0] - track_y + 1) - pre_fit[1]) \
                          / np.sqrt(pre_fit[0] ** 2 + 1) - dis_mean
                dis_var = np.dot(dis_var, dis_var.T) * (1 / track_x.size)

                # calculate degree error
                self.pre_angle = (pre_val[0] - pre_val[1]) / np.sqrt((pre_val[0] - pre_val[1]) ** 2 + img_src.shape[0] ** 2)
                self.pre_angle = np.arcsin(self.pre_angle)
                output_img = cv2.putText(output_img, 'angle error:' + str(round(self.pre_angle, 7)),
                                         (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.1)),
                                         cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)

                # calculate position error
                bot_part = np.where(track_y > img_src.shape[0] - (img_src.shape[0] / 4))
                now_error = np.mean(track_x[bot_part])
                now_error = now_error - img_src.shape[1] / 2
                output_img = cv2.putText(output_img, 'horizontal error:' + str(round(now_error, 7)),
                                         (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.2)),
                                         cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
                output_img = cv2.putText(output_img, 'fixed distance var:' + str(round(self.line_var, 7)),
                                         (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.3)),
                                         cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
                output_img = cv2.putText(output_img, 'dynamic distance var:' + str(round(dis_var, 7)),
                                         (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.4)),
                                         cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
                self.img_fb.angle_fb=round(self.pre_angle, 7)
                self.img_fb.dist_fb=round(self.line_var, 7)
                self.img_pub.publish(self.img_fb)
                cv2.imshow('output', output_img)
                cv2.imshow('img', img_src)
                rate.sleep()
                if(cv2.waitKey(1)&0xFF==ord('q')):
                    cv2.destroyAllWindows()
                    run_main=False
                    break
            except:
                pass
    

    """ 
    TODO: to be checked in whatever situation can start the move

    """

    def startMove(self):
        while not self.start_move:
            try:
                img_src = self.img_forward_src
                img_src = cv2.resize(img_src, (int(img_src.shape[1] * 0.5), int(img_src.shape[0] * 0.5)))

                # use blue to detect the start zone, use red to detect line
                img_2 = img_src[:, :, 2]
                img_2 = cv2.GaussianBlur(img_2, (15, 15), 15)
                img_2 = cv2.blur(img_2, (15, 15))
                img_2 = cv2.medianBlur(img_2, 15)
                img_0 = img_src[:, :, 0]
                img_0 = cv2.GaussianBlur(img_0, (15, 15), 15)
                img_0 = cv2.blur(img_0, (15, 15))
                img_0 = cv2.medianBlur(img_0, 15)
                ret, img_2 = cv2.threshold(img_2, self.thresh_val, 255, cv2.THRESH_BINARY)
                ret, img_0 = cv2.threshold(img_0, 100, 255, cv2.THRESH_BINARY)
                track_img = np.where(img_2 == 255)
                track_x = (track_img[1]).T
                track_y = (track_img[0]).T
                start_img = np.where(img_0 == 0)
                start_x = (start_img[1]).T
                start_y = (start_img[0]).T

                cv2.imshow('2', img_2)
                cv2.imshow('1', img_0)
                if(cv2.waitKey(1)&0xFF==ord('q')):
                    cv2.destroyAllWindows()
                    run_main=False
                    break

                if len(start_x) == 0 or len(start_y) == 0:
                    continue
                img = cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR)
                # fit linear function according to the white region
                pre_fit = np.polyfit(img_src.shape[0] - track_y + 1, track_x + 1, 1)  # #col = f(#row)

                dis_mean = np.sum(((track_x + 1) - pre_fit[0] * (img.shape[0] - track_y + 1) - pre_fit[1]) \
                                  / np.sqrt(pre_fit[0] ** 2 + 1)) * (1 / track_x.size)
                dis_var = ((track_x + 1) - pre_fit[0] * (img.shape[0] - track_y + 1) - pre_fit[1]) \
                          / np.sqrt(pre_fit[0] ** 2 + 1) - dis_mean
                dis_var = np.dot(dis_var, dis_var.T) * (1 / track_x.size)
                dis_s = np.sqrt(dis_var)    # standard error

                start_width = max(start_x) - min(start_x)
                start_height = max(start_y) - min(start_y)
                start_mid_x = np.mean(start_x) + 1
                start_mid_y = np.mean(img_src.shape[0] - start_y + 1)
                start_range = np.polyval(pre_fit, start_mid_y)

                # if the height of the black is bigger than 0.1 * the width of the black
                # and the black area is bigger than 0.5 of the boundary
                # and the center of the black is within the line
                if start_height >= 0.1 * start_width \
                        and len(start_y) >= 0.5 * start_width * start_height \
                        and start_range - dis_s <= start_mid_x <= start_range + dis_s:
                    self.start_move = 1
            except:
                pass


if __name__ == '__main__' :
    RovVision()

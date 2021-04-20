#!/usr/bin/python 
import cv2
import numpy as np
import os
from rosgraph.roslogging import renew_latest_logdir
import time
import threading
line_var_min = 300
line_var_max = 700


def followLine():
    """
    follow line
    input: global imtime_f = time.time()
            #g img_forward_src
    output: global thresh_val and pre_angle
    :param: none
    :return: none
    """
    global thresh_val
    global img_forward_src
    global pre_angle
    global run_main
    run_main = True
    #img_pub = rospy.Publisher('img_feedback',Img_fb,queue_size=1)
    #img_fb = Img_fb()
    time_l=0
    #rate = rospy.Rate(5)
    while run_main:  # and not rospy.is_shutdown()):
        try:
            img_src = img_forward_src
            img_src = cv2.resize(img_src, (int(img_src.shape[1] * 0.5), int(img_src.shape[0] * 0.5)))
            ret, img_1 = cv2.threshold(img_src[:, :, 1], thresh_val, 255, cv2.THRESH_BINARY)
            ret, img_2 = cv2.threshold(img_src[:, :, 2], thresh_val, 255, cv2.THRESH_BINARY)
            img = cv2.bitwise_and(img_1, img_2)
            track_img = np.where(img == 255)
            track_x = (track_img[1]).T
            track_y = (track_img[0]).T

            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            # fit linear function according to the white region
            pre_fit = np.polyfit(img_src.shape[0] - track_y + 1, track_x + 1, 1)  # #col = f(#row)
            pre_val = np.polyval(pre_fit, [0, img_src.shape[0] - 1]).astype(np.int)  # #col = f(#row)
            output_img = cv2.line(img, (int((pre_val[0] + pre_val[1]) / 2), img.shape[0]),
                                  (int((pre_val[1] + pre_val[0]) / 2), 0), (0, 255, 0), 5)
            output_img = cv2.line(output_img, (pre_val[0], img_src.shape[0]),
                                  (pre_val[1], 0), (0, 0, 255), 5)  # point(#col(topmin butmax), # row)
            # calculate degree error
            pre_angle = (pre_val[0] - pre_val[1]) / np.sqrt((pre_val[0] - pre_val[1]) ** 2 + img_src.shape[0] ** 2)
            pre_angle = np.arcsin(pre_angle)
            output_img = cv2.putText(output_img, 'angle error:' + str(round(pre_angle, 7)),
                                     (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.1)),
                                     cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
            # calculate position error
            bot_part = np.where(track_y > img_src.shape[0] - (img_src.shape[0] / 4))
            now_error = np.mean(track_x[bot_part])
            now_error = now_error - img_src.shape[1] / 2
            output_img = cv2.putText(output_img, 'horizontal error:' + str(round(now_error, 7)),
                                     (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.2)),
                                     cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
            time_f = time.time()
            fps=1.0/(time_f-time_l)
            time_l = time_f
            output_img = cv2.putText(output_img, 'fps:' + str(round(fps, 7)),
                                     (int(img_src.shape[1] * 0.03), int(img_src.shape[0] * 0.3)),
                                     cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
            #img_fb.angle_fb=round(pre_angle, 7)
            #img_fb.dist_fb=round(now_error, 7)
            #img_pub.publish(img_fb)
            cv2.imshow('output', output_img)
            #cv2.imshow('img', img_src)
            if(cv2.waitKey(1)&0xFF==ord('q')):
                cv2.destroyAllWindows()
                run_main=False
                break
            #rate.sleep()
        except:
            cv2.destroyAllWindows()
            run_main=False
            break

def fitLine(img_src):
    """
    to fit the track as line
    :param img_src: input img
    :return: none
    """
    thresh_min = 255
    thresh_max = 0
    cnt = 0
    dis_var_mean = 0
    dis_mean_mean = 0
    for thresh_val_tmp in range(0, 255, 5):
        img_0 = cv2.resize(img_src, (int(img_src.shape[1] * 0.5), int(img_src.shape[0] * 0.5)))
        ret, img_1 = cv2.threshold(img_0[:, :, 1], thresh_val_tmp, 255, cv2.THRESH_BINARY)
        ret, img_2 = cv2.threshold(img_0[:, :, 2], thresh_val_tmp, 255, cv2.THRESH_BINARY)
        img = cv2.bitwise_and(img_1, img_2)
        track_img = np.where(img == 255)
        track_x = (track_img[1]).T
        track_y = (track_img[0]).T

        # fit linear function according to the white region
        pre_fit = np.polyfit(img_0.shape[0] - track_y + 1, track_x + 1, 1)  # #col = f(#row)
        dis_mean = np.sum(((track_x + 1) - pre_fit[0] * (img_0.shape[0] - track_y + 1) - pre_fit[1]) \
                          / np.sqrt(pre_fit[0] ** 2 + 1)) * (1 / track_x.size)
        dis_var = ((track_x + 1) - pre_fit[0] * (img_0.shape[0] - track_y + 1) - pre_fit[1]) \
                  / np.sqrt(pre_fit[0] ** 2 + 1) - dis_mean
        dis_var = np.dot(dis_var, dis_var.T) * (1 / track_x.size)
        if dis_var < line_var_min:
            break
        if line_var_min <= dis_var <= line_var_max:
            cnt += 1
            dis_var_mean += dis_var
            dis_mean_mean += dis_mean
            if thresh_val_tmp >= thresh_max:
                thresh_max = thresh_val_tmp
            if thresh_val_tmp <= thresh_min:
                thresh_min = thresh_val_tmp
    thresh_val = int((thresh_max + thresh_min) / 2)
    dis_var_mean /= cnt
    dis_mean_mean /= cnt
    return thresh_val, dis_mean_mean, dis_var_mean, thresh_max, thresh_min


def autoAdapt():
    """
    automatically set the threshold of binaryzation
    :input: global img_forward_src, pre_angle
    :output: global thresh_val
    :return: none
    """
    global img_forward_src
    global thresh_val
    global pre_angle
    pre_angle = 0
    while True:
        try:
            if abs(pre_angle) <= 0.35:   # 0.35rad == 20degree
                img_src = img_forward_src
                thresh_val_line, dis_mean_line, dis_var_line, thresh_max_line, thresh_min_line = fitLine(img_src)
                thresh_val = thresh_val_line
                print("thresh_val=%d, dis_mean=%.5f, dis_var=%.5f, thresh_max=%d, thresh_min=%d" %
                      (thresh_val_line, dis_mean_line, dis_var_line, thresh_max_line, thresh_min_line))
        except:
            break


def detectBlock():
    pass


def selectCamera():
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


if __name__ == "__main__":
    try:
        #rospy.init_node("img_fb_node")
        #rate = rospy.Rate(1)# only in test
        # cap_forward, cap_bottom = selectCamera()   # in ubuntu only
        ros_img_handle = ROS_img()
        cap_forward = cv2.VideoCapture('/home/holmes/ros_ws/EngCom/src/ros_serial/scripts/ROV_test1.mp4')             # test only
        cap_bottom = []                                             # test only
        global thresh_val
        thresh_val = 150
        global img_forward_src, img_bottom_src
        global run_main 
        run_main = True
        ret, img_forward = cap_forward.read()
        img_forward = cv2.flip(img_forward, 0)
        img_forward_src = cv2.flip(img_forward, 1)
        #ret, img_bottom_src = cap_bottom.read()
        thread_follow_line = threading.Thread(target=followLine)
        thread_auto_adapt = threading.Thread(target=autoAdapt)
        thread_detect_block = threading.Thread(target=detectBlock)
        thread_follow_line.start()
        thread_auto_adapt.start()
        thread_detect_block.start()
        '''
        _thread.start_new_thread(followLine, (cap_forward,))
        _thread.start_new_thread(autoAdapt, (cap_forward,))
        _thread.start_new_thread(detectBlock, (cap_bottom,))
        '''
        while   run_main and cap_forward.isOpened() :#and not rospy.is_shutdown():
            ret, img_forward = cap_forward.read()
            img_forward = cv2.flip(img_forward, 0)
            img_forward_src = cv2.flip(img_forward, 1)
            #rate.sleep()#only in test
    except :
        cv2.destroyAllWindows()
        quit()
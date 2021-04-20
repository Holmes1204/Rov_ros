
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

/**************************
用遥控器通过上位机串口通讯控制stm32来控制6个推进器运动
//安装推进器注意：1   头    2
//             5         6
//             3         4
*************************/
//遥控器操作方式：左摇杆负责平面运动，右摇杆竖直方向为沉浮，水平方向为原地转动
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <topic_example/mbot_linux_serial.h>
#include <sensor_msgs/Joy.h>
#include <string.h>
#include <topic_example/Img_fb.h>


void img_fb_callback(const topic_example::Img_fb::ConstPtr& img_fb_msg){
    float angle_error = img_fb_msg->angle_fb;
    float dist_error = img_fb_msg->dist_fb;
    static mtr_msg mtrs;
    mtrs.mtr_state[0] = 0;
    mtrs.mtr_state[1] =  angle_error*2400/3.1415926;
    mtrs.mtr_state[2]   =  (int) dist_error;
    mtrs.mtr_state[3]   = 0;
    mtrs.mtr_state[4]   = 0;
    mtrs.mtr_state[5]   = 0;
    mtrs.mtr_state[6]   = 0;
    mtrs.mtr_state[7]   = 0;
    mtrs.mtr_state[8]   = 0;
    mtrs.mtr_state[9]   = 0;
    mtrs.mtr_state[10]   = 0;
    if(TX_serial_msg(mtrs))
        ROS_INFO("%d %d %d %d",mtrs.mtr_state[0],mtrs.mtr_state[1],mtrs.mtr_state[2],mtrs.mtr_state[3]);    
    else
        ROS_INFO("failed!");
    return;
    return;
}

int main(int agrc,char **argv)
{
    ros::init(agrc,argv,"serial_stm32");
    ros::NodeHandle nh;
    //ros::Subscriber joy_sub = nh.subscribe("/joy", 1000, &joy_callback);//订阅手柄
    ros::Subscriber img_fb_sub = nh.subscribe("/img_feedback", 100, &img_fb_callback);
    ros::Rate loop_rate(100);
    //串口初始化
    serialInit();
    while(ros::ok())
    {
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
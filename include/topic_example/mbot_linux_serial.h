#ifndef MBOT_LINUX_SERIAL_H
#define MBOT_LINUX_SERIAL_H

#include <ros/ros.h>
#include <ros/time.h>
#include <boost/asio.hpp>
#include <geometry_msgs/Twist.h>

typedef union 
{
    uint16_t u16;
    uint8_t u8[2];
}uint16to8;

struct mtr_msg
{
    /* data */
    uint8_t mtr_state[10];
};

void serialInit();
bool TX_serial_msg(const mtr_msg& mtr);
//extern bool readSpeed(double &Left_v,double &Right_v,double &Angle,unsigned char &ctrlFlag);
unsigned char getCrc8(unsigned char *ptr, unsigned short len);



#endif//MBOT_LINUX_SERIAL_H

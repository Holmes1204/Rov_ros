//针对my_rov的串口通信协议

#include <topic_example/mbot_linux_serial.h>

using namespace std;
using namespace boost::asio;
//串口相关对象

boost::asio::io_service iosev;
boost::asio::serial_port sp(iosev, "/dev/ttyUSB0");
//boost::asio::serial_port sp(iosev, "/dev/ttyTHS1");
boost::system::error_code err;

/********************************************************
            串口发送接收相关常量、变量、共用体对象
********************************************************/
const unsigned char ender[2] = {0xBF, 0xBB};//定义消息头
const unsigned char header[2] = {0xAF, 0xAA};



/********************************************************
函数功能：串口参数初始化
入口参数：无
出口参数：
********************************************************/

void serialInit()//串口初始化
{
    /*波特率*/
    sp.set_option(serial_port::baud_rate(115200));
    /*数据位*/
    sp.set_option(serial_port::character_size(8));    
    /*奇偶校验位*/
    sp.set_option(serial_port::parity(serial_port::parity::none));
    /*停止位*/
    sp.set_option(serial_port::stop_bits(serial_port::stop_bits::one));
    /*串口流控制*/
    sp.set_option(serial_port::flow_control(serial_port::flow_control::none));
}


bool TX_serial_msg(const mtr_msg& mtr)
{
    const int length = 10;
    uint8_t buf[3+length+3] = {0};//定义发送数据变量
    // 设置消息头
    buf[0] = header[0];
    buf[1] = header[1];             //buf[0]  buf[1]
    buf[2] = length;                    //buf[2] size为6
    for (int i = 0; i < length; i++)
    {
        buf[3+i]=mtr.mtr_state[i];
    }
    // 设置校验值、消息尾
    buf[3 + length] = getCrc8(buf, 3 + length);
    buf[3 + length + 1] = ender[0];            
    buf[3 + length + 2] = ender[1];        
    if(boost::asio::write(sp, boost::asio::buffer(buf))!=0)
    {
        return true;
    }
    else
    {
        return false;
    }

}
/********************************************************
函数功能：获得8位循环冗余校验值
入口参数：数组地址、长度
出口参数：校验值
********************************************************/
unsigned char getCrc8(unsigned char *ptr, unsigned short len)
{
    unsigned char crc;
    unsigned char i;
    crc = 0;
    while(len--)
    {
        crc ^= *ptr++;
        for(i = 0; i < 8; i++)
        {
            if(crc&0x01)
                crc=(crc>>1)^0x8C;
            else 
                crc >>= 1;
        }
    }
    return crc;
}

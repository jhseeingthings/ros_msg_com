#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
#from后边是自己的包.msg，也就是自己包的msg文件夹下，test是我的msg文件名test.msg
from first_one.msg import Num
from first_one.msg import Lane

def talker():
    pub = rospy.Publisher('chatter', Num, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    pub2 = rospy.Publisher('chatting', Num, queue_size=10)
    #rospy.init_node('anotherTalker', anonymous=True)

    rate = rospy.Rate(10) # 10hz
    n = 0
    while not rospy.is_shutdown():
   		#temp为到时候要用于传输的信息
        #temp = 1
        msg = Num()
        msgs = Lane()
        msgs.id = 4
        msgs.relation = 5
        msg.lanes.append(msgs)
        msgs1 = Lane()
        msgs1.id = 6
        msgs1.relation = 7
        msg.lanes.append(msgs1)
        msgs1.id = 9
        msgs1.relation = 10
        msg.lanes.append(msgs1)
        msg.num = 1 + n
        
        msg.x = 2
        msg.y = 3
        #这里test就像构造函数般使用，若有多个msg，那么写成test(a,b,c,d...)
        rospy.loginfo(msg)
        pub.publish(msg)
	
        n=n+1
        msg2 = Num()
	msg2.num = 11111111
	pub2.publish(msg2)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


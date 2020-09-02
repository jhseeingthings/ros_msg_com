#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from first_one.msg import Num
import copy
import numpy as np

data2=None
data3 =None

def callback(data):
#传过来的所有msg为data，其中data.后边的变量看msg文件写，比如我的是float32[] data,那么我就是data.data
    data1 = data
    global data2
    data2 = A(data)
    global data3
    data3 = data.num
    data2.virtual.append(16)
    #data2.virtual[1] = 18
    #data2.lane.length = 15
    rospy.loginfo(len(data2.lane))
    rospy.loginfo(data.num)
    rospy.loginfo(data.lanes)
    rospy.loginfo(data2.virtual[0])
    #rospy.loginfo(data2.length)
    rospy.loginfo(data2.lane1[0].id)
    rospy.loginfo(data2.lane)

    function1()


def callback2(data):
    rospy.loginfo(data3)

    aaa = Num()
    aaa.num = 110
    rospy.loginfo(aaa.num)

    if data3 == 10:
	    rospy.loginfo(".........000000000000000000")
	    rospy.loginfo(data.num)
	    rospy.loginfo(".........000000000000000000")
    else:
            print("oppsfail")
            rospy.loginfo("------%d" %data3)
            rospy.loginfo(" fail")
	    pass

def function1():
    #rospy.loginfo(data2.lane1)
    rospy.loginfo("uni")
    pass

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Num, callback)
    rospy.Subscriber('chatting',Num, callback2)
    rospy.loginfo("hello")
    #rospy.loginfo(data2.virtual[0])
    #rospy.loginfo(data2.length)
    #rospy.loginfo(data2.lane1[0].id)
    #rospy.loginfo(data2.lane)
    #rospy.loginfo(data2.lane1)



class A:
    def __init__(self, data):
        self.data = data
        self.lane   = copy.deepcopy(data.lanes)
        self.lane1   = data.lanes
        #self.lane.id = data.lanes.id
        self.virtual = []
        #self.lane[0].length = 0


if __name__ == '__main__':
    listener()
    rospy.loginfo("llllllllllllllllllllll")
    rospy.spin()
    listener()
    rospy.spin()




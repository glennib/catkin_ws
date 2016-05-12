#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_glenn(req):
    print "Returning [%s + %s = %s]" %(req.a, req.b, (req.a + req.b))
    print "But waiting a little bit..."
    rospy.sleep(1.0)
    return AddTwoIntsResponse(req.a + req.b)

def glenn_server():
    rospy.init_node('glenn_server')
    s = rospy.Service('glenn', AddTwoInts, handle_glenn)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    glenn_server()



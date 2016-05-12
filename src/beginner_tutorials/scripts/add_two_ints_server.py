#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy
import mutex

m = mutex.mutex()

def handle_add_two_ints(req):
    print "Server waiting for mutex"
    while not m.testandset():
        pass
    print "Mutex aquired"

    print "Returning [%s + %s = %s]" %(req.a, req.b, (req.a + req.b))
    rospy.sleep(10.0)


    m.unlock()
    print "Mutex unlocked"

    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()



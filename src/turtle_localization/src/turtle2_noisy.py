#! /usr/bin/python3
import rospy, turtlesim
import turtlesim.srv # uuden turtlen luominen
from geometry_msgs.msg import TwistWithCovarianceStamped # kuunteluviesti
from geometry_msgs.msg import Twist # ohjausviesti

def twist_callback(msg):

    twist_to_turtle2 = Twist()
    twist_to_turtle2.linear.x = msg.twist.twist.linear.x
    twist_to_turtle2.angular.z = msg.twist.twist.angular.z

    pub_twist.publish(twist_to_turtle2)

if __name__ == "__main__":

    rospy.wait_for_service('spawn')
    # new turtle2
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn) 
    spawner(5.544,5.544,0,'turtle2')

    rospy.wait_for_service('/turtle2/set_pen')
    pen_setter = rospy.ServiceProxy('turtle2/set_pen', turtlesim.srv.SetPen)
    pen_setter(125,125,125,5,0)

    rospy.init_node('turtle2_twist_remapper_node')
    rospy.Subscriber('turtle1/sensor/twist', TwistWithCovarianceStamped, twist_callback)
    pub_twist = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)

    while not rospy.is_shutdown():
        continue
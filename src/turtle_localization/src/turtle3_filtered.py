#! /usr/bin/python3
import rospy, turtlesim, turtlesim.srv
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

def twist_callback(msg):

    twist_to_turtle3 = Twist()
    twist_to_turtle3.linear.x = msg.twist.twist.linear.x
    twist_to_turtle3.angular.z = msg.twist.twist.angular.z

    pub_twist.publish(twist_to_turtle3)

if __name__ == "__main__":

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5.544,5.544,0,'turtle3')

    rospy.wait_for_service('/turtle3/set_pen') # rosservice list
    pen_setter = rospy.ServiceProxy('/turtle3/set_pen', turtlesim.srv.SetPen)
    pen_setter(0,0,0,5,0)

    rospy.init_node('turtle3_twist_remapper_node')
    rospy.Subscriber('odometry/filtered_twist', Odometry, twist_callback)
    pub_twist = rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=1)

    rospy.spin()

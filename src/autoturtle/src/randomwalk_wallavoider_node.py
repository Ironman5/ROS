#! /usr/bin/python3
import rospy, random
from geometry_msgs.msg import Twist # ohjaustieto
from turtlesim.msg import Pose  # paikkatieto

def callback(pose):

    vel_msg = Twist() 

    if pose.x > 10:
        vel_msg.angular.z = pose.theta + 0.5 #random.randint(0,2) pose.theta +
        vel_msg.linear.x = 2
    elif pose.x < 1:
        vel_msg.angular.z = pose.theta - 3.5
        vel_msg.linear.x = 2
    elif pose.y > 10:
        vel_msg.angular.z = pose.theta + 0.5
        vel_msg.linear.x = 2
    elif pose.y < 1:        
        vel_msg.angular.z = pose.theta - 3.5
        vel_msg.linear.x = 2
    else:
        vel_msg.angular.z = random.randint(-5,5)
        vel_msg.linear.x = random.randint(1,4)
    
    velocity_publisher.publish(vel_msg)

rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
pose_subscriber = rospy.Subscriber('turtle1/pose', Pose, callback)

while not rospy.is_shutdown():
    continue
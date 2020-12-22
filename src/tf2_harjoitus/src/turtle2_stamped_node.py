#! /usr/bin/python3
import rospy, turtlesim
from geometry_msgs.msg import PoseStamped
from turtlesim.msg import Pose


def pose_callback(msg):

    twist_to_send = PoseStamped() # geometry_msgs/PoseStamped.msg
    twist_to_send.header.seq = twist_to_send.header.seq + 1
    twist_to_send.header.stamp = rospy.Time.now()
    twist_to_send.header.frame_id = 'base link'
    twist_to_send.pose.position.x = msg.linear_velocity # turtlesim/Pose.msg 
    twist_to_send.pose.position.y = 0.0
    twist_to_send.pose.position.z = 0.0
    twist_to_send.pose.orientation.x = 0.0
    twist_to_send.pose.orientation.y = 0.0
    twist_to_send.pose.orientation.z = msg.angular_velocity 
    twist_to_send.pose.orientation.w = 0.0

    pub_twist.publish(twist_to_send)

if __name__ == "__main__":

    rospy.init_node('turtle2_pose_stamped')
    rospy.Subscriber('turtle2/pose', Pose, pose_callback)
    pub_twist = rospy.Publisher('turtle2/pose_stamped', PoseStamped, queue_size = 1)  
    
    while not rospy.is_shutdown():
        continue



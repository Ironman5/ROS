#! /usr/bin/python3
import rospy, tf2_ros, turtlesim, random 
from geometry_msgs.msg import TwistWithCovarianceStamped
from turtlesim.msg import Pose

random_noise_linear = rospy.get_param("random_noise_linear")
systemic_noise_linear = rospy.get_param("systemic_noise_linear")
random_noise_angular = rospy.get_param("random_noise_angular")
systemic_noise_angular = rospy.get_param("systemic_noise_angular")

def pose_callback(msg):

    twist_to_send = TwistWithCovarianceStamped()
    twist_to_send.header.seq = twist_to_send.header.seq + 1 
    twist_to_send.header.stamp = rospy.Time.now()
    twist_to_send.header.frame_id = 'base_link'
    # turtlesim/Pose.msg -> msg.linear_velocity
    twist_to_send.twist.twist.linear.x = msg.linear_velocity * (1 + systemic_noise_linear + random.uniform(0, random_noise_linear))
    twist_to_send.twist.twist.linear.y = 0.0
    twist_to_send.twist.twist.linear.z = 0.0
    twist_to_send.twist.twist.angular.x = 0.0
    twist_to_send.twist.twist.angular.y = 0.0
    twist_to_send.twist.twist.angular.z = msg.angular_velocity * (1 + systemic_noise_angular + random.uniform(0, random_noise_angular))
    twist_to_send.twist.covariance = systemic_noise_linear**2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,systemic_noise_angular**2

    pub_twist.publish(twist_to_send)

if __name__ == "__main__":

    rospy.init_node('turtle_odometry')
    rospy.Subscriber('turtle1/pose', Pose, pose_callback)
    pub_twist = rospy.Publisher('turtle1/sensor1/twist', TwistWithCovarianceStamped, queue_size = 1)
    
    while not rospy.is_shutdown():
        continue

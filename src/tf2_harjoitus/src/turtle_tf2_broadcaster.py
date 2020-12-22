#! /usr/bin/python3
import rospy, tf_conversions
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):

    transform_broadcaster = TransformBroadcaster()
    transformed_msg = TransformStamped()

    transformed_msg.header.stamp = rospy.Time.now()
    transformed_msg.header.frame_id = 'world'
    transformed_msg.child_frame_id = turtlename
    transformed_msg.transform.translation.x = msg.x
    transformed_msg.transform.translation.y = msg.y
    transformed_msg.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0,0,msg.theta)
    transformed_msg.transform.rotation.x = q[0]
    transformed_msg.transform.rotation.y = q[1]
    transformed_msg.transform.rotation.z = q[2]
    transformed_msg.transform.rotation.w = q[3]

    transform_broadcaster.sendTransform(transformed_msg)

if __name__ == "__main__":  

    rospy.init_node('turtle1_broadcaster')
    turtle_name = rospy.get_param('~turtle') # useampi turtle-node
    rospy.Subscriber('/%s/pose' % turtle_name, Pose, handle_turtle_pose, turtle_name) 
    rospy.spin()



""" #! /usr/bin/python3
import rospy, tf_conversions, random
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):

    transform_broadcaster = TransformBroadcaster()
    transformed_msg = TransformStamped()

    transformed_msg.header.stamp = rospy.Time.now()
    transformed_msg.header.frame_id = 'world'
    transformed_msg.child_frame_id = turtlename

    if turtlename == 'turtle1':
        transformed_msg.transform.translation.x = msg.x + random.randint(0,1)
        transformed_msg.transform.translation.y = msg.y + random.randint(0,1)
        transformed_msg.transform.translation.z = 0.0
        q = tf_conversions.transformations.quaternion_from_euler(0,0,msg.theta + random.randint(0,1))
    else:
        transformed_msg.transform.translation.x = msg.x
        transformed_msg.transform.translation.y = msg.y
        transformed_msg.transform.translation.z = 0.0
        q = tf_conversions.transformations.quaternion_from_euler(0,0,msg.theta)

    transformed_msg.transform.rotation.x = q[0]
    transformed_msg.transform.rotation.y = q[1]
    transformed_msg.transform.rotation.z = q[2]
    transformed_msg.transform.rotation.w = q[3]

    transform_broadcaster.sendTransform(transformed_msg)

if __name__ == "__main__":  

    rospy.init_node('turtle1_broadcaster')
    turtle_name = rospy.get_param('~turtle') # useampi turtle-node
    rospy.Subscriber('/%s/pose' % turtle_name, Pose, handle_turtle_pose, turtle_name)
    rospy.spin() """


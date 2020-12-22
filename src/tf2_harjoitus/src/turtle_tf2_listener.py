#! /usr/bin/python3
import rospy, math, turtlesim.srv, tf
from geometry_msgs.msg import Twist
from tf2_ros import Buffer, TransformListener

if __name__ == "__main__":

    rospy.init_node('turtle1_listener')
    tfBuffer = Buffer()
    listener = TransformListener(tfBuffer)
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name = rospy.get_param('turtle','turtle2')
    spawner(4,2,0,turtle_name) 

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, Twist, queue_size=1)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rate.sleep()
            continue

        msg = Twist()
        msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x**2 + trans.transform.translation.y**2)
        msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)

        turtle_vel.publish(msg)
        rate.sleep()
import rclpy as rp
from rclpy.node import Node

from geometry_msgs.msg import Twist

class TurtlesimSubscriber(Node):

	def __init__(self):
		super().__init__('turtlesim_subscriber')
		self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback(self):
		msg = Twist()
		msg.linear.x = 70.0
		msg.angular.z = 15.0
		self.publisher.publish(msg)
		
def main(args=None):
	rp.init(args=args)

	turtlesim_subscriber = TurtlesimSubscriber()
	rp.spin(turtlesim_subscriber)

	turtlesim_subscriber.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()
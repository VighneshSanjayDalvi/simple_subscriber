import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")

        self.sub_ = self.create_subscription(String, "Hello", self.msgCallback, 10)

    def msgCallback(self, msgs):
        self.get_logger().info("I heard %s successfully!" %msgs.data)

def main():
    rclpy.init() # rclpy initialized
    simple_subscriber = SimpleSubscriber() # creating instance of the class
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node() # destroys node on ctrl + c
    rclpy.shutdown()


if __name__ == '__main__':
    main()

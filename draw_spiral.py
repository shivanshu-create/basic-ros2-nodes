#!/usr/bin/env python3
import rclpy
from rclpy.node import Node # to use node class
from geometry_msgs.msg import Twist 

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_spiral")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #here 10 is q size to create a buffer
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw spiral node has been started")
        self.pp = 0
    def send_velocity_command(self):
        msg = Twist() # to crate a messege object from the class Twist
        msg.linear.x = 2.0 + self.pp
        msg.angular.z = 2.5133
        self.pp += 0.5
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node # to use node class
from geometry_msgs.msg import Twist 
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult

class DrawVariableSpiralNode(Node):

    def __init__(self):
        super().__init__("draw_variable_spiral")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #here 10 is q size to create a buffer
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw spiral node has been started")

        self.pp = 0

        self.declare_parameter('spiral_linear_velocity', 0.1)
        self.declare_parameter('spiral_angular_velocity', 1.0)

        self.spiral_linear_velocity_ = self.get_parameter('spiral_linear_velocity').value
        self.spiral_angular_velocity_ = self.get_parameter('spiral_angular_velocity').value

        self.add_on_set_parameters_callback(self.velocity_change)

    def velocity_change(self, params):
            for param in params:
                if param.name == 'spiral_linear_velocity':
                    self.spiral_linear_velocity_ = param.value
                if param.name == 'spiral_angular_velocity':
                    self.spiral_angular_velocity_ = param.value

            return SetParametersResult(successful=True)

        
    def send_velocity_command(self):
        msg = Twist() # to crate a messege object from the class Twist
        msg.linear.x = self.spiral_linear_velocity_ + self.pp
        msg.angular.z = self.spiral_angular_velocity_
        self.pp += 0.02
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawVariableSpiralNode()
    rclpy.spin(node)
    rclpy.shutdown()
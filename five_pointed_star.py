#!/usr/bin/env python3
import rclpy
from rclpy.node import Node # to use node class
from geometry_msgs.msg import Twist 

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_five_pointed_star")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #here 10 is q size to create a buffer
        self.state = "f"
        self.time = 0.0
        self.count = 0
        self.timer_ = self.create_timer(0.1, self.send_velocity_command)
        

    def send_velocity_command(self):
        msg = Twist() # to crate a messege object from the class Twist
        
        if self.state == "f":
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.time += 0.1
            if self.time > 1.0:
                self.state = "r"
                self.time = 0.0
                self.count += 1

        elif self.state == "r":
            if self.count % 2 == 1:
                msg.linear.x = 0.0
                msg.angular.z = 2.5133
                self.time += 0.1
                if self.time > 1.0:
                    self.state = "f"
                    self.time = 0.0
            else:
                msg.linear.x = 0.0
                msg.angular.z = -2.5133
                self.time += 0.1
                if self.time > 0.5:
                    self.state = "f"
                    self.time = 0
        
        self.cmd_vel_pub_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
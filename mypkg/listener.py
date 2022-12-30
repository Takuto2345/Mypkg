# SPDX-FileCopyrightText : 2022 Takuto Kanno
# SPDX-License-Identifirt: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self, node):
        self.subscription = self.create_subscription(Int16, "countup", cb, 10)
    self.subscription
    def cb(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
#pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)

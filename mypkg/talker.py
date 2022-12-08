import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def_init_(self):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0

rclpy.init()
node = Node("talker")
talker = Talker()

#pub = node.create_publisher(Int16, "countup", 10)
#n = 0

def cb():
    msg = Int16()
    msg.data = taler.n
    talker.pub.publish(msg)
    talker.n += 1

node.create_timer(0.5,cb)
rclpy.spin(node)

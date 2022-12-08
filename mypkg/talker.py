import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):#initに__（アンダーバーが必要なのはselfとnodeに変更を設定できるようにするためであり、今回の場合一度初期値にするために必要らしい
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
            msg = Int16()
            msg.data = self.n
            self.pub.publish(msg)
            self.n += 1




rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)

#def cb():
#    msg = Int16()
#   msg.data = talker.n
#    talker.pub.publish(msg)
#    talker.n += 1

#node.create_timer(0.5,cb)
#rclpy.spin(node)

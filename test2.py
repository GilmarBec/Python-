import time

from src.node.my_node import MyNode

node = MyNode("192.168.0.1", 10002)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(10)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10003)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()
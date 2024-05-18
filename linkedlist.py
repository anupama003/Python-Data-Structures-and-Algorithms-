class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


def print_linked_list(head):
  current = head
  while current is not None:
    print(current.data, end=' --> ')
    current = current.next
  print("None")


if __name__ == '__main__':
  # Creating nodes
  node1 = Node(10)
  node2 = Node(20)
  node3 = Node(30)
  node4 = Node(40)

  # Linking nodes
  node1.next = node2
  node2.next = node3
  node3.next = node4

  # Printing linked list
  print_linked_list(node1)

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

  # Inserting Node at the end
def insert_at_end(head, value):
  new_node = Node(value)
  if head is None:
    return new_node
  current = head
  while current.next is not None:
    current = current.next
  current.next = new_node
  return head

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

  # insert into end of linked list
  insert_at_end(node1, 50)
  insert_at_end(node1, 60)
  insert_at_end(node1, 70)
  insert_at_end(node1, 80)
  insert_at_end(node1, 90)
  insert_at_end(node1, 100)

  # Printing linked list
  print_linked_list(node1)



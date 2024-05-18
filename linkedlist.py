class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

#print created nodes
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

# Inserting Node at the beginning
def create_at_beginning(head, value):
  head = node1
  new_node = Node(value)
  new_node.next = head
  head = new_node
  return head

# Inserting Node at a specific position
def insert_at_position(head, value, position):
  new_node = Node(value)
  if position == 0:
    new_node.next = head
    head = new_node
    return head
  current = head
  for i in range(position - 1):
    if current is None:
      return head
    current = current.next
  new_node.next = current.next
  current.next = new_node
  return head

# Deleting Node at the end
def delete_at_end(head):
  current = head
  while current.next.next is not None:
    print(current.data, end=' --> ')
    current = current.next
  current.next = None

# Deleting Node at the beginning
def delete_at_beginning(head):
  if head is not None:
    head = head.next
  current = head
  while current.next is not None:
    print(current.data, end=' --> ')
    current = current.next
  print('None')

if __name__ == '__main__':
  # createing nodes
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

  # insert into beginning of linked list
  create_at_beginning(node1, 5)
  create_at_beginning(node1, 4)

  # insert into specific position of linked list
  insert_at_position(node1, 15, 2)

  # delete from end of linked list
  delete_at_end(node1)

  # delete from beginning of linked list
  delete_at_beginning(node1)
  
  # Printing linked list
  print_linked_list(node1)



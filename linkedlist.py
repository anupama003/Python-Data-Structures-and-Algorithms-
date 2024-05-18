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

'''Alternate way:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' --> ')
        current = current.next
    print("None")

def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, position, value):
    if position < 0:
        print("Invalid position")
        return head
    if position == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node
    current = head
    while position > 1 and current is not None:
        current = current.next
        position -= 1
    if current is None:
        print("Invalid position")
        return head
    new_node = Node(value)
    new_node.next = current.next
    current.next = new_node
    return head

def delete_at_position(head, position):
    if head is None:
        print("Linked list is empty")
        return None
    if position < 0:
        print("Invalid position")
        return head
    if position == 0:
        return head.next
    current = head
    while position > 1 and current.next is not None:
        current = current.next
        position -= 1
    if current.next is None:
        print("Invalid position")
        return head
    current.next = current.next.next
    return head

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

def delete_at_beginning(head):
    if head is None:
        print("Linked list is empty")
        return None
    return head.next

def delete_at_end(head):
    if head is None:
        print("Linked list is empty")
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
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

    # Inserting a node at the end
    head = insert_at_end(node1, 50)

    # Printing linked list
    print("Linked list after inserting at the end:")
    print_linked_list(head)

    # Inserting a node at position 2
    head = insert_at_position(head, 2, 25)

    # Printing linked list
    print("\nLinked list after inserting at position 2:")
    print_linked_list(head)

    # Deleting node at position 3
    head = delete_at_position(head, 3)

    # Printing linked list
    print("\nLinked list after deleting at position 3:")
    print_linked_list(head)

    # Inserting a node at the beginning
    head = insert_at_beginning(head, 5)

    # Printing linked list
    print("\nLinked list after inserting at the beginning:")
    print_linked_list(head)

    # Deleting node at the beginning
    head = delete_at_beginning(head)

    # Printing linked list
    print("\nLinked list after deleting at the beginning:")
    print_linked_list(head)

    # Deleting node at the end
    head = delete_at_end(head)

    # Printing linked list
    print("\nLinked list after deleting at the end:")
    print_linked_list(head)
'''



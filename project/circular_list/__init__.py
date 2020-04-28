# Create the node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Create the doubly linked list class
class circularList:

   def __init__(self):
      self.head = None
      self.last = None

# Define the push method to add elements at the begining
   def push(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = self.head

      if self.head is not None:
         self.head.prev = NewNode

      if self.last is None:
        self.last = NewNode

      #Aggiornamento puntatore prev testa alla coda
      NewNode.prev = self.last
      
      self.head = NewNode

      #Aggiornamento puntatore ultimo nodo alla testa
      self.last.next = self.head

      return NewNode

# Define the append method to add elements at the end
   def append(self, NewVal):

      #Caso lista vuota, funzionamento come push
      if self.head is None:
        return self.push(NewVal)

      NewNode = Node(NewVal)

      #Link nodo appeso alla testa della lista
      NewNode.next = self.head

      #Aggiornamento puntatore next di last al nuovo last
      self.last.next = NewNode

      #Aggiornamento puntatore nuova last al last precedente
      NewNode.prev = self.last

      #Aggiornamento nuovo last
      self.last = NewNode

      return NewNode

# Define the method to print
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

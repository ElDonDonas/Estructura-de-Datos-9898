class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

def promedio(lista):
    suma = 0
    n = 0
    for num in lista:
        suma += num
        n += 1
    if n == 0:
        return None
    else:
        return suma / n

# Ejemplo de uso
lista = LinkedList()
lista.append(2)
lista.append(4)
lista.append(6)
lista.append(8)
lista.append(10)

print(promedio(lista))  # Imprime 6.0

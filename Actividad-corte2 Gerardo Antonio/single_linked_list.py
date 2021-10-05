import math

class Single_linked_list:
  class Node:
    #Metodo Constructor Nodo
    def __init__(self,value):
      self.value = value
      self.next = None
  
  #Metodo Constructor Clase Single_linked_list
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  #Metodos de la clase Single_linked_list
  #Metodo #1:Mostrar los elementos que conforman la lista
  def show_elements(self):
    array = []
    current_node = self.head #Nodo Actual
    #Empezamos por la cabeza de la lista
    while current_node != None:
      #Mientras exista un elemento en la cabeza de la lista,el valor se añade a lista array
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)
  
  #Metodo #2:Agregar un elemento al inicio de la lista
  def prepend(self,value):
    new_node = self.Node(value)
    #Si la lista no contiene elementos,la cabeza y cola pasan a tener el mismo valor
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    #Actualizamos el tamaño de la lista
    self.length += 1
  
  #Metodo #3:agregar elemento al final de la lista
  def append(self):
    while True:
      try:
        cant_node = int(input('   Cantidad de nodos a crear:  '))
        for node_item in range(cant_node):
          value = input(' Ingresa el valor del nodo:  ')
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
          else:
            self.tail.next = new_node
            self.tail = new_node
          self.length += 1
        self.show_elements()
        break
      except ValueError:
        print('   Error, se esperaba un valor numerico')
  
  #Metodo #4:eliminar el primer elemento de la lista
  def shift(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      self.length -= 1
      return print(delete_node.value)
  
  #Metodo #5:eliminar ultimo elemento de la lista
  def pop(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      #Recorremos la lista para identificar el ultimo elemento
      current_node = self.head
      new_tail = current_node
      while current_node.next != None:
        new_tail = current_node
        current_node = current_node.next
      self.tail = new_tail
      self.tail.next = None
      self.length -= 1
      return print(current_node.value)
  
  #metodo #6: Consultar el valor del nodo a partir del indice que ingresa el usuario
  def get(self, index):
    if index == self.length -1:
      return self.tail
    if index == 0:
      return self.head
    elif not(index >= self.length or index <0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      return current_node
    else:
      return None
  
  #metodo 7:actualizar el valor que contiene el nodo consultado
  def update(self,index,value):
    update_node = self.get(index)
    #validamos si encontramos el nodo
    if update_node != None:
      update_node.value = value
    else:
      return None
  
  #metodo #8:insertar un nodo en determinada posicion
  def insert(self,index,value): #posicion despues
    #Se añadira el elemento al final de la Single_linked_List
    if index == self.length -1:
      return self.append(value)
    elif not(index >= self.length or index < 0):
      new_node = self.Node(value)
      preview_node = self.get(index)
      next_node = preview_node.next
      preview_node.next = new_node
      new_node.next = next_node
      self.length += 1
    else:
      return None
  #metodo 9:Eliminar un elemento determinado
  def remove(self,index):
    if index == 0:
      return self.shift()
    elif index == self.length -1:
      return self.pop()
    elif not (index >= self.length or index < 0):
      preview_node = self.get(index-1)
      delete_node = preview_node.next
      preview_node.next = delete_node.next
      delete_node.next = None
      self.length -= 1
      return delete_node
    else:
      return None
  
  #metodo 10:Agregar solo numeros pares
  def append_pair(self,value):
    while True:
      if value % 2 == 0:
        new_node = self.Node(value)
        break
      else:
        value = int(input('El valor ingresado fue impar\n Digite nuevamente el valor del Nodo:  '))
    
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
  
  #metodo 11:elevar los nodos que esten en las posiciones pares al cuadrado
  def pow_nodes_pairs(self):
    current_node = self.head #Nodo Actual
    #Empezamos por la cabeza de la lista
    while current_node != None:
      #Mientras exista un elemento en la cabeza de la lista,el valor se añade a lista array
      if current_node.value % 2 == 0:
        current_node.value = math.pow(current_node.value,2)
      current_node = current_node.next
  
  #Metodo 12:Validar que un valor este dentro de la lista enlazada
  def validate_value(self,user_value):
    bandera = False
    current_node = self.head
    while current_node != None:
      if current_node.value == user_value:
        bandera = True
        current_node = current_node.next
    
    return bandera
  
  #Metodo 13: Agregar Nodo por valor
  def append_2(self,value):
    new_node = self.Node(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
  
  #Metodo 14:Invertir Lista
  def reverse(self):
    pre = sig = None
    i = self.head

    while i:
      sig = i.next
      i.next = pre
      pre = i
      i = sig
    self.head = pre
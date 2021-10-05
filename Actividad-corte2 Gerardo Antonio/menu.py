#Librerias
import math
from single_linked_list import Single_linked_list
from colorama import Fore, init
init()

class Menu:
  #Metodo Constructor
  def __init__(self):
    self.opc_menu = 0
    self.lista_principal = Single_linked_list()
  
  #Metodos de la clase
  def mostrar_menu(self):
    print('     ****Bienvenido Señor/a Usuario****')
    print('   ***Al Programa de Listas Enlazadas Simples***')
    print(' **Opciones de Servicio**')
    print(' 1.Agregar Nodo por Valor\n  2.Buscar Nodo por indice y Agregar el valor de la raíz cuadrada de ese nodo al inicio de la lista\n 3.Eliminar Nodo por Indice y Agregar el valor al cuadrado de ese Nodo al final de la lista\n  4.Mostrar Lista\n 5.Mostrar Lista Invertida\n 6.Salir')
  
  def validar_cantidad_nodos(self,cant_nodos):
    bandera_funcion = True
    while bandera_funcion:
      if cant_nodos <= 0:
        print('Error Cantidad de Nodos Invalida')
        cant_nodos = int(input('  Digite nuevamente la cantidad de nodos a agregar: '))
      else:
        bandera_funcion = False
  
  def validar_valor_nodo_neg(self,valor_n):
    bandera_funcion = True
    while bandera_funcion:
      if valor_n < 0:
        print('Error Valor Negativo')
        valor_n = int(input(' Digite Nuevamente el valor del Nodo: '))
      else:
        bandera_funcion = False
  
  def mostrarMenu2(self,respuestaSN):
    while True:
      if respuestaSN.lower() != 'si' and respuestaSN.lower() != 'sí' and respuestaSN.lower() != 'no':
        respuestaSN = input(Fore.RED+"Respuesta No Valida \nDesea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
      elif respuestaSN.lower() == 'si' or respuestaSN.lower() == 'sí':
        print('\n\n')
        self.mostrar_menu()
        respuestaRegresoM = int(input(Fore.CYAN+'Tu respuesta: '+Fore.RESET))
        self.mostrar_opcion_menu(respuestaRegresoM)
        break
      elif respuestaSN.lower() == 'no':
        print(Fore.GREEN+'Muchas Gracias Por Diligenciar el Formulario')
        break
  
  def mostrar_opcion_menu(self,opcionU):
    bandera = True

    while bandera:
      if opcionU != 1 and opcionU != 2 and opcionU != 3 and opcionU != 4 and opcionU != 5 and opcionU != 6:
        print(' Opcion Invalida')
        self.mostrar_menu()
        opcionU = int(input(' Tu respuesta: '))
        self.mostrar_opcion_menu(opcionU)
      elif opcionU == 1:
        print('Escogiste La opcion 1')
        print(' Agregar Nodo por Valor')
        cantidad_nodos = int(input('  Digite la cantidad de nodos a agregar: '))
        self.validar_cantidad_nodos(cantidad_nodos)
        #Iterador 
        i = 0

        while i < cantidad_nodos:
          valor_nodo_agregado = float(input(' Digite el valor del Nodo: '))
          self.validar_valor_nodo_neg(valor_nodo_agregado)
          self.lista_principal.append_2(valor_nodo_agregado)
          i += 1
        
        regresoMenu = input(Fore.LIGHTCYAN_EX+"Desea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
        self.mostrarMenu2(regresoMenu)
        bandera = False
      elif opcionU == 2:
        print(' Escogiste La opcion 2 del menu')
        indice_nodo = int(input(' Digite el indice del Nodo a Buscar: '))
        nodo_buscado = self.lista_principal.get(indice_nodo)

        if nodo_buscado != None:
          valor_raiz_cuadrada = math.sqrt(nodo_buscado.value)
          self.lista_principal.prepend(valor_raiz_cuadrada)
          print(' Proceso Completado')
        else:
          print('No se pudo realizar el proceso')
        
        regresoMenu = input(Fore.LIGHTCYAN_EX+"Desea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
        self.mostrarMenu2(regresoMenu)
        bandera = False
      elif opcionU == 4:
        print(' Escogiste la opcion 4')
        print('La lista Enlazada Simple es: ')
        self.lista_principal.show_elements()

        regresoMenu = input(Fore.LIGHTCYAN_EX+"Desea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
        self.mostrarMenu2(regresoMenu)
        bandera = False
      elif opcionU == 3:
        print(' Escogiste la opcion 3')
        indice_nodo = int(input(' Digite el indice del Nodo a Buscar: '))
        self.lista_principal.remove(indice_nodo)
        nodo_buscado2 = self.lista_principal.get(indice_nodo)
        
        if nodo_buscado2 != None:
          valor_cuadrado = math.pow(nodo_buscado2.value,2)
          self.lista_principal.append_2(valor_cuadrado)
          print(' Proceso Completado')
        else:
          print('No se pudo realizar el proceso')
        
        regresoMenu = input(Fore.LIGHTCYAN_EX+"Desea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
        self.mostrarMenu2(regresoMenu)
        bandera = False
      elif opcionU == 6:
        print(' Escogiste la opcion 6')
        print('   Salir')
        print(' Muchas Gracias atte: Gasp')
        bandera = False
      elif opcionU == 5:
        print(' Escogiste la opcion 5')
        print(' La lista invertida es: ')
        self.lista_principal.reverse()
        self.lista_principal.show_elements()

        regresoMenu = input(Fore.LIGHTCYAN_EX+"Desea Realizar otra opción del menu (Si,No) \nTu respuesta: "+Fore.RESET)
        self.mostrarMenu2(regresoMenu)
        bandera = False
  def diligenciar_formulario(self):
    self.mostrar_menu()
    respuesta = int(input(' tu respuesta: '))
    self.mostrar_opcion_menu(respuesta)
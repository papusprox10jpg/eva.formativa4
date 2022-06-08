import numpy as np
#Borrado consola
import os
def clear():
    os.system('cls')
clear()

#Continuar - borrado de consola
from time import sleep
def ir_menu():
  sleep(1)
  next = input("Para volver al menú principal presione una tecla.")
  clear()

#Mostrar asientos disponibles
#Según el requisito: Mostrará por pantalla todos los asientos disponibles con su número de asiento y los no disponibles los con una “X”
def disp_asiento (mapa_avion):#agrego nombre más claro.
  print("*"*3,"Asientos del  avión","*"*3)
  for i in range(9):
    for j in range(9):
      print(mapa_avion[i][j], end=" ")
    print()
  print()
  print("1.Asientos normales: del 1 al 30. \n2. Asientos VIP: del 31 al 42.")
  print()

#Contar asientos ocupados
def cant_ocupado (mapa_avion):
  cant_disp=0
  for fila in mapa_avion: #indexación de cada fila de la matriz
    for asiento in fila : #indexación en cada valor de cada fila
      if asiento == "X": #si algun valor es X, retorna disponibildiad
        cant_disp+=1
  print("Asientos ocupados:", cant_disp)
  print()

#Funcion telefono 
validacion = True
def validar_telefono():
  cont = 0
  while validacion:
    try:
      telefono = int(input("\nIngrese su numero de telefono: (comenzar con el numero 9)\t"))
      if len(str(telefono)) == 9:
        for i in str(telefono):
          if "9" in i:
            return telefono
            break
          else:
            cont += 1
        if cont >= 1:
          print("\nError, Su Telefono debe tener un 9 al principio")
          cont = 0
        else:
          break
      else:
        print("\nError, su numero debe tener 9 digitos")
    except ValueError:
      print("\nError, ingrese su telefono como numeros")

#Funcion compra
def compra(compra_asiento,banco,avion,asiento):
  disp_avion = avion.strip()
  donde = np.where(disp_avion == asiento)
  avion[tuple(donde)] = "X"
  if compra_asiento > 0 and compra_asiento <= 30 :
    normal = 0
    normal += 78900
    if banco:
      descuento = normal * 0.15
      normal = normal - descuento
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* ","asientos normales\t","$78.900" )
      if banco:
        print("* ","descuento 15%\t","$11.835")
      print("*"*40)
      print("                           su total es:\t", round(normal))
  if compra_asiento >= 31 and compra_asiento <= 42:
    vip = 0
    vip += 240000
    if banco:
      descuento = vip * 0.15
      vip = vip - descuento
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* "," asientos normales\t","$240.000" )
      if banco:
        print("* ","descuento 15%\t","$36.000")
      print("*"*40)
      print("                           su total es:\t", round(vip))
#Funcion modificar
def modificar_datos(opcion):
  if opcion == 1:
    print("\nModificando nombre: ")
    nom = str(input("\nIngrese su nuevo nombre: \t"))
    return nom
  elif opcion == 2:
    print("\nModificando telefono: ")
    telefono = validar_telefono()
    return telefono

def anular_pasaje(asiento,nombre,rut,telefono,banco):
  #anular datos
  nombre = None ; rut = None ; telefono = None ; banco = None
  return nombre,rut,telefono,banco


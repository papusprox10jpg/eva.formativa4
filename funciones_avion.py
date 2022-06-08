import numpy as np
#Borrado consola
import os
def clear():
    os.system('cls')
    os.system('clear')
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
  print("1.Asientos normales: del 1 al 30. \n2.Asientos VIP: del 31 al 42.")
  print()

#Contar asientos ocupados
def cant_ocupado (mapa_avion):
  cant_ocupados=0
  for fila in mapa_avion: #indexación de cada fila de la matriz
    for asiento in fila : #indexación en cada valor de cada fila
      if asiento == "X" or asiento == " X": #si algun valor es X, retorna disponibildiad
        cant_ocupados+=1
  print("Asientos ocupados:", cant_ocupados)
  print()
  return cant_ocupados

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
def compra(compra_asiento,banco,avion,asiento,normal,vip,total):
  disp_avion = avion.strip()
  donde = np.where(disp_avion == asiento)
  avion[tuple(donde)] = " X"
  if compra_asiento > 0 and compra_asiento <= 30 :
    normal += 78900
    print("\n")
    print("*"*40)
    print("Boleta:")
    print("* ","asientos normales:\t$",round(normal))
    if banco:
      descuento = normal * 0.15
      normal = normal - descuento
      print("* ","descuento 15%:\t$",round(descuento))
    print("*"*40)
  elif compra_asiento >= 31 and compra_asiento <= 42:
    vip += 240000
    print("\n")
    print("*"*40)
    print("Boleta:")
    print("* ","asientos Vip:\t$",round(vip))
    if banco:
      descuento = vip * 0.15
      vip = vip - descuento
      print("* ","descuento 15%:\t$",round(descuento))
    print("*"*40)
  total = total + vip + normal
  print("            su total es:\t$", round(total))
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

def anular_pasaje(avion):
  mapa_avion = np.char.array([["|", " 1", " 2", " 3", "     ", " 4", " 5", " 6", "|"], ["|", " 7", " 8", " 9", "     ", "10", "11", "12", "|"],
                              ["|", "13", "14", "15", "     ", "16", "17", "18", "|"], ["|", "19", "20", "21", "     ", "22", "23", "24", "|"],
                              ["|", "25", "26", "27", "     ", "28", "29", "30", "|"], ["|―", "――", "――", "―", "     ", "―", "――", "――", "―|"],
                              ["|_", "__", "__", "_", "     ", "_", "__", "__", "_|"], ["|", "31", "32", "33", "    ", "34", "35", "36", "|"],
                              ["|", "37", "38", "39", "     ", "40", "41", "42", "|"]])
  while validacion:
    try:
      asiento_nul = int(input("\nIngrese el asiento que desea anular o ingrese 0 para salir: "))
      asiento2 = str(asiento_nul)
      check_avion = valid_compra(asiento2, avion)
      if asiento_nul > 0 and asiento_nul <= 42 and check_avion == False:
        asiento_nul = str(asiento_nul)
        print("\nEl asiento:",asiento_nul,"fue eliminado...")
        break
      elif asiento_nul == 0:
        print("\nVolviendo al menu..")
        break
      elif check_avion == True:
        print("\nError: El asiento esta libre actualmente")
      else:
        print("\nError: Ingrese un numero entre el 1 y el 42")
    except ValueError:
      print("\nError: Ingrese el asiento como un numero")
  if asiento_nul != 0:
    disp_mapa_avion = mapa_avion.strip()
    ub_anul_asiento = np.where(disp_mapa_avion == asiento_nul)
    if asiento_nul in ("1,2,3,4,5,6,7,8,9"):
      avion[tuple(ub_anul_asiento)] = " "+asiento_nul
    else:
      avion[tuple(ub_anul_asiento)] = asiento_nul
    return asiento_nul

def eliminar_datos(nombre,rut,telefono,banco):
  nombre = None ; rut = None ; telefono = None ; banco = None
  return nombre,rut,telefono,banco

#Función no comprar el mismo pasaje
def valid_compra(asiento,avion):
  raw_avion = avion.strip()
  if asiento in raw_avion:
    return True
  else:
    return False

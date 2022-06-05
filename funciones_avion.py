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

#Funcion compra
def compra(compra_asiento,banco):
  if compra_asiento > 0 and compra_asiento <= 30 :
    normal = 0
    normal += 78900
    if banco == "si":
      descuento = normal * 0.15
      normal = normal - descuento
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* "," asientos normales\t","$78.900" )
      print("* ","descuento 15%\t","$11.835")
      print("*"*40)
      print("                           su total es:\t", round(normal))

    else:
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* "," asientos normales\t","$78.900" )
      print("* ","descuento 15%\t","$0")
      print("*"*40)
      print("                           su total es:\t", round(normal))

  if compra_asiento >= 31 and compra_asiento <= 42:
    vip = 0
    vip += 240000
    if banco == "si":
      descuento = vip * 0.15
      vip = vip - descuento
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* "," asientos normales\t","$240.000" )
      print("* ","descuento 15%\t","$36.000")
      print("*"*40)
      print("                           su total es:\t", round(vip))
    else:
      print("\n")
      print("*"*40)
      print("Boleta:")
      print("* "," asientos normales\t","$240.000" )
      print("* ","descuento 15%\t","$0")
      print("*"*40)
      print("                           su total es:\t", round(vip))
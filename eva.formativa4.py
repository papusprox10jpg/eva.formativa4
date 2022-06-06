import funciones_avion as fun
import numpy as np
validacion = True
menu = True 
cont = 0
rut = None
avion = [["|"," 1"," 2"," 3","     "," 4"," 5"," 6","|"],["|"," 7"," 8"," 9","     ","10","11","12","|"],
        ["|","13","14","15","    "," 16","17","18","|"],["|","19","20","21","     ","22","23","24","|"],
        ["|","25","26","27","    "," 28","29","30","|"],["|―","――","――","―","     ","―","――","――","―|"],
        ["|_","__","__","_","     ","_","__","__","_|"],["|","31","32","33","    "," 34","35","36","|"],
        ["|","37","38","39","    "," 40","41","42","|"]]) #Gab/sugerencia: Muevo asiento a arriba para organizar las funciones.
while menu:
  print("\n¡Bienvenido a Vuelos-Duoc!")
  print("\n1. Ver asientos disponibles. \n2. Comprar asientos. \n3. Anular vuelo. \n4. Modificar datos de pasajero. \n5. Salir. \n ")
  while validacion:
    try:
      op = int(input("\nIngrese la opción que desee: \t"))
      if op >=1 and op<=5:
        break
      else:
        print("\nError: Ingrese un numero entre el 1 y 5")
    except ValueError:
      print("\nError: Ingrese la opcion como un numero")
  if op == 1:
    fun.clear()
    fun.disp_asiento(avion)
    fun.cant_ocupado(avion)
    fun.ir_menu()
  elif op == 2:
    fun.clear()
    nom = str("\nIngrese su nombre: \t")
    while validacion:
      try:
        rut = int(input("\nIngrese su RUT: \t"))
        if rut >= 5000000 and rut <= 99999999:
          break
        else:
          print("\nError: RUT inválido, ingrese correctamente ")
      except ValueError:
        print("\nError, ingrese su rut sin puntos ni digito verificador")
    while validacion:
      try:
        telefono = (input("\nIngrese su numero de telefono: (comenzar con el numero 9)\t"))
        if len(telefono) == 9:
          break
        else :
          print("\nError, su numero debe tener 9 digitos")
      except ValueError:
        print("\nError, ingrese su telefono como numero ")
        
      for i in telefono:
        if "9" in i:
          break
        else:
          cont += 1
      if cont >= 1:
        print("\nError, Su Telefono debe tener un 9 al principio")
        cont = 0
    while validacion:
      banco = input("\nPertenece al bancoDuoc: \t")
      banco.lower()
      if banco == "si" or banco =="no":
        break
      else:
        print("\nError, Ingrese como opcion (si/no): \t")
    while validacion:
      try:
        compra_asiento= int(input("\nIngrese el asiento deseado: \t"))
        if compra_asiento > 0 and compra_asiento < 43:
          break
        else:
          print("Error, Ingrese un numero entre el 1 y el 42")
      except ValueError:
        print("Error, Ingrese numeros")
    fun.compra(compra_asiento)
  elif op == 3:
    if rut != None:
      #Ciclo para confirmar si el usuario es dueño del rut, sale del ciclo solo si es correcto
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para consultar los datos:\t"))                  
        #Solo sale del ciclo si cumple esta condicion y es un entero
        if validar_rut == str(rut):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut no coincide con nuestros registros")
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
    
  elif op == 4:
    if rut != None:
      #Ciclo para confirmar si el usuario es dueño del rut, sale del ciclo solo si es correcto
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para consultar los datos:\t"))                  
        #Solo sale del ciclo si cumple esta condicion y es un entero
        if validar_rut == str(rut):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut no coincide con nuestros registros")
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
  elif op == 5:
    print("\nSaliendo del programa...")
    break

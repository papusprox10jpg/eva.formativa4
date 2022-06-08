import funciones_avion as fun
import numpy as np
validacion = True
menu = True 
cont = 0
rut = None
normal = 0
vip = 0
total = 0
avion = np.char.array([["|", " 1", " 2", " 3", "     ", " 4", " 5", " 6", "|"], ["|", " 7", " 8", " 9", "     ", "10", "11", "12", "|"],
                       ["|", "13", "14", "15", "     ", "16", "17", "18", "|"], ["|", "19", "20", "21", "     ", "22", "23", "24", "|"],
                       ["|", "25", "26", "27", "     ", "28", "29", "30", "|"], ["|―", "――", "――", "―", "     ", "―", "――", "――", "―|"],
                       ["|_", "__", "__", "_", "     ", "_", "__", "__", "_|"], ["|", "31", "32", "33", "    ", "34", "35", "36", "|"],
                       ["|", "37", "38", "39", "     ", "40", "41", "42", "|"]])
while menu:
  print("\n¡Bienvenido a Vuelos-Duoc!")
  print("\n1. Ver asientos disponibles. \n2. Comprar asientos. \n3. Anular vuelo. \n4. Modificar datos de pasajero. \n5. Salir. \n ")
  while validacion:
    try:
      op = int(input("Ingrese la opción que desee: \t"))
      if op >=1 and op<=5:
        break
      else:
        print("\nError: Ingrese un numero entre el 1 y 5")
    except ValueError:
      print("\nError: Ingrese la opcion como un numero")
  if op == 1:
    fun.clear()
    fun.disp_asiento(avion)
    asientos_ocupados = fun.cant_ocupado(avion)
    fun.ir_menu()
  elif op == 2:
    fun.clear()
    nom = str(input("\nIngrese su nombre: \t"))
    while validacion:
      try:
        rut = int(input("\nIngrese su RUT: \t"))
        if rut >= 5000000 and rut <= 99999999:
          break
        else:
          print("\nError: RUT inválido, ingrese correctamente.")
      except ValueError:
        print("\nError, ingrese su rut sin puntos ni digito verificador.")
    telefono = fun.validar_telefono()
    while validacion: 
      banco = input("\nIngrese su banco: \t") #cambiar definicion de compra ya que se cambiaron las opciones
      banco.lower()
      if banco == "bancoduoc" or banco == "banco duoc" or banco == "duoc":
        print("\nFelicidades, se le aplicara un descuento del 15% en la compra total del pasaje")
        banco_duoc = True
        break
      else:
        banco_duoc = False
        break
    while validacion:
      try:
        compra_asiento= int(input("\nIngrese el asiento deseado: \t"))
        asiento = str(compra_asiento)
        check_avion = fun.valid_compra(asiento, avion)
        if compra_asiento > 0 and compra_asiento < 43 and check_avion == True:
          break
        elif check_avion == False:
          print("\nEl asiento ya ha sido comprado. Intente otro.")
        else:
          print("\nError: Ingrese un numero entre el 1 y el 42")
      except ValueError:
        print("\nError: Ingrese el asiento como un numero")
    fun.compra(compra_asiento, banco_duoc, avion, asiento, normal, vip,total)
    fun.ir_menu()
  elif op == 3:
    fun.clear()
    if rut != None:
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para cancelar su asiento o borrar sus datos:\t"))
        if validar_rut == str(rut):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut no coincide con nuestros registros")
      while menu:
        print("\n1. Eliminar datos. \n2. Eliminar Asiento. \n3. Salir" )
        while validacion:
          try:
            op3 = int(input("\nIngrese la opción que desee: \t"))
            if op3 == 1 or op3 == 2 or op3 == 3:
              break
            else:
              print("\nError: Ingrese un numero entre el 1 y 3")
          except ValueError:
            print("\nError: Ingrese la opcion como un numero")
        if op3 == 1:
          nom,rut,telefono,banco = fun.eliminar_datos(nom,rut,telefono,banco)
          print("\nDatos eliminados..")
        elif op3 == 2:
          asiento_nul = fun.anular_pasaje(avion)
        elif op3 == 3:
          break
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    fun.ir_menu()
  elif op == 4:
    fun.clear()   
    if rut != None:
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para modificar sus datos:\t"))
        validar_asiento = str(input("\nIngrese su asiento actualmente:\t"))
        if validar_rut == str(rut) and validar_asiento == str(compra_asiento):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut o asiento no coincide con nuestros registros")
      while menu:
        print("\n1. Modificar nombre. \n2. Modificar telefono. \n3. Ver datos \n4. Salir" )
        while validacion:
          try:
            op2 = int(input("\nIngrese la opción que desee: \t"))
            if op2 == 1 or op2 == 2 or op2 == 3 or op2 == 4:
              break
            else:
              print("\nError: Ingrese un numero entre el 1 y 4")
          except ValueError:
            print("\nError: Ingrese la opcion como un numero")
        dato_modificado = fun.modificar_datos(op2)
        if op2 == 1:
          nom = dato_modificado
        elif op2 == 2:
          telefono = dato_modificado
        elif op2 == 3:
          print("\nSus datos actuales son: \nNombre:",nom,"\nRut:",rut,"\nTelefono:",telefono,"\nbanco:",banco,"\nasiento:",compra_asiento)
        elif op2 == 4:
          break
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    fun.ir_menu()
  elif op == 5:
    fun.clear() 
    print("\nSaliendo del programa...")
    break

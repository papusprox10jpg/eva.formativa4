import funciones_avion as fun
validacion = True
menu = True 
cont = 0
rut = None
avion = [["|"," 1"," 2"," 3","     "," 4"," 5"," 6","|"],["|"," 7"," 8"," 9","     ","10","11","12","|"],
        ["|","13","14","15","    "," 16","17","18","|"],["|","19","20","21","     ","22","23","24","|"],
        ["|","25","26","27","    "," 28","29","30","|"],["|―","――","――","―","     ","―","――","――","―|"],
        ["|_","__","__","_","     ","_","__","__","_|"],["|","31","32","33","    "," 34","35","36","|"],
        ["|","37","38","39","    "," 40","41","42","|"]] #Gab/sugerencia: Muevo asiento a arriba para organizar las funciones.
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
    #telefono = validar_telefono() quitar # en el git
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
        if compra_asiento > 0 and compra_asiento < 43:
          break
        else:
          print("Error, Ingrese un numero entre el 1 y el 42")
      except ValueError:
        print("Error, Ingrese numeros")
    #fun.compra(compra_asiento) quitar # cuando se termine la funcion
  elif op == 3:
    if rut != None:
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para cancelar su asiento y borrar sus datos:\t"))
        if validar_rut == str(rut):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut no coincide con nuestros registros")
      #nombre,rut,telefono,banco = anular_pasaje(nombre,rut,telefono,banco) quitar # en git, falta ingresar el argumento pasaje para habilitar el asiento
      print("\nDatos eliminados y asiento otra vez valido")
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
    
  elif op == 4:
    
    if rut != None:    
      while validacion:
        validar_rut = str(input("\nBienvenid@ si esta registrad@ ingrese su RUT para modificar sus datos:\t"))
        validar_asiento = str(input("\nIngrese su asiento actualmente:\t"))
        if validar_rut == str(rut) and validar_asiento == str(compra_asiento):
          print("\nConfirmamos su identidad.")
          break
        else:
          print("\nError, lo sentimos su rut o asiento no coincide con nuestros registros")
      print("\n1. Modificar nombre. \n2. Modificar telefono. ")
      while validacion:
        try:
          op2 = int(input("\nIngrese la opción que desee2: \t"))
          if op2 == 1 or op2 == 2:
            break
          else:
            print("\nError: Ingrese un numero entre el 1 y 2")
        except ValueError:
          print("\nError: Ingrese la opcion como un numero")
      #dato_modificado = modificar_datos(opcion)
      print("\nEl dato fue modificado, volviendo al menu anterior..")

    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
  elif op == 5:
    print("\nSaliendo del programa...")
    break
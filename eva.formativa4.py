import funciones_avion as fun
validacion = True
menu = True 
cont = 0
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
        print("\nError: ingrese su RUT sin puntos ni digito verificador")   
    while validacion:
      try:
        telefono = int(input("\nIngrese su número de telefono: (comenzar con el numero 9)\t"))
        if len(str(telefono)) == 9:
          for i in str(telefono):
            if "9" in i:
              break
            else:
              cont += 1
          if cont >= 1:
            print("\nError: su número de teléfono debe iniciar con un 9.")
            cont = 0
          else:
            break
        else:
          print("\nError: su número de teléfono debe tener 9 digitos")
      except ValueError:
        print("\nError: ingrese número de teléfono como numeros")
    fun.ir_menu()
  elif op == 3:
    fun.clear()
    print("op3") #momentaneo!
    fun.ir_menu()
  elif op == 4:
    fun.clear()
    print("op4") #momentaneo!
    fun.ir_menu()
  elif op == 5:
    print("\nSaliendo del programa...")
    break

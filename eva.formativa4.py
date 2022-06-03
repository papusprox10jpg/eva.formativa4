def dispo (sala): #Recordar mover esta funcion a otro archivo!
  c=0
  for fila in sala:
    for asiento in fila :
      if asiento == "X":
        c+=1 
  return  c

validacion = True
menu = True 
cont = 0
while menu:
  print("\nVuelos-Duoc")
  print("\nBienvenido!")
  print("\n1. Ver asientos disponibles \n2. Comprar asientos \n3. Anular vuelo \n4. modificar datos de pasajero \n5. Salir \n ")
  while validacion:
    try:
      op = int(input("\nIngrese la opcion que desee: \t"))
      if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
        break
      else:
        print("\nError, Ingrese un numero entre el 1 y 5")
    except ValueError:
      print("\nError, Ingrese la opcion como un numero")
  if op == 1:
    print("\nAsientos del avión: ")
    avion = [["|"," 1"," 2"," 3","     "," 4"," 5"," 6","|"],["|"," 7"," 8"," 9","     ","10","11","12","|"],
              ["|","13","14","15","    "," 16","17","18","|"],["|","19","20","21","     ","22","23","24","|"],
              ["|","25","26","27","    "," 28","29","30","|"],["|―","――","――","―","     ","―","――","――","―|"],
              ["|_","__","__","_","     ","_","__","__","_|"],["|","31","32","33","    "," 34","35","36","|"],
              ["|","37","38","39","    "," 40","41","42","|"]]
    for i in range(9):
      for j in range(9):
          print(avion[i][j],end=" ")
      print()
    print("\nAsientos ocupados: ")
    print(dispo(avion))
    print("\n1. Asientos normales: del 1 al 30 \n2. Asientos VIP: del 31 al 42\n")

  elif op == 2:
    nom = str("\nIngrese su nombre: \t")
    while validacion:
      try:
        rut = int(input("\nIngrese su rut: \t"))
        if rut >= 5000000 and rut <= 99999999:
          break
        else:
          print("\nError, Rut no valido, ingrese correctamente ")
      except ValueError:
        print("\nError, ingrese su rut sin puntos ni digito verificador")   
    while validacion:
      try:
        telefono = int(input("\nIngrese su numero de telefono: (comenzar con el numero 9)\t"))
        if len(str(telefono)) == 9:
          for i in str(telefono):
            if "9" in i:
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

  elif op == 3:
    print("op3") #momentaneo!
  elif op == 4:
    print("op4") #momentaneo!
  elif op == 5:
    print("\nSaliendo del programa...")
    break

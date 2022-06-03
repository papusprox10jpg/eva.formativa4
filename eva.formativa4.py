def dispo (sala):
  c=0
  for fila in sala:
    for asiento in fila :
      if asiento == "O":
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
      op = int(input("ingrese una opcion valida: (1/2/3/4/5)\t"))
      if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
        break
      else:
        print("ingrese un numero entre el 1 y 5")
    except ValueError:
      print("ingrese numeros!")
  if op == 1:
    print("\n1. Asientos normales \n2. Asientos VIP\n")
    matriz = [["|"," 1"," 2"," 3","     "," 4"," 5"," 6","|"],["|"," 7"," 8"," 9","     ","10","11","12","|"],
              ["|","13","14","15","    "," 16","17","18","|"],["|","19","20","21","     ","22","23","24","|"],
              ["|","25","26","27","    "," 28","29","30","|"],["|","31","32","33","     ","34","35","36","|"]]
    for n in range(6):
      for i in range(9):
          print(matriz[n][i],end=" ")
      print()
    print("\nasientos ocupados: ")
    print(dispo(matriz))

  if op == 2:
    nom = str("\ningrese su nombre: \t")
    while validacion:
      try:
        rut = int(input("\ningrese su rut: \t"))
        if rut >= 5000000 and rut <= 99999999:
          break
        else:
          print("numero de rut erroneo")
      except ValueError:
        print("ingrese numeros")
    while validacion:
      try:
        telefono = (input("\ningrese su numero de telefono: (comenzar con el numero 9)\t"))
        if len(telefono) == 9:
          break
        else :
          print("ingrese un numero con 9 digitos")
      except ValueError:
        print("ingrese un numero ")
        
      for i in telefono:
        if "9" in i:
          break
        else:
          cont += 1
      if cont >= 1:
        print("\n Error, Su celular debe tener un 9 al principio")
        cont = 0

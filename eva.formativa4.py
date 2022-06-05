def compra(compra_asiento):
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
import funciones_avion as fun
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
    matriz = [["|"," 1"," 2"," 3","     "," 4"," 5"," 6","|"],["|"," 7"," 8"," 9","     ","10","11","12","|"],
              ["|","13","14","15","    "," 16","17","18","|"],["|","19","20","21","     ","22","23","24","|"],
              ["|","25","26","27","    "," 28","29","30","|"],["|―","――","――","―","     ","―","――","――","―|"],
              ["|_","__","__","_","     ","_","__","__","_|"],["|","31","32","33","    "," 34","35","36","|"],
              ["|","37","38","39","    "," 40","41","42","|"]]
    for i in range(9):
      for j in range(9):
          print(matriz[i][j],end=" ")
      print()
    print("\nAsientos ocupados: ")
    print(disp_asiento(avion))
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
    compra(compra_asiento)
  elif op == 3:
    if rut != None:
      print("op3") #momentaneo , programmar aqui!
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
    
  elif op == 4:
    if rut != None:
      print("op4") #momentaneo , programar aqui!
    else:
      print("\nError, ingrese a la opcion 2 para registrarse...")
    print("\nVolviendo al menu principal...")
  elif op == 5:
    print("\nSaliendo del programa...")
    break

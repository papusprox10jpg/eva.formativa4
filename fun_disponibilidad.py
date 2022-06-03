def disp_asiento (mapa_avion):#agrego nombre más claro.
  cant_disp=0
  for fila in mapa_avion: #indexación de cada fila de la matriz
    for asiento in fila : #indexación en cada valor de cada fila
      if asiento == "X": #si algun valor es X, retorna disponibildiad
        cant_disp+=1
  return  cant_disp
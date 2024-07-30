def principal():

    def conversegundos():
            horas = float(input("Ingresa el numero de horas: "))
            minutos = float(input("Ingresa el numero de minutos: "))
            segundos = float(input("Ingresa el numero de segundos: "))
            resulsegundos = int((horas*3600)+(minutos*60)+segundos)
            print(resulsegundos)
  

    def converhorminseg():
            segundos = float(input("Ingresa el numero de segundos: "))
            hor = int(segundos/3600)
            min = int(abs(segundos-3600)/60)
            seg = int(abs(segundos-3600)-(min*60))
            print(str(hor) + "hh " + str(min) + "mm " + str(seg) + "ss")
  
    opcionescogida = input("Selecciona una de las siguientes opciones: \n" 
                           "1- Convierte a Segundos a partir de horas, minutos y segundos \n"
                           "2- Convierte a horas, minutos y segundos a partir de los segundos \n"
                           "3- Salir del Programa \n")
    
    if opcionescogida == "1":
           conversegundos()
    elif opcionescogida == "2":
           converhorminseg()
    elif opcionescogida == "3":
          print("Adios del programa")
    else:
        print("Escribe una opcion correcta")

principal()
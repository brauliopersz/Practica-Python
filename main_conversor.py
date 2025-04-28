
#Se importan los paquetes, modulos y funciones a utilizar
from conversor_temperatura.celsius import celcius_to_farenheit, celcius_to_kelvin
from conversor_temperatura.fahrenheit import fahrenheit_to_celsius, fahrenheit_to_kelvin
from conversor_temperatura.kelvin import kelvin_to_celsius, kelvin_to_fahrenheit
from conversor_longitud.kilometros import kilometro_to_metro, kilometro_to_milla, kilometro_to_pie
from conversor_longitud.metros import metro_to_kilometro, metro_to_milla, metro_to_pie
from conversor_longitud.millas import milla_to_kilometro, milla_to_metro, milla_to_pie
from conversor_longitud.pies import pie_to_kilometro, pie_to_metro, pie_to_milla


#Se declaran las variables a utilizar
temperatura = 0
longitud = 0
op = 0

#Se utiliza un bucle tipo while para mantener flujo constante del programa
while True:
      #Se imprime por pantalla las opciones que el usuario puede seleccionar
      print("""
            
            Seleccione una opción
            
            1. Conversor Longitud
            2. Conversor Temperatura
            3. Salir
            
            \n""")
      #Se solicita al usuario escoger una de las opciones
      op = int(input("Inserte la opción que desea: "))
      print("")

      #Si el usuario escoge la opción 1, se selecciona el Conversor de Longitud
      if op == 1:
            print("Seleccionó el Conversor Longitud! \n")
            print("""
                  1.Kilometro
                  2.Metro
                  3.Milla
                  4.Pie
                  \n""")
            #Se solicita al usuario indicar la longitud que desea convertir
            op = int(input("Qué tipo de longitud está intentando convertir? : "))
            print("")
            #Si escoge la opción 1, estará conviertiendo de Kilometro a las diferentes opciones presentadas aquí debajo
            if op == 1:
                  print("""
                        
                        1.Kilometro a Metro
                        2.Kilometro a Milla
                        3.Kilometro a Pie
                        
                        """)
                  #Se solicita al usuario indicar al programa, la longitud a la que desea convertir la opción escogida
                  op = int(input("Inserta una opción: "))
                  print("")
                  if op == 1:
                        #Si el usuario escoge la opción 1, se estará haciendo la conversión de Kilometro a Metro
                        print("Kilometro a Metro")
                        print("")
                        #Se realiza la conversión del input a float ya que por defecto input() retorna string 
                        longitud = float(input("Inserte la longitud en Kilometros: "))
                        #Se imprime cadena de texto y se pasa argumento a función kilometro_to_metro(longitud)
                        print (f"El resultado de convertir {longitud} Kilometros a Metros es igual a {kilometro_to_metro(longitud)} Metros")
                        
                  elif op == 2:
                        print("Kilometro a Milla")
                        print("")
                        longitud = float(input("Inserte la longitud en Kilometros: "))
                        print(f"El resultado de convertir {longitud} Kilometros a Millas es igual a {kilometro_to_milla(longitud)} Millas")
                        
                  elif op == 3:
                        print("Kilometro a Pie")
                        print("")
                        longitud = float(input("Inserte la longitud en Kilometros: "))
                        print(f"El resultado de convertir {longitud} Kilometros a Pies es igual a {kilometro_to_pie(longitud)} Pies")
                        
            elif op == 2:
                  print("""
                        1.Metro a Kilometro
                        2.Metro a Milla
                        3.Metro a Pie
                        \n""")
                  op = int(input("Inserta una opción: "))
                  print("")
                  if op == 1:
                        print("Metro a Kilometro\n")
                        longitud = float(input("Inserte la longitud en Metros: "))
                        print(f"El resultado de convertir {longitud} a Kilometros es igual a: {metro_to_kilometro(longitud)} Kilometros")
                  elif op == 2:
                        print("Metro a Milla\n")
                        longitud = float(input("Inserte la longitud en Metros: "))
                        print(f"El resultado de convertir {longitud} en Millas es igual a: {metro_to_milla(longitud)} Millas")
                  elif op == 3:
                        print("Metro a Pie\n")
                        longitud = float(input("Inserte la longitud en Metros: "))
                        print(f"El resultado de convertir {longitud} Metros a Pies es igual a: {metro_to_pie(longitud)} Pies")
                        
                        
            elif op == 3:
                  print("""
                        1.Milla a Kilometro
                        2.Milla a Metro
                        3.Milla a Pie
                        \n""")
                  op = int(input("Inserta una opción: "))
                  print("")
                  if op == 1:
                        print("Milla a Kilometro\n")
                        op == float(input("Inserte la longitud en Millas:"))
                        print(f"El resultado de convertir {longitud} Millas a Kilometros es igual a: {milla_to_kilometro(longitud)} Kilometros")
                        
                  elif op == 2:
                        print("Milla a Metro\n")
                        op == float(input("Inserte la longitud en Millas:"))
                        print(f"El resultado de convertir {longitud} Millas en Metros es igual a : {milla_to_metro(longitud)} Metros")
                        
                  elif op == 3:
                        print("Milla a Pie\n")
                        op == float(input("Inserte la longitud en Millas:"))
                        print(f"El resultado de convertir {longitud} Millas a Pies es igual a: {milla_to_pie(longitud)} Pies")
                  
            elif op == 4:
                  print("""
                        1.Pie a Kilometro
                        2.Pie a Metro
                        3.Pie a Milla
                        \n""")
                  op = int(input("Inserta una opción: "))
                  print("")
                  if op == 1:
                        print("Pie a Kilometro")
                        op = float(input("Inserte la longitud en Pies:"))
                        print(f"El resultado de convertir {longitud} Pies en Kilometros es igual a: {pie_to_kilometro(longitud)} Kilometros")
                  elif op == 2:
                        print("Pie a Metro")
                        op = float(input("Inserte la longitud en Pies:"))
                        print(f"El resultado de convertir {longitud} Pies a Metros es igual a: {pie_to_metro(longitud)} Metros")
                  elif op == 3:
                        print("Pie a Milla")
                        op = float(input("Inserte la longitud en Pies:"))
                        print(f"El resultado de convertir {longitud} Pies en Millas es igual a: {pie_to_milla(longitud)} Millas")
            else:
                  print("Inserte una opción válida!")
            
            
      #Si el usuario escoge la opción 2, se selecciona el Conversor de Temperatura
      elif op == 2:
            print("Seleccionó el Conversor Temperatura! \n")
            #Se imprime el tipo de temperaturas existentes 
            print("""
                  
                  1.Celcius (°C)
                  2.Farenheit (°F)
                  3.Kelvin (K)
                  
                  
                  \n""")
            #Se solicita al usuario que indique el tipo temperatura que está intentando convertir
            op = int(input("Qué tipo de temperatura está intentando convertir? : "))
            print("")
            
            #Si el usuario escoge la opción 1, le dará las diferentes opciones en las que puede hacer la conversión
            if op == 1:
                  print("""
                        
                        Deseas convertir de:
                        
                        1.Celcius a Fahrenheit
                        2.Celcius a Kelvin
                        
                        \n""")
                  #Se le solicita al usuario escoger una de las opciones
                  op = int(input("Inserta una opción: "))
                  print("")
                  #Si selecciona la opción 1, se realiza la conversión de Celcius a Fahrenheit
                  if op == 1:
                        print("Celcius a Fahrenheit")
                        print("")
                        #Lógica de conversión
                        #Se solicita al usuario insertar la temperatura a convertir
                        #Se realiza la conversión del input a float ya que por defecto input() retorna string 
                        temperatura = float(input("Inserte la Temperatura en °C: "))
                        print("")
                        #Se imprime cadena de texto y se le pasa argumento a la función celcius_to_farenheit(temperatura)
                        print(f"El resultado de convertir {temperatura} Celcius °C a Fahrenheit es igual a {celcius_to_farenheit(temperatura)} °F")
                  
                  elif op == 2:
                        print("Celcius Kelvin")
                        print("")
                        temperatura = float(input("Inserte la Temperatura en °C: "))
                        print("")
                        print(f"El resultado de convertir {temperatura} Celcius °C a Kelvin es igual a {celcius_to_kelvin(temperatura)} (K)")
                        
                  
                  else:
                        print("Inserte una opción válida!")
                  
            elif op == 2:
                  print("""
                        
                        Deseas convertir de:
                        
                        1.Fahrenheit a Celcius
                        2.Fahrenheit a Kelvin
                        
                        \n""")
                  
                  op = int(input("Inserta una opción: "))
                  print("")
                  
                  if op == 1:
                        print("Fahrenheit a Celcius")
                        print("")
                        temperatura = float(input("Inserte la temperatura en °F: "))
                        print("")
                        print(f"El resultado de convertir {temperatura} Fahrenheit °F a Celcius es igual a {fahrenheit_to_celsius(temperatura)} °C ")
                        
                        
                  elif op == 2:
                        print("Fahrenheit a Kelvin")
                        print("")
                        temperatura = float(input("Inserte la temperatura en °F: "))
                        print("")
                        print(f"El resultado de convertir {temperatura} Fahrenheit °F a Kelvin es igual a {fahrenheit_to_kelvin(temperatura)} (K) ")
                        
                  
                  else:
                        print("Inserte una opción válida!")
                        
            elif op == 3:
                  print("""
                        
                        Deseas convertir de:
                        
                        1.Kelvin a Celcius
                        2.Kelvin a Fahrenheit
                        
                        \n""")
                  
                  op = int(input("Inserta una opción: "))
                  print("")
                  
                  if op == 1:
                        print("Kelvin a Celcius")
                        print("")
                        temperatura = float(input("Inserte la temperatura en (K): "))
                        print("")
                        print(f"El resultado de convertir {temperatura} Kelvin (K) a Celcius es igual a {kelvin_to_celsius(temperatura)} °C ")
                        
                        
                  elif op == 2:
                        print("Kelvin a Fahrenheit")
                        print("")
                        temperatura = float(input("Inserte la temperatura en (K): "))
                        print("")
                        print(f"El resultado de convertir {temperatura} Kelvin (K) a Fahrenheit es igual a {kelvin_to_fahrenheit(temperatura)} °F ")
                        
                  
                  else:
                        print("Inserte una opción válida!")
                  
                  
            
            else: 
                  print("Inserte una opción válida!")
                  
      elif op == 3:
            print("""
                  
                  Gracias por utilizar el programa 
                  Hasta Luego!
                  
                  """)
            break
            
                  
      else:
            print("Inserte una opción válida!")
            continue
            


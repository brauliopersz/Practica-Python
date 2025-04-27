
from conversor_temperatura.celsius import celcius_to_farenheit, celcius_to_kelvin
from conversor_temperatura.fahrenheit import fahrenheit_to_celsius, fahrenheit_to_kelvin
from conversor_temperatura.kelvin import kelvin_to_celsius, kelvin_to_fahrenheit
 
#Se declaran las variables a utilizar
temperatura = 0
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
            pass
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
                        print("Inserte una opción válida")
                        
                  
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
                        print("Inserte una opción válida")
                        
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
                        print("Inserte una opción válida")
                  
                  
            
            else: 
                  print("Inserte una opción válida")
                  
      elif op == 3:
            break
            
                  
      else:
            print("Inserte una opción válida")
            continue
            


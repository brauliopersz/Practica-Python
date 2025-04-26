
from conversor_temperatura.celsius import celcius_to_farenheit, celcius_to_kelvin
from conversor_temperatura.fahrenheit import fahrenheit_to_celsius, fahrenheit_to_kelvin
from conversor_temperatura.kelvin import kelvin_to_celsius, kelvin_to_fahrenheit

temperatura = 0

print("""
      
      Seleccione el conversor que desea utilizar
      
      1. Conversor Longitud
      2. Conversor Temperatura
      
      \n""")

op = int(input("Inserte la opción que desea: "))

if op == 2:
      print("Seleccionó el Conversor Temperatura \n")
      
      print("""
            
            1.Celcius
            2.Farenheit
            3.Kelvin
            
            
            \n""")
      
      op = int(input("Qué tipo de temperatura está intentando convertir? : "))
      
      if op == 1:
            op = int(input("""
                  
                  Deseas convertir de:
                  
                  1.Celcius a Fahrenheit
                  2.Celcius Kelvin
                  
                  \n"""))
            
            if op == 1:
                  temperatura = float(input("Inserte la Temperatura: "))
                  print(f"El resultado de convertir {temperatura} Celcius a Fahrenheit es igual a {celcius_to_farenheit(temperatura)}")
      
      


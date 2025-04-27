def celcius_to_farenheit(temperatura):
    
    """
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Celcius a Fahrenheit de dicha temperatura

    Fórmula: temperatura * 1.8 + 32
    
    Returns:
    El (resultado) de la conversión de celsius a fahrenheit 
    """
    resultado = 0
    resultado = (temperatura * 1.8) + 32
    return resultado

def celcius_to_kelvin(temperatura):
    
    """
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Celcius a Kelvin de dicha temperatura
    
    Fórmula: temperatura + 273.15

    Returns:
       El (resultado) de la conversión de celsius a kelvin
    """
    resultado = 0
    resultado = temperatura + 273.15
    return resultado

    
def fahrenheit_to_celsius(temperatura):
    
    """
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Fahrenheit a Celcius de dicha temperatura

    Fórmula: (temperatura - 32) / 1.8
    
    Returns:
    El (resultado) de la conversión de fahrenheit a celsius 
    """
    
    resultado = 0
    resultado = (temperatura - 32) / 1.8
    return resultado

def fahrenheit_to_kelvin(temperatura):
    
    """
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Fahrenheit a Kelvin de dicha temperatura

    Fórmula: (temperatura + 459.67) / 1.8
    
    Returns:
    El (resultado) de la conversión de fahrenheit a kelvin
    """
    
    resultado = 0
    resultado = (temperatura + 459.67) / 1.8
    return resultado
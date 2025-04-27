def kelvin_to_celsius(temperatura):
    
    """
    _summary_:
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Kelvin a Celsius de dicha temperatura

    Fórmula: temperatura - 273.15
    
    Returns:
    El (resultado) de la conversión de kelvin a celsius
    """
    
    resultado = 0
    resultado = temperatura - 273.15
    return resultado

def kelvin_to_fahrenheit(temperatura):
    
    """
    _summary_:
    Función que recibe un parámetro (temperatura) y realiza la conversión de 
    Kelvin a Fahrenheit de dicha temperatura

    Fórmula: (temperatura - 273.15) * 9/5 + 32
    
    Returns:
    El (resultado) de la conversión de kelvin a fahrenheit 
    """
    
    resultado = 0
    resultado = (temperatura - 273.15) * 9/5 + 32
    return resultado
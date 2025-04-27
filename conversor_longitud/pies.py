def pie_to_kilometro(longitud):
    
    """
    Función que toma como parámetro una longitud (pies) y la convierte 
    en kilometros
    
    Función: longitud / 3280.83989501  

    Returns:
        El resultado de convertir (longitud) en kilometros
    """
    
    resultado = 0
    resultado = longitud / 3280.83989501
    return resultado
    

def pie_to_metro(longitud):
    
    """
    Función que toma como parámetro una longitud (pies) y la convierte 
    en metros
    
    Función: longitud / 3.28084

    Returns:
        El resultado de convertir (longitud) en metros
    """
    
    resultado = 0
    resultado = longitud / 3.28084
    return resultado

def pie_to_milla(longitud):
    
    """
    Función que toma como parámetro una longitud (pies) y la convierte 
    en millas
    
    Función: longitud / 5280

    Returns:
        El resultado de convertir (longitud) en millas
    """
    
    resultado = 0
    resultado = longitud / 5280
    return resultado
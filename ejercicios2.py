def clasificar_numero_simple():
    """ 
    solicita un numero y determina si es positivo, negativo o cero. 
    Incluye manejo de errores.
        """
    
    try: 
        numero = float(input("Ingrese un número: "))

        if numero > 0:
            resultado = "POSITIVO"
        elif numero < 0:
            resultado = "NEGATIVO"
        else:
            resultado = "CERO"
        print(f"El numero {numero} es {resultado}. ")

    except ValueError:
        print("Error: Por favor ingrese un número válido.")
    
    if __name__ == "__main__":
        clasificar_numero_simple()

    
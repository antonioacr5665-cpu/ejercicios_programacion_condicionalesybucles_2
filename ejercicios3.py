def verificar_par_impar():
    try:

        numero = int(input("Ingrese un número entero: "))
       
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es iMPAR.")


    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")  

if __name__ == "__main__":
    verificar_par_impar()
    
def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass

    contrasena=input("Ingrese contraseña:")

    tiene_largo_ok = len(contrasena) >= 8       #booleanos
    tiene_numero = False                        #booleanos

    for caracter in contrasena:
        if caracter in "0123456789":
            tiene_numero=True

    if tiene_largo_ok and tiene_numero:
        print("Contraseña valida")

    if not tiene_largo_ok:
        print("Contraseña muy corta")

    if not tiene_numero:
        print("Debe contener un numero")


password()

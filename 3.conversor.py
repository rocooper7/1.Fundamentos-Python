def convertir(tipo_moneda, dolares):
    pesos = float(input('¿Cuántos Pesos' + tipo_moneda + ' desea cambiar? '))
    return round(pesos / dolares, 2)


if __name__ == '__main__':

    opcion = int(input(""" 
    Bienvenido al conversor de monedas. 🤔
    1. Pesos colombianos
    2. Pesos argentinos
    3. Pesos mexicanos
    Elija una opción: """))

    # Coloque los precios a valores recientes
    if opcion == 1:
        print('Su cantidad de dolares es: $' + str(convertir('colombianos', 3715.50)))
    elif opcion == 2:
        print('Su cantidad de dolares es: $' + str(convertir("argentinos", 70.50)))
    elif opcion == 3:
        print('Su cantidad de dolares es: $' + str(convertir('mexicanos', 22.66)))
    else:
        print('Ingrese una opción válida, por favor.')
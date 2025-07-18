productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2],
          'UWU131HD': [349990,1], 
          'FS1230HD': [249990,0]}

def stock_marca():
    marca = input("Ingrese marca: ").strip().lower()
    stock_diccionario= 0
    for clave in productos:
        dato = productos[clave]
        if dato[0].strip().lower() == marca.strip().lower():
            stock_diccionario+= stock[clave][1]
            print(f"El codigo: {clave}")
            print(f"Marca: {marca}")
            print(f"Cantidad disponible: {stock_diccionario}")
            print("*********************")

    
def busquedad_por_precio():
    while True:
        try:
            precio_min = int(input("Ingrese precio minimo: "))
            precio_max = int(input("Ingrese precio maximo: "))
            break
        except ValueError:
            print("Debe ingresar numeros enteros.")
    lista_precio = []
    for clave in stock:
        precio = stock[clave][0]
        stock_dispo = stock[clave][1]
        if precio_min <= precio <= precio_max and stock_dispo> 0:
            marca = productos[clave][0]
            lista_precio.append(f"{marca}--{clave}")
    if len(lista_precio) == 0:
        print("No hay notebooks en ese rango de precio.")
    else:
        lista_precio.sort()
        print("Notebook dentro del rango: ")
        for usuario in lista_precio:
            print(usuario)

def actualizar_precio():
    while True:
        clave = input("Ingrese la clave del modelo que desea actualizar: ")
        if clave in stock:
            while True:
                try:
                    nuevo_precio =int(input("Ingrese nuevo precio: "))
                    break
                except ValueError:
                    print("Debe ingresar numeros enteros.")
            stock[clave][0] = nuevo_precio
            print("Precio actualizado!!")
        else:
            print("El modelo no existe!!")
        actualizar = input("¿Desea actualizar otro precio? (si/no)").strip().lower()
        if actualizar != "si":
            print("Dirigiendote al menu principal......")
            break

def mostra_notebooks():
    if not productos:
        print("No hay notebooks.")
    else:
        print("Noteboks registrados: ")
        for claves in productos:
            datos = productos[claves]
            precio = stock[claves][0]
            stock_dispo = stock[claves][1]
            print(f"Clave del modelo: {claves}")
            print(f"Marca: {datos[0]}")
            print(f"Pantalla: {datos[1]}")
            print(f"RAM: {datos[2]}")
            print(f"Disco: {datos[3]}")
            print(f"GB de DD: {datos[4]}")
            print(f"Procesador: {datos[5]}")
            print(f"Video: {datos[6]}")
            print(f"Precio: {precio}")
            print(f"Stock: {stock_dispo}")
            print("-----------------------------------------------")

def menu():
    while True:
        try:
            print("     -->>>     BIENVENIDO A PYBOOKS   <<<--       ")
            print("          *** MENU PRINCIPAL***     ")
            print("         1) Stock marca.    ")
            print("        2) Busqueda de precio.   ")
            print("      3) Actualizar precio.   ")
            print("    4) Mostrar Notebooks.    ")
            print("  5) Salir.")
            
            opc = int(input("Ingrese una opcion: "))
            if opc == 1:
                stock_marca()
            elif opc == 2:
                busquedad_por_precio()
            elif opc == 3:
                actualizar_precio()
            elif opc == 4:
                mostra_notebooks()
            elif opc == 5:
                print("Programa finalizado...........")
                break
            else:
                print("Debe seleccionar una opcion valida.")

        except ValueError:
            print("ERROR. Debe ingresar una opcion valida.")
menu()


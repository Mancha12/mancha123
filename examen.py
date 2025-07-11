#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10],
        '2175HD': [327990,4], 
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0], 
}

def stock_marca(marca):
        for datos in productos.values():
            marca = datos[0]
            if datos == marca:
                print(F"El sctock es:",datos[0])
        else:
            print("No tiene stock.")
            
def busqueda_precio(p_min,p_max):
        for modelo, datos in stock.items():
            precio = datos[0]
            if p_min <= precio <= p_max:
                print(f"Modelo: {modelo}, Precio: {precio}, Stock: {datos[1]}")
        else:
            print("No hay notebooks en ese rango de precios.")


def eliminar_producto(modelo):
    if modelo in stock:
        del stock[modelo]
        print(f"Producto {modelo} eliminado correctamente.")
    else:
        print(f"El producto {modelo} no existe en el stock.")


def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        
        opcion = int(input("Ingresar opcion(1 al 4): "))

        if opcion == 1:
            marca = input("Ingresar marca a consultar: ").lower()
            stock_marca(marca)
        try:
            if opcion == 2:
                p_min = int(input("Buscar porprecio minimo:"))
                p_max = int(input("Ingrese precio maximo:"))
                busqueda_precio(p_min,p_max)
        except ValueError:
            print("Debe ingresar valores enteros. ")

        if opcion == 3:
            eliminar = input("Eliminar producto: ")
            eliminar_producto(eliminar)

        elif opcion == 4:
            print("Ingrese modelo a actualizar. ")

        else:
            print("Debe seleccionar una opcion valida!!")

main()

#https://github.com/Mancha12/examen.git
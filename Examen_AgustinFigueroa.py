#Agustin Figueroa 005D
def menu_principal():
    print("\n ***MENU PRINCIPAL***")
    print("1.- Stock marca")
    print("2.- Busqueda por RAM y precio")
    print("3.- Eliminar producto")
    print("4.- Salir")
    print(" ********************")
stocks = [31, 43, 3, 1]
pc = ["['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050']", "['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050']", "['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti']", "['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada']", "['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050']", "['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada']", "['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050']", "['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']"]
modelos = ["8475HD", "2175HD", "JjfFHD", "fgdxFHD", "GF75HD", "123FHD", "342FHD", "UWU131HD"]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
          }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }


while True:
    menu_principal()
    try:
        opcion1 = input("Por favor seleccione una opcion: ")
        if opcion1 == "1":
            while True:
                marca = input("Por favor elija una marca (HP, Acer, Asus, Dell): ").upper()
                if marca == "HP":
                    print(f"El Stock es: {stocks[0]}")
                    break
                elif marca == "ACER":
                    print(f"El Stock es: {stocks[1]}")
                    break
                elif marca == "ASUS":
                    print(f"El Stock es: {stocks[2]}")
                    break
                elif marca == "DELL":
                    print(f"El Stock es: {stocks[3]} ")
                    break
                else:
                    print("Selecciona una opcion valida!")
                    continue
        elif opcion1 == "2":
            while True:
                ram_min = int(input("Ingrese RAM minima: "))
                ram_max = int(input("Ingrese RAM maxima: "))
                precio = int(input("Ingrese precio: "))
                if ram_min >= 4 and ram_max == 6 and precio > 290000:
                    print(f"\n {pc[1]} {pc[5]}")
                    break
                elif ram_min >= 8 and ram_max < 16 and precio > 290000:
                    print(f"\n {pc[0]} {pc[3]} {pc[4]} {pc[6]} {pc[7]}")
                    break
                elif ram_min == 4 and ram_max == 4 and precio > 290000:
                    print(f"\n {pc[1]}")
                    break
                elif ram_min >= 4 and ram_max <= 8 and precio > 290000:
                    print(f"\n {pc[0]} {pc[1]} {pc[3]} {pc[4]} {pc[5]} {pc[6]} {pc[7]}")
                    break
                elif ram_min >= 4 and ram_max >= 16 and precio > 290000:
                    print(f"\n {pc[0]} {pc[1]} {pc[2]} {pc[3]} {pc[4]} {pc[5]} {pc[6]} {pc[7]}")
                    break
                else:
                    print("No hay notebooks que mostrar")
                    continue
        elif opcion1 == "3":
            while True:
                modelo = input(f"Ingrese un modelo a eliminar {modelos}: ")
                if modelo not in modelos:
                    print("Ese modelo no existe")
                    break
                else:
                    print("Producto Eliminado!")
                    modelos.remove(modelo)
                    borrado = input("Desea eliminar otro modelo? (S/N): ").upper()
                    if borrado == "S":
                        continue
                    elif borrado == "N":
                        break
                    
                    
        elif opcion1 == "4":
            print("Fin del Programa.")
            break
        else:
            print("Debe ingresar una opcion valida!")
    except ValueError:
        ()
    
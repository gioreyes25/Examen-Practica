datos = {
    "L001": ["El Principito", 1980, "Ficcion", 15],
    "L002": ["Cien Años de Soledad", 1967, "Realismo Magico", 10],
    "L003": ["1984", 1949, "Distopía", 8],
    "L004": ["Don Quijote de la Mancha", 1905, "Clasico", 12],
    "L005": ["Harry Potter y la piedra filosofal", 1997, "Fantasia", 9],
    "L006": ["Los Juegos del Hambre", 2008, "Ciencia Ficcion", 11],
    "L007": ["La Sombra del Viento", 2001, "Misterio", 0],
    "L008": ["Orgullo y Prejuicio", 1913, "Romance", 13],
    "L009": ["El Hobbit", 1937, "Fantasia", 10],
    "L010": ["Fahrenheit 451", 1953, "Distopia", 14]
}
inventario = {
    "L001": [15, "Ficcion"],
    "L002": [10, "Realismo Magico"],
    "L003": [8, "Distopia"],
    "L004": [12, "Romance"],
    "L005": [9, "Fantasia"],
    "L006": [11, "Ficcion"],
    "L007": [0, "Misterio"],
    "L008": [13, "Romance"],
    "L009": [10, "Fantasia"],
    "L010": [14, "Distopia"]
}
while True:
    print("\n1. Ver Stock de libros por genero")
    print("2. Buscar Libros Por Años")
    print("3. Actualizar Stock")
    print("4. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            gene=input("Ingrese genero de a buscar: ").title()
            dispo=[valor[1] for valor in inventario.values()]
            if gene in dispo:
                total=0
                for n,valor in inventario.items():
                    if gene==valor[1]:
                        total+=valor[0]
                print(f"El stock de genero de libros {gene} es {total}")
            else:
                print("Genero ingresado no existe")
        case 2:
            num1=int(input("Ingrese rango de años min"))
            num2=int(input("Ingrese rango de años max"))
            ordenados=sorted(datos.items(),key=lambda x:x[1][0])
            resultados=[]
            for id,valor in ordenados:
                libro,año,genero,cantidad = valor
                if num1 <= int(año) <= num2 and cantidad !=0:
                    resultados.append(f"{id}--{libro}--{genero}")
                else:
                    print
            if resultados:
                for k in resultados:
                    print(k)
            else:
                print("No se encuentran libros entre rango de años ingresado")
        case 3:
            id=input("Ingrese ID Para actualizar stock: ").upper()
            if id in datos:
                for n,i in inventario.items():
                    if id==n:
                        print(f"{n}--{i[0]}--{i[1]}")
                        cantidad=int(input("Ingrese cantidad de unidades: "))
                        inventario[id][0]+=cantidad
                        print(f"Se agregaron {cantidad}u a el ID {n}")
            else:
                print("ID Ingresado no existe")
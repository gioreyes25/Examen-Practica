datos = {
    "P001": ["Pan", 800, 30, "Alimentos"],
    "P002": ["Leche", 1200, 20, "Bebidas"],
    "P003": ["Jabon", 1500, 15, "Aseo"],
    "P004": ["Arroz", 1000, 25, "Alimentos"],
    "P005": ["Gaseosa", 1800, 18, "Bebidas"],
    "P006": ["Detergente", 2500, 10, "Aseo"],
    "P007": ["Fideos", 900, 40, "Alimentos"],
    "P008": ["Agua", 700, 35, "Bebidas"],
    "P009": ["Shampoo", 2200, 12, "Aseo"],
    "P010": ["Cafe", 2000, 22, "Bebidas"]
}
while True:
    print("\n1. Ver Stock Por Categoria")
    print("2. Ver Productos")
    print("3. Buscar Producto Por Nombre")
    print("4. Actualizar Stock")
    print("5. Ver Gasto Total De Inventario")
    print("6. Top 3 Productos Mas Caros")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cate=input("Ingrese Categoria: ")
            dispo=[valor[3] for valor in datos.values()]
            if cate in dispo:
                total=0
                for n,i in datos.items():
                    if cate==i[3]:
                        total+=i[2]
                print(f"El total de productos de {cate} es: {total}")
            else:
                print("No hay coincidencias")
        case 2:
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            for n,i in ordenados:
                print(f"{n} {i[0]} Precio: {i[1]}| Categoria: {i[3]}")
        case 3:
            name=input("Ingrese producto que desea buscar: ")
            dispo=[valor[3] for valor in datos.values()]
            if name in dispo:
                for n,i in datos.items():
                    if name==i[0]:
                        print(f"{n} {i[0]} Precio: {i[1]}| Categoria: {i[3]}")
            else:
                print("No hay coincidencias")
        case 4:
            id=input("Ingrese ID de producto que desea actualizar: ")
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        cantidad=int(input("Ingrese cantidad de stock que agregara: "))
                        datos[id][2]+=cantidad
            else:
                print("ID no existe")
        case 5:
            total=0
            for n,i in datos.items():
                total+=i[1]
            print(f"El gasto total de inventario es: {total}")
        case 6:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][1])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {v[0]} Precio: ${v[1]}")
datos= {
    "PROD001": ["Laptop Gamer X-Pro","Electronica", 1200],
    "PROD002": ["Auriculares Bluetooth","Electronica", 75],
    "PROD003": ["Libro 'El Último Dragón'","Libros", 25],
    "PROD004": ["Cafetera Espresso Deluxe","Hogar", 150],
    "PROD005": ["Mouse Ergonómico Inalámbrico","Electronica",40],
    "PROD006": ["Set de Sartenes Antiadherentes","Hogar", 80],
    "PROD007": ["Cargador Portátil 20000mAh","Electronica", 35]
}

inventario = {
    "PROD001": [5, True],
    "PROD002": [50, True],
    "PROD003": [15, True],
    "PROD004": [3, False], # Temporalmente fuera de stock
    "PROD005": [20, True],
    "PROD006": [8, True],
    "PROD007": [0, False] # Agotado
}
while True:
    print("1. Ver Productos Disponibles")
    print("2. Buscar Producto por ID")
    print("3. Productos por Categoria")
    print("4. Valor Total de inventario")
    print("5. Actualizar Stock de un producto")
    op=int(input("Ingrese opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in inventario.items():
                    if n==p:
                        if v[1]==True:
                            todos.append((n,i[0],i[1],i[2],v[0]))
            orden=sorted(todos,key= lambda x:x[1])
            for n,i,p,v,k in orden:
                print(f"{n}|{i}|{p}|Precio: {v}|Stock: {k}")
        case 2:
            id=input("Ingrese ID para buscar Producto: ").upper()
            for n,i in datos.items():
                for p,v in inventario.items():
                    if id==n and id==p:
                        print(f"{id}|{i[0]}||Precio: {i[2]}|Stock: {v[0]}")
        case 3:
            cate=input("Ingrese Categoria: ").title()
            for n,i in datos.items():
                for p,v in inventario.items():
                    if cate==i[1] and n==p:
                        print(f"{n}|{i[0]}||Precio: {i[2]}|Stock: {v[0]}")
        case 4:
            t=0
            for n,i in datos.items():
                for p,v in inventario.items():
                    if v[0] !=0 and n==p:
                        t+=i[2]*v[0]
            print(f"Valor total de inventario: ${t}")
        case 5:
            id=input("Ingrese ID de producto: ").upper()
            for n,i in datos.items():
                for p,v in inventario.items():
                    if id==n and id==p:
                        print(f"{n}|{i[0]}||Precio: {i[2]}|Stock: {v[0]}")
                        canti=int(input("Ingrese cantidad de u que agregara: "))
                        inventario[n][0]+=canti
                        print("Stock actualizado")
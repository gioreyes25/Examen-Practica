datos= {
    "V001": ["Toyota Corolla", 2023, "Gasolina", 25],
    "V002": ["Honda CR-V", 2024, "Hibrido", 35],
    "V003": ["Ford F-150", 2022, "Diesel", 45],
    "V004": ["Tesla Model 3", 2023, "Electrico", 40],
    "V005": ["BMW X5", 2024, "Gasolina", 60],
    "V006": ["Hyundai Kona", 2023, "Electrico", 30],
    "V007": ["Nissan Kicks", 2022, "Gasolina", 22],
    "V008": ["Mercedes-Benz C-Class", 2024, "Hibrido", 55],
    "V009": ["Chevrolet Silverado", 2023, "Diesel", 48],
    "V010": ["Volkswagen Jetta", 2023, "Gasolina", 28]
}

inventario = {
    "V001": [5, "Gasolina"],
    "V002": [3, "Hibrido"],
    "V003": [2, "Diesel"],
    "V004": [4, "Electrico"],
    "V005": [1, "Gasolina"],
    "V006": [6, "Electrico"],
    "V007": [7, "Gasolina"],
    "V008": [2, "Hibrido"],
    "V009": [3, "Diesel"],
    "V010": [4, "Gasolina"]
}
while True:
    print("1. Ver Vehiculos")
    print("2. Buscar Vehiculo Por ID")
    print("3. Vehiculos Por Tipo de combustible")
    print("4. Ver Valor total de stock")
    print("5. Actualizar Stock")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                todos.append((n,i))
            orden=sorted(todos,key= lambda x:x[1][0])
            for n,i in orden:
                print(f"{n}- {i[0]} {i[1]} {i[2]}")
        case 2:
            id=input("Ingrese ID de vehiculo: ").upper()
            e=False
            for n,i in datos.items():
                if id==n:
                    e=True
                    print(f"{n}- {i[0]} {i[1]} {i[2]}")
            if not e:
                print("No hay coincidencias")
        case 3:
            r=[]
            for n,i in datos.items():
                if i[2] not in r:
                    r.append(i[2])
            for n in r:
                print(n)
            com=input("Ingrese tipo de combustible que desea filtrar: ")
            e=False
            for n,i in datos.items():
                if com==i[2]:
                    e=True
                    print(f"{n}- {i[0]} {i[1]} {i[2]}")
            if not e:
                print("No hay coincidencias")
        case 4:
            s=0
            for n,i in datos.items():
                total=0
                if n:
                    for p,v in inventario.items():
                        if n==p:
                            total=v[0]*i[3]
                            s+=total
            print(f"EL Valor de inventario total es: ${s} Mil Millones USD")
        case 5:
            id=input("Ingrese ID de vehiculo para modificar stock: ").upper()
            e=False
            for n,i in inventario.items():
                if id==n:
                    e=True
                    for p,v in datos.items():
                        if id==p:
                            print(f"{p}- {v[0]} {v[1]} {v[2]} {i[0]}")
                            cantidad=int(input("Ingrese cantidad e unidades que agregara: "))
                            inventario[n][0]+=cantidad
                            print("Stock Actualizado")
            if not e:
                print("No hay coincidencias")
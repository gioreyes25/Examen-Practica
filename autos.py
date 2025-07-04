datos= {
    "A001": ["Tesla Model S", "Electrico", 75000000, 4, 0, 2020],
    "A002": ["Nissan Leaf", "Electrico", 32000000, 7, 0, 2015],
    "A003": ["Chevrolet Bolt", "Electrico", 35000000, 6, 0, 2019],
    "A004": ["BMW i3", "Electrico", 43000000, 3, 0, 2014],
    "A005": ["Audi e-tron", "Electrico", 67000000, 2, 0, 2021],
    "A006": ["Toyota Prius", "Hibrido", 28000000, 8, 0, 2010],
    "A007": ["Honda Insight", "Hibrido", 27000000, 5, 0, 2012],
    "A008": ["Ford Escape Hibrido", "Hibrido", 30000000, 4, 0, 2018],
    "A009": ["Lexus RX Hibrido", "Hibrido", 52000000, 3, 0, 2016],
    "A010": ["Hyundai Ioniq", "Hibrido", 29000000, 7, 0, 2022],
    "A011": ["Mazda 3", "Mecanico", 22000000, 10, 0, 2008],
    "A012": ["Ford Mustang", "Mecanico", 40000000, 3, 0, 2017],
    "A013": ["Chevrolet Camaro", "Mecanico", 39000000, 2, 0, 2005],
    "A014": ["Volkswagen Golf", "Mecanico", 25000000, 7, 0, 2011],
    "A015": ["Honda Civic", "Mecanico", 23000000, 9, 0, 2014],
    "A016": ["Toyota Corolla", "Mecanico", 24000000, 8, 0, 2013],
    "A017": ["Subaru Impreza", "Mecanico", 26000000, 6, 0, 2003],
    "A018": ["Tesla Model 3", "Electrico", 45000000, 5, 0, 2023],
    "A019": ["BMW X5 Hibrido", "Hibrido", 60000000, 3, 0, 2024],
    "A020": ["Ford F-150", "Mecanico", 41000000, 4, 0, 2000]
}
while True:
    print("1. Ver Stock Por Categoria")
    print("2. Buscar Autos Por Rango De Años")
    print("3. Comprar Autos")
    print("4. Ver Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cate=input("Ingrese Categoria de vehiculos: ").title()
            dispo=[valor[1] for valor in datos.values()]
            total=0
            if cate in dispo:
                for n,i in datos.items():
                    if cate==i[1]:
                        total+=i[3]
                print(f"Hay {total} Vehiculos Disponibles {cate}")
            else:
                print("Categoria ingresada no existe")
        case 2:
            n1=int(input("Ingrese año min"))
            n2=int(input("Ingrese año max"))
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            resultados=[]
            for n,i in ordenados:
                if n1 <= int(i[5]) <= n2 and i[3]!=0:
                    resultados.append(f"{n}|{i[0]}-{i[1]} Año: {i[5]}")
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No hay coincidencias")
        case 3:
            id=input("Ingrese ID del vehiculo que desea comprar: ").upper()
            if id in datos:
                for n,i in datos.items():
                    total=0
                    if id==n:
                        print(f"{n}- {i[0]} {i[1]} Precio: ${i[2]}")
                        op=input("Desea comprar Si o no: ").capitalize()
                        if op=="Si":
                            total=i[2]
                            datos[id][3]-=1
                            datos[id][4]+=total
                        else:
                            break
            else:
                print("No hay coincidencias")
        case 4:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][4])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n}|{v[0]} {v[1]} Total Ganancias: {v[4]}")
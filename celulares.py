datos = {
    "M001": ["iPhone 13", "Smartphone", 800000, 15, 0, 2021],
    "M002": ["Samsung Galaxy S21", "Smartphone", 750000, 12, 0, 2021],
    "M003": ["iPad Pro", "Tablet", 900000, 10, 0, 2022],
    "M004": ["Samsung Galaxy Tab S7", "Tablet", 850000, 8, 0, 2020],
    "M005": ["OnePlus 9", "Smartphone", 650000, 14, 0, 2021],
    "M006": ["Google Pixel 6", "Smartphone", 700000, 10, 0, 2021],
    "M007": ["Xiaomi Mi 11", "Smartphone", 600000, 20, 0, 2021],
    "M008": ["Amazon Fire HD 10", "Tablet", 400000, 9, 0, 2019],
    "M009": ["Samsung Galaxy Note 20", "Smartphone", 850000, 7, 0, 2020],
    "M010": ["Huawei MatePad", "Tablet", 780000, 6, 0, 2021]
}
while True:
    print("1. Ver Stock por categoria")
    print("2. Ver Productos por años")
    print("3. Comprar")
    print("4. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cate=input("Ingrese categoria: ").capitalize()
            dispo=[valor[1] for valor in datos.values()]
            total=0
            if cate in dispo:
                for n,i in datos.items():
                    if cate==i[1]:
                        total+=i[3]
                print(f"El stock de {cate} es: {total}")
            else:
                print("No hay coincidencias")
        case 2:
            n1=int(input("Ingrese año min"))
            n2=int(input("Ingrese año max"))
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            resultados=[]
            for n,i in ordenados:
                if n1 <= int(i[5]) <= n2 and i[3]!=0:
                    resultados.append(f"{n}- {i[0]},{i[1]} Año: {i[5]}")
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("No hay coincidencias")
        case 3:
            id=input("Ingrese ID de producto que desea comprar: ").upper()
            if id in datos:
                total=0
                for n,i in datos.items():
                    if id==n:
                        print(f"{n}- {i[0]},{i[1]} Año: {i[5]}")
                        cantidad=int(input("Ingrese cantidad: "))
                        total=cantidad*i[2]
                        datos[n][4]+=total
                        datos[n][3]+=cantidad
            else:
                print("No hay coincidencias")
        case 4:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][4])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n} {v[0]},{v[1]} Ganancias Totales: {v[4]}")

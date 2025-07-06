empleados = {
    "E001": ["Camila", 35, "Jefe De Area", [1800000, 1850000, 1900000]],
    "E002": ["Mauricio", 45, "Jefe De Area", [2000000, 1980000, 2020000]],
    "E003": ["Valentina", 40, "Jefe De Area", [1950000, 1930000, 1970000]],
    "E004": ["Daniel", 28, "Desarrollador Backend", [1300000, 1320000, 1350000]],
    "E005": ["Sofia", 30, "Desarrollador Backend", [1250000, 1260000, 1280000]],
    "E006": ["Ignacio", 26, "Desarrollador Backend", [1180000, 1200000, 1190000]],
    "E007": ["Martina", 25, "Desarrollador Frontend", [1150000, 1170000, 1180000]],
    "E008": ["Javier", 32, "Desarrollador Frontend", [1230000, 1220000, 1250000]],
    "E009": ["Lucas", 29, "Desarrollador Frontend", [1210000, 1200000, 1220000]],
    "E010": ["Florencia", 27, "Qa Tester", [1050000, 1060000, 1070000]],
    "E011": ["Benjamin", 31, "Qa Tester", [1100000, 1110000, 1090000]],
    "E012": ["Tomas", 24, "Qa Tester", [1000000, 1020000, 1010000]],
    "E013": ["Isidora", 33, "Analista De Datos", [1280000, 1300000, 1270000]],
    "E014": ["Cristobal", 38, "Analista De Datos", [1350000, 1330000, 1360000]],
    "E015": ["Antonia", 29, "Analista De Datos", [1320000, 1340000, 1310000]]
}
datos={}
if not datos:
    for n,i in empleados.items():
        if n:
            sueldo=(sum(empleados[n][3]))/3
            sueldo=round(sueldo)
            datos[n]=[i[0],i[1],i[2],sueldo]
while True:
    print("1. Ver Empleados")
    print("2. Buscar Por Cargo")
    print("3. Top 3 empleados con mas sueldo")
    print("4. Actualizar Sueldo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("1. Ver Todos Los Empleados")
            print("2. Filtrar Por Rango De Edad")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    ordenados=sorted(datos.items(),key= lambda x:x[1][0])
                    for n,i in ordenados:
                        print(f"{n}- {i[0]}|Edad:{i[1]}|Puesto: {i[2]}|Sueldo: ${i[3]}")
                case 2:
                    n1=int(input("Ingrese año min: "))
                    n2=int(input("Ingrese año max: "))
                    ordenados=sorted(datos.items(),key= lambda x:x[1][0])
                    resultados=[]
                    for n,i in ordenados:
                        if n1 <= (i[1]) <=n2:
                            resultados.append(f"{n}- {i[0]}|Edad:{i[1]}|Puesto: {i[2]}|Sueldo: ${i[3]}")
                    if resultados:
                        for r in resultados:
                            print(r)
                    else:
                        print("No hay coincidencias en ese rango de edad")
        case 2:
            cargo=input("Ingrese Cargo A Buscar: ").title()
            dispo=[valor[2] for valor in datos.values()]
            if cargo in dispo:
                for n,i in datos.items():
                    if cargo==i[2]:
                        print(f"{n}- {i[0]}|Edad:{i[1]}|Puesto: {i[2]}|Sueldo: ${i[3]}")
            else:
                print("No hay coincidencias")
        case 3:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][3])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {v[0]} {v[1]} Sueldo: {v[3]}")
        case 4:
            id=input("Ingrese id de el empleado: ").upper()
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        print(f"{n}- {i[0]}|Edad:{i[1]}|Puesto: {i[2]}|Sueldo: ${i[3]}")
                        sueldo=int(input("Ingrese el aumento de sueldo que el dara: "))
                        datos[n][3]+=sueldo
                        print(f"Su sueldo ahora es de {datos[n][3]}")
            else:
                print("No hay coincidencias")

datos= {
    "PROJ001": ["Aplicacion de Gestion de Clientes", "2024-01-15", "Equipo Alfa", 50000],
    "PROJ002": ["Plataforma de E-commerce", "2023-11-01", "Equipo Beta", 75000],
    "PROJ003": ["Sistema de Inventario Automatizado", "2025-02-20", "Equipo Gamma", 30000],
    "PROJ004": ["Desarrollo de API de Pagos", "2024-03-10", "Equipo Delta", 40000],
    "PROJ005": ["Actualizacion de Seguridad Web", "2025-01-05", "Equipo Alfa", 20000]
}

estado = {
    "PROJ001": ["Activo", 60, "2025-07-01"],
    "PROJ002": ["Completado", 100, "2025-06-15"],
    "PROJ003": ["En Pausa", 10, "2025-07-05"],
    "PROJ004": ["Activo", 85, "2025-06-28"],
    "PROJ005": ["Activo", 30, "2025-07-03"]
}
esta=[]
for p,v in estado.items():
    if v[0] not in esta:
        esta.append(v[0])
while True:
    print("1. Ver Proyectos Activos")
    print("2. Ver Proyecto Especifico")
    print("3. Ver Proyectos Por Equipo")
    print("4. Ver Presupuesto de proyectos activos total")
    print("5. Actualizar Progreso de un proyecto")
    op=int(input("Ingrese opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                for p,v in estado.items():
                        if v[0]=="Activo":
                            if p==n:
                                print(f"{n}- {i[0]} {i[1]} {i[2]} {i[3]} {v[0]}")
        case 2:
            id=input("Ingrese ID para ver proyecto: ").upper()
            for n,i in datos.items():
                for p,v in estado.items():
                    if id==n and id==p:
                        print(f"{n}- {i[0]} {i[1]} {i[2]} {i[3]} {v[0]}")
        case 3:
            t=[]
            for n,i in datos.items():
                if i[2] not in t:
                    t.append(i[2])
            for n in t:
                print(n)
            team=input("Ingrese equipo: ")
            for n,i in datos.items():
                for p,v in estado.items():
                    if team==i[2] and n==p:
                        print(f"{n}- {i[0]} {i[1]} {i[2]} {i[3]} {v[0]}")
        case 4:
            t=0
            for n,i in datos.items():
                for p,v in estado.items():
                    if v[0]=="Activo" and n==p:
                        t+=i[3]
            print(f"El presupuesto de proyectos activos es: ${t}")
        case 5:
            id=input("Ingrese id para modificar proyecto: ").upper()
            for n,i in datos.items():
                for p,v in estado.items():
                    if v[0] not in esta:
                            esta.append(v[0])
                    if id==n and id==p:
                        print(f"{n}- {i[0]} {i[1]} {i[2]} {i[3]} {v[0]}")
                        for r in esta:
                            print(r)
                        modi=input("Ingrese estado que pasara proyecto: ").title()
                        if modi in esta:
                            estado[id][0]=modi
                            print("Proyecto ha sido modificado con exito")
                        else:
                            print("Estado ingresado incorrectamente")
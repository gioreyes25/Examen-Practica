datos = {
    "Matemáticas": {
        "Juan": {"edad": 15, "nota": 6.2},
        "Ana": {"edad": 14, "nota": 5.8},
        "Luis": {"edad": 15, "nota": 7.0},
        "Sofía": {"edad": 14, "nota": 6.5},
        "Carlos": {"edad": 16, "nota": 5.9}
    },
    "Historia": {
        "Juan": {"edad": 15, "nota": 5.5},
        "Ana": {"edad": 14, "nota": 6.1},
        "Luis": {"edad": 15, "nota": 5.7},
        "Sofía": {"edad": 14, "nota": 6.9},
        "Carlos": {"edad": 16, "nota": 6.3}
    },
    "Ciencias": {
        "Juan": {"edad": 15, "nota": 6.8},
        "Ana": {"edad": 14, "nota": 6.0},
        "Luis": {"edad": 15, "nota": 6.4},
        "Sofía": {"edad": 14, "nota": 6.2},
        "Carlos": {"edad": 16, "nota": 7.0}
    }
}
while True:
    print("1. Ver Estudiantes")
    print("2. Ver Estudaintes Por Asignatura")
    print("3. Ver Top 3 estudiantes")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            ordenados=sorted(datos.items())
            for a,v in ordenados:
                print(f"Nombre: {a} Nota: {v["edad"]} Nota: {v["nota"]}")
        case 2:
            buscar=input("Ingrese asignatua que desea buscar: ").title()
            for n,i in datos.items():
                    for r,v in i.items():
                        ordenados=sorted(datos[buscar].items(),key= lambda x:x[1]["nota"])
                    if buscar==n:
                        print(f"{n}")
                        for a,x in ordenados:
                            print(f"Nombre: {a} Nota: {x["edad"]} Nota: {x["nota"]}")
        case 3:
            print
            
datos = {
    "entradas": {
        "znsalada cesar": {"precio": 4500, "tiempo": 10, "vegetariano": True},
        "empanadas": {"precio": 3000, "tiempo": 15, "vegetariano": False},
        "sopa de verduras": {"precio": 4000, "tiempo": 12, "vegetariano": True}
    },
    "platos fuertes": {
        "lomo saltado": {"precio": 8500, "tiempo": 20, "vegetariano": False},
        "pasta al pesto": {"precio": 7500, "tiempo": 18, "vegetariano": True},
        "pollo al horno": {"precio": 8000, "tiempo": 25, "vegetariano": False}
    },
    "postres": {
        "helado": {"precio": 2500, "tiempo": 5, "vegetariano": True},
        "tarta de manzana": {"precio": 3000, "tiempo": 10, "vegetariano": True},
        "flan": {"precio": 2800, "tiempo": 8, "vegetariano": True}
    }
}
while True:
    print("1. Listar Platos por seccion")
    print("2. Buscar Plato")
    print("3. Ver Platos Para Vegetarianos")
    print("4. Mostrar Platos Por Orden de preparacion")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            b=input("Ingrese seccion que desea filtrar: ")
            if b in datos:
                print(b)
                for n,i in datos.items():
                    for p,v in i.items():
                        todos.append((n,p,v))
                    ordenados=sorted(todos,key= lambda x:x[1])
                for se,pl,inf in ordenados:
                    if b==se:
                        print(f"{se} {pl} {inf["precio"]}")
        case 2:
            buscar=input("Ingrese plato que desea buscar: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    if buscar==p:
                        encontrado=True
                        print(f"Seccion: {n}|Plato: {p}|Precio: {v["precio"]}|Tiempo: {v["tiempo"]}")
            if not encontrado:
                print("No hay coincidencias")
        case 3:
            print("Platos Vegetarianos")
            for n,i in datos.items():
                for p,v in i.items():
                    if v["vegetariano"]==True:
                        print(f"Seccion: {n}|Plato: {p}|Precio: {v["precio"]}|Tiempo: {v["tiempo"]}")
        case 4:
            todos=[]
            for seccion,platos in datos.items():
                for nombre,info in platos.items():
                    todos.append((seccion,nombre,info))
            ordenados=sorted(todos,key= lambda x: x[2]["tiempo"])
            for seccion,plato,tiempo in ordenados:
                print(f"Seccion: {seccion}|Plato: {plato}|Tiempo: {tiempo["tiempo"]}")
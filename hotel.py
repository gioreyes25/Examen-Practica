datos = {
    "H001": ["Habitación Simple", "Económica", 45000, 5, 0],
    "H002": ["Habitación Doble Ejecutiva", "Estándar", 68000, 0, 0],
    "H003": ["Suite Premium con Vista al Mar", "Lujo", 125000, 5, 0]
}
ventas=[]
while True:
    print("1. Reservar Habitacion")
    print("2. Ver Habitaciones Disponibles")
    print("3. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            id=input("Ingrese ID de habitacion: ").upper()
            if id in datos:
                for n,i in datos.items():
                    total=0
                    if id==n:
                        if i[3]!=0:
                            print(f"{n}- {i[0]} Disponibles: {i[3]}")
                            op=input("¿Desea Reservar? Si o No: ").capitalize()
                            if op=="Si":
                                datos[id][3]-=1
                                total=i[2]
                                datos[id][4]+=total
                                print(f"Felicidades ha reversado exitosamente")
                            else:
                                break
                        else:
                            print("No quedan habitaciones para esta categoria disponibles")
            else:
                print("ID no existe")
        case 2:
            for n,i in datos.items():
                if i[3]!=0:
                    print(f"{n}- {i[0]} Disponibles: {i[3]}")
                else:
                    print(f"{n}- {i[0]} Disponibles: 0")
        case 3:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][4])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- ID {n}| {v[0]}| Ingresos Totales: {v[4]}")
                    

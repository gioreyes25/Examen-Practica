datos = {
    "T001": ["París", "Europa", 1200, 8,0],
    "T002": ["Cancún", "America", 950, 10,0],
    "T003": ["Machu Picchu", "America", 800, 5,0],
    "T004": ["Tokio", "Asia", 1500, 8,0],
    "T005": ["El Cairo", "Africa", 1100, 6,0],
    "T006": ["Roma", "Europa", 1150, 9,0],
    "T007": ["Nueva York", "America", 980, 14,0],
    "T008": ["Bangkok", "Asia", 1300, 7,0],
    "T009": ["Ciudad del Cabo", "Africa", 1250, 4,0],
    "T010": ["Barcelona", "Europa", 1180, 11,0]
}
while True:
    print("\n1. Cantidad de pasajeros por destino")
    print("2. Ver Vuelos")
    print("3. Actualizar Vuelos")
    print("4. Eliminar Vuelo")
    print("5. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            desti=input("Ingrese destino a ver: ").title()
            total=0
            dispo=[valor[1] for valor in datos.values()]
            if desti in dispo:
                for n,i in datos.items():
                    if desti==i[1]:
                        total+=i[3]
                print(f"La cantidad de pasajeros que viajan a {desti} son: {total}")
            else:
                print("No hay coincidencias")
        case 2:
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            resultados=[]
            for n,i in ordenados:
                if i[3]!=0:
                    resultados.append(f"Destino: {i[0]},{i[1]}|Pasajeros: {i[3]}")
            if resultados:
                for r in resultados:
                    print(r)
        case 3:
            id=input("Ingrese ID del vuelo: ").upper()
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        print(f"{i[0]},{i[1]}|Pasajeros Actuales: {i[3]}")
                        cantidad=int(input("Ingrese cantida de pasajeros que agregara al vuelo"))
                        datos[id][3]+=cantidad
                        print("Vuelo Actualizado Exitosamente")
                        print(f"{i[0]},{i[1]}|Pasajeros Ahora: {i[3]}")
            else:
                print("No hay coincidencias")
        case 4:
            delete=input("Ingrese ID de vuelo a eliminar: ").upper()
            if delete in datos:
                del datos[delete]
                print(f"Se ha eliminado el vuelo {delete}")
            else:
                print("ID NO EXISTE")
        case 5:
            import heapq
            for n,i in datos.items():
                total=0
                if n:
                    total=i[2]*i[3]
                    datos[n][4]+=total
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][4])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- Vuelo: {n}|{v[0]},{v[1]}|Total Ganancias: ${v[4]}")
                    
                    
            
            

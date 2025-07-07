juga= {
    "J001": ["Matias", 30, "Colo Colo", "Arquero", [0, 0, 15]],
    "J002": ["Lucas", 28, "Colo Colo", "Defensa", [2, 1, 18]],
    "J003": ["Tomas", 25, "Colo Colo", "Delantero", [10, 5, 16], [0.3, 0.4, 0.5]],
    "J004": ["Joaquin", 27, "Colo Colo", "Mediocampista", [4, 7, 17], [0.4, 0.5, 0.6]],
    "J005": ["Ignacio", 24, "Universidad De Chile", "Delantero", [12, 6, 15], [0.5, 0.4, 0.6]],
    "J006": ["Benjamin", 29, "Universidad De Chile", "Defensa", [1, 1, 19]],
    "J007": ["Santiago", 31, "Universidad De Chile", "Arquero", [0, 0, 20]],
    "J008": ["Cristobal", 26, "Universidad De Chile", "Mediocampista", [3, 8, 18], [0.6, 0.5, 0.7]],
    "J009": ["Diego", 22, "Universidad Catolica", "Delantero", [9, 4, 14], [0.3, 0.2, 0.4]],
    "J010": ["Rodrigo", 30, "Universidad Catolica", "Defensa", [0, 1, 17]],
    "J011": ["Gabriel", 28, "Universidad Catolica", "Mediocampista", [2, 6, 16], [0.4, 0.5, 0.3]],
    "J012": ["Felipe", 27, "Universidad Catolica", "Arquero", [0, 0, 18]],
    "J013": ["Andres", 25, "Union Espanola", "Delantero", [11, 7, 17], [0.6, 0.5, 0.7]],
    "J014": ["Emilio", 23, "Union Espanola", "Mediocampista", [5, 5, 15], [0.4, 0.5, 0.4]],
    "J015": ["Sebastian", 32, "Union Espanola", "Defensa", [1, 2, 20]]
}
datos={}
if not datos:
    for n,i in juga.items():
        if n:
            pj=juga[n][4][2]
            gl=juga[n][4][0]
            asi=juga[n][4][1]
            if i[3] == "Delantero" or i[3]=="Mediocampista":
                proasi=(sum(juga[n][5]))/3
                proasi=round(proasi,1)
                datos[n]=[i[0],i[1],i[2],i[3],pj,gl,asi,proasi]
            else:
                datos[n]=[i[0],i[1],i[2],i[3],pj,gl,asi]
                
while True:
    print("1. Ver Jugadores")
    print("2. Buscar Jugadores Por Equipo")
    print("3. Top 5 Goleadores")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            for n,i in ordenados:
                if i[3] == "Delantero" or i[3]=="Mediocampista":
                    print(f"Jugador: {i[0]} Edad: {i[1]} Equipo: {i[2]} Posicion: {i[3]}\nPartidos Jugados: {i[4]}\nGoles Anotados: {i[5]}\nAsistencias: {i[6]}\nPromedio De Asistencias: {i[7]}")
                    print()
                else:
                    print(f"Jugador: {i[0]} Edad: {i[1]} Equipo: {i[2]} Posicion: {i[3]}\nPartidos Jugados: {i[4]}\nGoles Anotados: {i[5]}\nAsistencias: {i[6]}")
                    print()
        case 2:
            team=input("Ingrese equipo: ").title()
            dispo=[valor[2] for valor in datos.values()]
            if team in dispo:
                for n,i in datos.items():
                    if team==i[2]:
                        if i[3] == "Delantero" or i[3]=="Mediocampista":
                            print(f"Jugador: {i[0]} Edad: {i[1]} Equipo: {i[2]} Posicion: {i[3]}\nPartidos Jugados: {i[4]}\nGoles Anotados: {i[5]}\nAsistencias: {i[6]}\nPromedio De Asistencias: {i[7]}")
                        else:
                            print(f"Jugador: {i[0]} Edad: {i[1]} Equipo: {i[2]} Posicion: {i[3]}\nPartidos Jugados: {i[4]}\nGoles Anotados: {i[5]}\nAsistencias: {i[6]}")
            else:
                print("No hay coincidencias")
        case 3:
            import heapq
            print("1. Top Mayores Goleadores")
            print("2. Top Mayores Asistidores")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(5,datos.items(),key= lambda x:x[1][5])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- Jugador: {v[0]} Edad: {v[1]} Equipo: {v[2]} Posicion: {v[3]}\nPartidos Jugados: {v[4]}\nGoles Anotados: {v[5]}")
                        print()
                case 2:
                    top=heapq.nlargest(5,datos.items(),key= lambda x:x[1][6])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- Jugador: {v[0]} Edad: {v[1]} Equipo: {v[2]} Posicion: {v[3]}\nPartidos Jugados: {v[4]}\nAsistencias: {v[6]}")
                        print()

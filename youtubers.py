streamers = {
    "Y001": ["Fernanfloo", 30, "Gaming", [950000, 970000, 960000]],
    "Y002": ["HolaSoyGerman", 34, "Entretenimiento", [1500000, 1480000, 1495000]],
    "Y003": ["ElRubiusOMG", 34, "Gaming", [1250000, 1230000, 1240000]],
    "Y004": ["Luisito Comunica", 33, "Entretenimiento", [1400000, 1390000, 1385000]],
    "Y005": ["AuronPlay", 35, "Entretenimiento", [1300000, 1320000, 1310000]],
    "Y006": ["TheDonato", 24, "Gaming", [890000, 910000, 905000]],
    "Y007": ["Mikecrack", 31, "Gaming", [1150000, 1160000, 1145000]],
    "Y008": ["Kimberly Loaiza", 26, "Música", [1050000, 1070000, 1065000]],
    "Y009": ["Juan De Dios Pantoja", 28, "Música", [980000, 990000, 985000]],
    "Y010": ["DimeNacho", 25, "Entretenimiento", [400000, 420000, 410000]],
    "Y011": ["Lyna", 29, "Gaming", [870000, 880000, 875000]],
    "Y012": ["Pautips", 30, "Entretenimiento", [600000, 620000, 610000]],
    "Y013": ["Kenia OS", 24, "Música", [750000, 770000, 760000]],
    "Y014": ["Yolo Aventuras", 27, "Entretenimiento", [950000, 960000, 955000]],
    "Y015": ["Antrax", 27, "Gaming", [920000, 940000, 930000]]
}
datos={}
if not datos:
    for n,i in streamers.items():
        vistas=sum(streamers[n][3])/3
        vistas=round(vistas)
        datos[n]=[i[0],i[1],i[2],vistas]
while True:
    print("1. Ver Lista De Youtubers")
    print("2. Buscar Youtubers Por ID")
    print("3. Filtrar Youtubers Por Categoria")
    print("4. Top 3 youtubers")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            for n,i in ordenados:
                print(f"Canal: {i[0]}|Edad: {i[1]}|Categoria: {i[2]} Vistas mensuales: {i[3]}")
        case 2:
            id=input("Ingrese ID de youtuber que desea buscar: ").upper()
            if id in datos:
                for n,i in datos.items():
                    if id==n:
                        print(f"Canal: {i[0]}|Edad: {i[1]}|Categoria: {i[2]} Vistas mensuales: {i[3]}")
            else:
                print("No hay coincidencias")
        case 3:
            cate=input("Ingrese categoria que desea filtrar: ").title()
            dispo=[valor[2] for valor in datos.values()]
            if cate in dispo:
                for n,i in datos.items():
                    if cate==i[2]:
                        print(f"Canal: {i[0]}|Edad: {i[1]}|Categoria: {i[2]} Vistas mensuales: {i[3]}")
            else:
                print("No hay coincidencias")
        case 4:
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1][3])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {v[0]} {v[1]} {v[2]} {v[3]}")
                

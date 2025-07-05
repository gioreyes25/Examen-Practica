ventas = {
    "Norte": [
        {"producto": "Arroz", "precio_unitario": 1200, "cantidad_vendida": 35},
        {"producto": "Leche", "precio_unitario": 950, "cantidad_vendida": 50},
        {"producto": "Pan", "precio_unitario": 500, "cantidad_vendida": 80},
        {"producto": "Huevos", "precio_unitario": 150, "cantidad_vendida": 200},
        {"producto": "Azucar", "precio_unitario": 1000, "cantidad_vendida": 45}
    ],
    "Centro": [
        {"producto": "Fideos", "precio_unitario": 1100, "cantidad_vendida": 60},
        {"producto": "Aceite", "precio_unitario": 2500, "cantidad_vendida": 30},
        {"producto": "Cafe", "precio_unitario": 2000, "cantidad_vendida": 25},
        {"producto": "Galletas", "precio_unitario": 900, "cantidad_vendida": 70},
        {"producto": "Sal", "precio_unitario": 700, "cantidad_vendida": 90}
    ],
    "Sur": [
        {"producto": "Jabon", "precio_unitario": 1500, "cantidad_vendida": 40},
        {"producto": "Detergente", "precio_unitario": 2800, "cantidad_vendida": 20},
        {"producto": "Shampoo", "precio_unitario": 3000, "cantidad_vendida": 15},
        {"producto": "Toalla", "precio_unitario": 2500, "cantidad_vendida": 10},
        {"producto": "Cepillo", "precio_unitario": 1000, "cantidad_vendida": 25}
    ]
}
while True:
    print("1. Calcular el total de ingresos por región")
    print("2. Mostrar el producto más vendido por región")
    print("3. Mostrar el top 3 productos con más ingresos (precio x cantidad)")
    print("4. Buscar un producto y mostrar en qué regiones se vendió")
    print("5. Calcular el total general de ventas del país")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            total=0
            pais=0
            for n,i in ventas.items():
                for v in i:
                    if n:
                        total+= v["precio_unitario"]*v["cantidad_vendida"]
                print(f"Region: {n} Ventas Totales: ${total}")
                pais+=total
            print(f"Ventas Totales En El Pais: ${pais}")
            total=0
        case 2:
            import heapq
            for n,i in ventas.items():
                top=heapq.nlargest(1,i,key= lambda x: x["cantidad_vendida"])
                for i,pro in enumerate(top,start=1):
                    print(f"{i}- {n} {pro["cantidad_vendida"]} {pro["producto"]}")
        case 3:
            print
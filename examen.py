from funci import menu,stockgenero,busquedaaño,actualizarstock
datos = {
    "A001": ["Thriller", 1982, "Pop", 15],
    "A002": ["Back in Black", 1982, "Rock", 10],
    "A003": ["The Dark Side of the Moon", 1973, "Rock", 8],
    "A004": ["The Bodyguard", 1992, "RB", 12],
    "A005": ["Rumours", 1977, "Rock", 9],
    "A006": ["Run", 2011, "Pop", 11],
    "A007": ["Come Away With Me", 2002, "Jazz", 0],
    "A008": ["Abbey Road", 1970, "Rock", 13],
    "A009": ["Hotel California", 1970, "Rock", 10],
    "A010": ["Zilk", 2014, "Pop", 14]
}
inventario = {
    "A001": [15, "Pop"],
    "A002": [10, "Rock"],
    "A003": [8, "Rock"],
    "A004": [12, "RB"],
    "A005": [9, "Rock"],
    "A006": [11, "Pop"],
    "A007": [0, "Jazz"],
    "A008": [13, "Rock"],
    "A009": [10, "Rock"],
    "A010": [14, "Pop"]
}
while True:
    print(inventario)
    menu()
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            genero=input("Ingrese genero a buscar: ").title()
            stockgenero(genero,inventario,op)
        case 2:
            num1=int(input("Ingrese año min"))
            num2=int(input("Ingrese año max"))
            busquedaaño(num1,num2,datos)
        case 3:
            id=input("Ingrese ID para actualizar stock: ").upper()
            cantidad=int(input("Ingrese ingrese cantidad a actualizar"))
            actualizarstock(id,cantidad,inventario)
        case 4:
            print("Programa finalizado")
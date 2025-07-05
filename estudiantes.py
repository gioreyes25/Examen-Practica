datos = {
    "E001": {
        "nombre": "Camila",
        "edad": 22,
        "cursos": {
            "Python": {"nota_final": 6.5, "porcentaje_asistencia": 90},
            "Bases De Datos": {"nota_final": 5.8, "porcentaje_asistencia": 95}
        }
    },
    "E002": {
        "nombre": "Tomas",
        "edad": 25,
        "cursos": {
            "Python": {"nota_final": 4.5, "porcentaje_asistencia": 60},
            "Html Y Css": {"nota_final": 6.0, "porcentaje_asistencia": 85}
        }
    },
    "E003": {
        "nombre": "Valentina",
        "edad": 20,
        "cursos": {
            "Javascript": {"nota_final": 5.0, "porcentaje_asistencia": 80},
            "Python": {"nota_final": 6.8, "porcentaje_asistencia": 92}
        }
    },
    "E004": {
        "nombre": "Ignacio",
        "edad": 23,
        "cursos": {
            "Bases De Datos": {"nota_final": 3.5, "porcentaje_asistencia": 70},
            "Machine Learning": {"nota_final": 4.2, "porcentaje_asistencia": 88}
        }
    },
    "E005": {
        "nombre": "Sofia",
        "edad": 26,
        "cursos": {
            "Python": {"nota_final": 7.0, "porcentaje_asistencia": 100},
            "Machine Learning": {"nota_final": 6.5, "porcentaje_asistencia": 93}
        }
    },
    "E006": {
        "nombre": "Luis",
        "edad": 28,
        "cursos": {
            "Html Y Css": {"nota_final": 5.9, "porcentaje_asistencia": 78},
            "Javascript": {"nota_final": 6.1, "porcentaje_asistencia": 82}
        }
    },
    "E007": {
        "nombre": "Martina",
        "edad": 21,
        "cursos": {
            "Bases De Datos": {"nota_final": 4.0, "porcentaje_asistencia": 75},
            "Python": {"nota_final": 4.5, "porcentaje_asistencia": 65}
        }
    },
    "E008": {
        "nombre": "Benjamin",
        "edad": 24,
        "cursos": {
            "Javascript": {"nota_final": 3.9, "porcentaje_asistencia": 74},
            "Machine Learning": {"nota_final": 5.5, "porcentaje_asistencia": 90}
        }
    },
    "E009": {
        "nombre": "Daniela",
        "edad": 22,
        "cursos": {
            "Html Y Css": {"nota_final": 6.0, "porcentaje_asistencia": 57},
            "Python": {"nota_final": 5.2, "porcentaje_asistencia": 85},
            "Machine Learning": {"nota_final": 4.9, "porcentaje_asistencia": 91}
        }
    },
    "E010": {
        "nombre": "Cristobal",
        "edad": 27,
        "cursos": {
            "Bases De Datos": {"nota_final": 6.3, "porcentaje_asistencia": 88},
            "Javascript": {"nota_final": 6.7, "porcentaje_asistencia": 92}
        }
    }
}
nota=[]
if not nota:
    for n,i in datos.items():
        nombre=i["nombre"]
        if n:   
            for cur,v in i["cursos"].items():
                nota.append((nombre,cur,v["nota_final"]))
while True:
    print("1. Ver Estudiantes")
    print("2. Mostrar Promedio de curso x")
    print("3. Mostrar Estudiantes Aprobados Y Reprobados")
    print("4. Ver top 3 estudaintes")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                print(f"Nombre: {i["nombre"]} Edad: {i["edad"]}")
                for cur,v in i["cursos"].items():
                    print(f"Curso: {cur} Nota Final: {v["nota_final"]} Asistencia: {v["porcentaje_asistencia"]}")
                print()
        case 2:
            curso=input("Ingrese curso a ver: ").title()
            dispo = [curso for estudiante in datos.values() for curso in estudiante["cursos"]]
            c=0
            promedio=0
            if curso in dispo:
                for n,i in datos.items():
                    for v,r in i["cursos"].items():
                        if curso==v:
                            c+=1
                            promedio+=r["nota_final"]
                            print(f"proemdio {promedio}")
                promedio/=c
                promedio=round(promedio,1)
                print(f"El promedio de el curso {curso} es {promedio}")
                c=0
        case 3:
            for n,i in datos.items():
                print(f"Nombre: {i["nombre"]} Edad: {i["edad"]}")
                for cur,v in i["cursos"].items():
                    if v["nota_final"] >=4 and v["porcentaje_asistencia"] >=75:
                        print(f"Aprobo {cur} Nota Final: {v["nota_final"]} Asistencia: {v["porcentaje_asistencia"]}")
                    else:
                        print(f"Reprobo {cur} Nota Final: {v["nota_final"]} Asistencia: {v["porcentaje_asistencia"]}")
                print()
        case 4:
            import heapq
            top=heapq.nlargest(3,nota,key= lambda x:x[2])
            for i,(name,curso,nota) in enumerate(top,start=1):
                print(f"{i}- {name} {curso} {nota}")
           
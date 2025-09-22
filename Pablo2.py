dic_ejemplo = {
    'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],
    'Curso': "Big Data",
    'Edad': [23, 21, 20, 22],
    'Presencial': [True,False,True,False]
}
setnumAlumnos = set(dic_ejemplo['Edad'])
setpresencial = set(dic_ejemplo['Presencial'])
print(setnumAlumnos)
print(len(setnumAlumnos))
print(setpresencial)
# Mostrar cantidad de alumnos presenciales y remotos
presenciales = dic_ejemplo['Presencial'].count(True)
remotos = dic_ejemplo['Presencial'].count(False)
print("Alumnos presenciales: {presenciales}")
print("Alumnos remotos: {remotos}")

# Mostrar nombres según modalidad
for alumno, presencial in zip(dic_ejemplo['Alumnos'], dic_ejemplo['Presencial']):
    if presencial:
        print("{alumno} es presencial")
    else:
        print("{alumno} es remoto")
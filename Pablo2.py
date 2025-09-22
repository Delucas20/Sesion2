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
# Mostrar alumnos según modalidad
alumnos = dic_ejemplo['Alumnos']
presencialidad = dic_ejemplo['Presencial']
presenciales = [alumnos[i] for i in range(len(alumnos)) if presencialidad[i]]
remotos = [alumnos[i] for i in range(len(alumnos)) if not presencialidad[i]]
print(f"Alumnos presenciales: {presenciales}")
print(f"Alumnos remotos: {remotos}")
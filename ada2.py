num_alumnos = 100
num_materias = 6

calificaciones = []

valor = 1
for i in range(num_alumnos):
    alumno = []
    for j in range(num_materias):
        alumno.append(valor)
        valor += 1
    calificaciones.append(alumno)

print("Calificaciones de las materias:")
for i in range(num_materias):
    print(f"Materia {i+1}: ", end="")
    for j in range(num_alumnos):
        print(calificaciones[j][i], end=" ")
    print()  

valor = calificaciones[94][4]
print(f"\nLa calificación del alumno 95 en la materia 5 es: {valor}")
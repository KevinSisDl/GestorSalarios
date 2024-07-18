usuarios_registrados = {
    "Carlos": "12345",
    "Maria": "20103",
    "Miguel": "24105"
}

def autenticar_usuario():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        if usuario in usuarios_registrados and usuarios_registrados[usuario] == password:
            print(f"Bienvenido, {usuario}.\n")
            return True
        else:
            print("Credenciales incorrectas. Por favor, intente nuevamente.\n")
        
print("Bienvenido al sistema de gestión de salarios")

autenticado = autenticar_usuario()

if autenticado:
    num_empleados = int(input("Ingrese la cantidad de empleados: "))

salarios = []

for i in range(num_empleados):
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
    salarios.append(salario)

suma_salarios = sum(salarios)

salario_promedio = suma_salarios / num_empleados

salario_maximo = max(salarios)
salario_minimo = min(salarios)

salarios_ordenados = sorted(salarios)
n = len(salarios)
if n % 2 == 0:
    mediana = (salarios_ordenados[n//2 - 1] + salarios_ordenados[n//2]) / 2
else:
    mediana = salarios_ordenados[n//2]
    
rango_salarios = salario_maximo - salario_minimo

salarios_descendente = sorted(salarios, reverse=True)

salarios_debajo_del_promedio = int(sum(1 for salario in salarios if salario < salario_promedio))

porcentaje_debajo_promedio = (salarios_debajo_del_promedio / num_empleados) * 100

print("Salarios:")
for i, salario in enumerate(salarios, 1):
    print(f"Empleado {i}: {salario:.2f}")

print(f"\nSuma de salarios: {suma_salarios:.2f}")
print(f"Salario promedio: {salario_promedio:.2f}")
print(f"Salario máximo: {salario_maximo:.2f}")
print(f"Salario mínimo: {salario_minimo:.2f}")
print(f"Mediana de salarios: {mediana:.2f}")
print(f"Número de salarios por debajo del promedio: {salarios_debajo_del_promedio}")
print(f"Rango de salarios: {rango_salarios:.2f}")
print(f"Porcentaje de salarios debajo del promedio: {porcentaje_debajo_promedio:.2f}%")

print("\n--- Detalle de salarios en orden descendente ---")
for i, salario in enumerate(salarios_descendente, 1):
    print(f"Empleado {i}: {salario:.2f}")

print("\nGracias por utilizar nuestro sistema!")
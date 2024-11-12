costo_operador1 = float(input("Digite el costo de cada llamada al primer operador: "))
costo_operador2 = float(input("Digite el costo de cada llamada al segundo operador: "))
costo_total_operador1 = costo_operador1 * 2
costo_total_operador2 = costo_operador2 * 2
costo_total_llamadas = costo_total_operador1 + costo_total_operador2
print(f"Costo de cada llamada al primer operador: {costo_operador1}")
print(f"Costo de cada llamada al segundo operador: {costo_operador2}")
print(f"Costo total de las llamadas al primer operador: {costo_total_operador1}")
print(f"Costo total de las llamadas al segundo operador: {costo_total_operador2}")
print(f"Costo total de las cuatro llamadas: {costo_total_llamadas}")

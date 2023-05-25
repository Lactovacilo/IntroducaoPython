salario = float(input(("Salário atual (Ex. 1400.50): ")))
aumento = float(input(("Percentual de aumento (Ex. 30): ")))

salarioaumentado = salario * (1 + aumento/100)

print(f"Salário aumentado: {salarioaumentado:.2f}")
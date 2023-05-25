import math

raio = float(input("Raio da lata: "))
altura = float(input("Altura da lata: "))

volume = (math.pi * raio * raio) * altura

print(f"Volume da lata: {volume:.2f}")
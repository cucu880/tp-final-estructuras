2. Estructuras Recursivas
Cálculo Recursivo de Evolución de Poder
El cálculo recursivo debe considerar transformaciones (como Super Saiyajin o Kaioken) 
que multipliquen el nivel de poder tras cada combate.

def calcular_evolucion_poder(nivel_actual, batallas, multiplicador, incremento_base=10):
    if batallas == 0:
        return nivel_actual
    nuevo_nivel = (nivel_actual * multiplicador) + incremento_base
    return calcular_evolucion_poder(nuevo_nivel, batallas - 1, multiplicador, incremento_base)

# Ejemplo de uso
nivel_inicial = 1000
batallas = 3
multiplicador = 1.5  # Ejemplo: transformación Super Saiyajin
print(f"Nivel de poder tras {batallas} batallas: {calcular_evolucion_poder(nivel_inicial, batallas, multiplicador)}")

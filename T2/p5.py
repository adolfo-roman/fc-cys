import random
import math
import matplotlib.pyplot as plt

def generar_mensaje(n):
    return random.randint(0, n - 1)

def simular_birthday_attack(n, umbral=0.99):
    probabilidades = []
    d = 0
    P = 0.0

    while P < umbral:
        mensaje = generar_mensaje(n)

        if mensaje is not None:
            d += 1

        P = 1 - math.exp(-(d * (d - 1)) / (2 * n))
        
        probabilidades.append(P)

    return probabilidades, d

def graficar_resultados(probabilidades, d_final):
    valores_d = range(1, d_final + 1)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(valores_d, probabilidades, label='Probabilidad de colisión (P)', color='blue', linewidth=2)
    
    plt.axhline(y=0.99, color='red', linestyle='--', alpha=0.7, label='Umbral P = 0.99')
    plt.axvline(x=d_final, color='green', linestyle='--', alpha=0.7, label=f'Punto crítico: d = {d_final}')
    plt.scatter([d_final], [probabilidades[-1]], color='black', zorder=5) 
    
    plt.title("Simulación Birthday Attack: Probabilidad de Colisión vs Mensajes Interceptados")
    plt.xlabel("Número de mensajes interceptados (d)")
    plt.ylabel("Probabilidad de colisión (P)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    print(f"P5: Simulación Birthday Attack en RSA")

    n_espacio = int(input("Tamaño del espacio(n): "))
    
    print(f"Tamaño del espacio (n) = {n_espacio}")
    
    probabilidades, d_final = simular_birthday_attack(n_espacio)
    
    print("-" * 40)
    print("Resultados de la simulación:")
    print(f"El umbral de P >= 0.99 se alcanzó.")
    print(f"Número exacto de mensajes interceptados (d) necesarios: {d_final}")
    print("-" * 40)
    
    graficar_resultados(probabilidades, d_final)
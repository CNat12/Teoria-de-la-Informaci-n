import itertools
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def calcular_probabilidades(num_dados):
    """
    Calcula las probabilidades exactas de todas las sumas posibles
    al lanzar 'num_dados' dados.
    Retorna dos listas: sumas y probabilidades.
    """
    combinaciones = list(itertools.product(range(1, 7), repeat=num_dados))
    sumas = [sum(c) for c in combinaciones]
    conteo = Counter(sumas)
    total_combinaciones = len(combinaciones)
    sumas_ordenadas = sorted(conteo.keys())
    probabilidades = [conteo[s] / total_combinaciones for s in sumas_ordenadas]
    return sumas_ordenadas, probabilidades

def graficar_individualmente():
    """
    Muestra 5 gráficas separadas, una para cada cantidad de dados.
    Cada gráfica incluye curvas, puntos y porcentajes.
    """
    colores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    for i, num_dados in enumerate(range(1, 6)):
        sumas, probabilidades = calcular_probabilidades(num_dados)

        # Crear una nueva ventana para cada gráfica
        fig = plt.figure(figsize=(12, 6))

        # Curva suave interpolada
        x = np.linspace(min(sumas), max(sumas), 300)
        y = np.interp(x, sumas, probabilidades)
        plt.plot(x, y, color=colores[i], linewidth=2, label="Curva de probabilidad")

        # Puntos exactos
        plt.scatter(sumas, probabilidades, color=colores[i], marker="o", s=50, label="Probabilidad exacta")

        # Mostrar porcentajes sobre cada punto
        for s, p in zip(sumas, probabilidades):
            plt.text(s, p + 0.002, f"{p:.2%}", ha="center", fontsize=8, rotation=45)

        # Personalizar gráfica
        plt.title(f"Distribución de Probabilidades con {num_dados} Dado(s) 🎲", fontsize=16, fontweight="bold")
        plt.xlabel("Suma de los dados", fontsize=14)
        plt.ylabel("Probabilidad", fontsize=14)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(fontsize=10)
        plt.tight_layout()
        plt.show(block=True)

def graficar_resumen():
    """
    Muestra una gráfica final con todas las distribuciones juntas.
    """
    colores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    plt.figure(figsize=(14, 7))

    for i, num_dados in enumerate(range(1, 6)):
        sumas, probabilidades = calcular_probabilidades(num_dados)

        # Curva suave interpolada
        x = np.linspace(min(sumas), max(sumas), 300)
        y = np.interp(x, sumas, probabilidades)

        # Graficar cada distribución en la misma gráfica
        plt.plot(x, y, color=colores[i], linewidth=2, label=f"{num_dados} dado(s)")

    # Personalizar gráfica final
    plt.title("Comparación de Distribuciones de Probabilidades (1 a 5 Dados)", fontsize=16, fontweight="bold")
    plt.xlabel("Suma de los dados", fontsize=14)
    plt.ylabel("Probabilidad", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=12)
    plt.tight_layout()

    # Mostrar la gráfica final y terminar el programa al cerrarla
    plt.show(block=True)

def main():
    # Mostrar probabilidades exactas en consola
    for num_dados in range(1, 6):
        sumas, probabilidades = calcular_probabilidades(num_dados)
        print(f"\n=== PROBABILIDADES CON {num_dados} DADO(S) ===")
        for s, p in zip(sumas, probabilidades):
            print(f"Suma {s}: {p:.2%}")

    # Mostrar 5 gráficas separadas
    graficar_individualmente()

    # Mostrar la gráfica resumen final
    graficar_resumen()

if __name__ == "__main__":
    main()

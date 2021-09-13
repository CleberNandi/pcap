import datetime
import computa

def main():
    inicio = datetime.datetime.now()
    print(f"Iniciei")
    computa.computar(fim=50_000_000)
    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos")

if __name__ == "__main__":
    main()

"""
Terminou em 12.82 segundos
Terminou em 15.19 segundos
Terminou em 13.31 segundos
Terminou em 10.70 segundos C1
Terminou em 0.00 segundos C1
"""
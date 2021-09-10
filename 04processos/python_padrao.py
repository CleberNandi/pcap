import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor

def main():
    qtde_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matemático com {qtde_cores} cores(s)")

    inicio = datetime.datetime.now()
    
    with ProcessPoolExecutor() as executor:
        for n in range(1, qtde_cores + 1):
            ini = 50_000_000 * (n -1) / qtde_cores
            fim = 50_000_000 * n / qtde_cores
            print(f"Core {n} processando de {ini} até {fim}")
            executor.submit(computar, {"inicio": ini, "fim": fim})
            
    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos")

def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == "__main__":
    main()

"""
Terminou em 12.82 segundos Threads
Terminou em 10.41 segundos processos
Terminou em 1.11 segundos multiprocessos
"""
import datetime
import math
import asyncio

def main():
    print(f"Realizando o processamento matemático de forma assincrona")
    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    # el.run_until_complete(computar(inicio=1, fim=50_000_000))
    tarefa1 = el.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = el.create_task(computar(inicio=10_000_001, fim=20_000_000))
    tarefa3 = el.create_task(computar(inicio=20_000_001, fim=30_000_000))
    tarefa4 = el.create_task(computar(inicio=30_000_001, fim=40_000_000))
    tarefa5 = el.create_task(computar(inicio=40_000_001, fim=50_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas)
            
    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos")

async def computar(fim, inicio=1):
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
Terminou em 12.86 segundos asyncio F1
Terminou em 12.71 segundos asyncio F2
"""
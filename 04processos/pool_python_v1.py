import multiprocessing

def calcula(dado):
    return dado ** 2

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2
    print(f"Tamanho da pool: {tamanho_pool}")
    pool = multiprocessing.Pool(processes=tamanho_pool)
    entradas = list(range(7))
    saida = pool.map(calcula, entradas)

    print(f"Saidas: {saida}")

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
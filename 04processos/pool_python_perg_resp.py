import multiprocessing
from functools import partial
 
tamanho_pool = multiprocessing.cpu_count() * 2
 
pool = multiprocessing.Pool(processes = tamanho_pool)
saidas = pool.map(partial(calcular, a=1, b=2) entradas)
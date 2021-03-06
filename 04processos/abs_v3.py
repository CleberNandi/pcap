import time

from concurrent.futures.thread import ThreadPoolExecutor as Executer#
# from concurrent.futures.process import ProcessPoolExecutor as Executer


def processar():
    print("[", end="", flush=True)
    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)
    print("]", end="", flush=True)

    return 83

if __name__ == "__main__":
    with Executer() as executor:
        future = executor.submit(processar)
    
    print(f"O retorno foi: {future.result()}")
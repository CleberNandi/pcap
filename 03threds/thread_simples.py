import threading # 1
import time

def main():
    th = threading.Thread(target=contar, args=("elefante", 10)) # 2

    th.start() # Adiciona a thread na pool de theads prontas para execução # 3

    print("Podemos fazer qualquer outras coisas no programa enquanto a thread vai executando...")
    print("Cleber Goulsart Nandi" * 2)
    for n in range(1, 50):
        print(f"aqui {n}")
        time.sleep(0.5)

    th.join() # Avisa para ficar aguardando aqui até a thead terminar a execução # 4

    print("Pronto")

def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f"{n} {o_que} (s)")
        time.sleep(1)

if __name__ == "__main__":
    main()

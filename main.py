import time

contador = 0

try:
    while True:
        contador += 1
        print(f"Contador: {contador}")
        time.sleep(1)  # espera 1 segundo entre cada número
except KeyboardInterrupt:
    print(f"\nContador detenido en {contador}.")
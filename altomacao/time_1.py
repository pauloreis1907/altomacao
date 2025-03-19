import time

def lembrente_beber_agua(intervalo_minutos):
    contador = 1
    while True:
        print(f'Tempo encerrado (lembrete{contador})')
        contador += 1
        time.sleep(intervalo_minutos*5)
lembrente_beber_agua(1)
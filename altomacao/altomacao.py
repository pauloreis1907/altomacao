import random

def sorteio_aluno():
    alunos = [
        'Jhorlen','vini','raissa',
        'Gael','deise','fatima'
    ]
    escolhar = random.choice(alunos)
    print('o aluno escolhido foi:',escolhar)
sorteio_aluno()
# занести значеня в список і вивести парні або непарні

def numbers():
    parni = []
    nieparni = []
    spusok = []
    for i in range(5):
        spusok.append(int(input('enter value: ')))
    for value in spusok:
        if value % 2 == 0:
            parni.append(value)
        else:
            nieparni.append(value)
    print(f'parni: {parni}, nieparni: {nieparni}')

numbers()
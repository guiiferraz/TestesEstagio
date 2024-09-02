phrase = str(input('Digite uma frase: '))
phrasereverse = ''

for e in range(len(phrase)-1, -1, -1):
    phrasereverse += phrase[e]
print(phrasereverse)

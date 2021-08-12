from random import randint
computador = randint(0,10)
tentativas = 0
print('Olá, sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
resposta = 11
while computador!=resposta:
    resposta = int(input('Qual seu palpite? '))
    if computador > resposta:
        print('Mais... Tente outra vez')
        tentativas += 1
    elif computador < resposta:
        print('Menos... Tente outra vez')
        tentativas += 1
print('Acertou com {} tentativas. Parabéns'.format(tentativas))
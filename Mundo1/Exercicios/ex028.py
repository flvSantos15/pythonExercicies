from random import randint

num = randint(0, 5)
n = int(input('Digite um numero entre 0 e 5: '))
if num == n:
  print('Você acertou!')
else:
  print('Você errou!')
print(f'O numero que pensei foi {num}')
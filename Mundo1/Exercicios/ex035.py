r1 = float(input('Seguimento: '))
r2 = float(input('Seguimento: '))
r3 = float(input('Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Podem formar um triângulo')
else:
  print('Não podem formar um triângulo')
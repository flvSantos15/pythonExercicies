sal = float(input('Salario (ex: 1035) R$? '))
if sal >= 1250:
  nsal = sal + (sal * 10 / 100)
  print(f'Seu novo salario é de R$ {nsal:.2f} reais')
else:
  nsal = sal + (sal * 15 / 100)
  print(f'Seu novo salario é de R$ {nsal:.2f} reais')
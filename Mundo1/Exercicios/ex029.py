v = float(input('Velocidade do carro: '))
if v > 80:
  multa = (v - 80) * 7
  print('Você foi multado!')
  print(f'Sua multa é de R${multa:.2f} reais')
print('Tudo ok')
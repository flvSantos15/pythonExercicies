km = float(input('Quantos km? '))
if km <= 200:
  v = km * 0.5
  print(f'O valor total será de R$ {v:.2f} reais')
else:
  v = km * 0.45
  print(f'O valor total será de R$ {v:.2f} reais')
print('Tenha uma boa viagem')
n1 = int(input('Numero: '))
n2 = int(input('Numero: '))
n3 = int(input('Numero: '))

if n1 > n2:
  if n1 > n3:
    maior = n1
if n2 > n1:
  if n2 > n3:
    maior = n2
if n3 > n1:
  if n3 > n2:
    maior = n3

if n1 < n2:
  if n1 < n3:
    menor = n1
if n2 < n1:
  if n2 < n3:
    menor = n2
if n3 < n1:
  if n3 < n2:
    menor = n3
print(f'O maior é {maior}')
print(f'O menor é {menor}')
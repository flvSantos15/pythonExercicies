frase = str(input('Frase: ')).strip().upper()
print(f'Letra A {frase.count("A")} vezes')
print(f'Primeira posição: {frase.index("A") + 1}')
print(f'Ultima posição: {frase.rfind("A") + 1}')
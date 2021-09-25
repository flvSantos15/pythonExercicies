from math import cos, sin, tan, radians


ang = float(input('Angulo: '))

seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'Seno {seno:.2f}')
print(f'Cosseno {coseno:.2f}')
print(f'Tangente {tangente:.2f}')

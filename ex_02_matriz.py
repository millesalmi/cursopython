mat = [0,0,0], [0,0,0], [0,0,0]
spar = maior = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))
print('~'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
        if mat[l][c] % 2 == 0:
            spar += mat[l][c]
    print()
print('~'*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += mat[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0,3):
    if c == 0:
        maior = mat[1][c]
    elif mat[1][c] > maior:
        maior = mat[1][c]
print(f'O maior valor da segunda linha é {maior}.')
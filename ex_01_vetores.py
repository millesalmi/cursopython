listanum = []
mais = 0
menos = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mais = menos = listanum[c]
    else:
        if listanum[c] > mais:
            mais = listanum[c]
        if listanum[c] < menos:
            menos = listanum[c]

print('=-' *30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mais} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mais:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menos} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menos:
        print(f'{i}... ', end='')
print()
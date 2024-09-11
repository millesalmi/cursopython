def add_aluno():
    with open('alunos.txt', 'a') as file:
        nome = input("Entre com o nome do aluno: ")
        serie = input("Entre com a série que o aluno estuda: ")
        file.write(f'{nome}: {serie}\n')
        print('Aluno cadastrado com sucesso!')

def ver_aluno():
    try:
        with open('alunos.txt', 'r') as file:
            alunos = file.readlines()
            if alunos:
                for aluno in alunos:
                    print(aluno.strip())
            else:
                print('Aluno não encontrado.')
    except FileNotFoundError:
        print('Aluno não encontrado.')

def buscar_aluno():
    nome_buscar = input('Entre com o nome do aluno que deseja encontrar: ')
    try:
        with open('alunos.txt', 'r') as file:
            found = False
            for line in file:
                nome, serie = line.strip().split(': ')
                if nome.lower() == nome_buscar.lower():
                    print(f'{nome}: {serie}')
                    found = True
                    break

            if not found:
                print(f'Aluno {nome_buscar} não encontrado.')
    except FileNotFoundError:
        print('Nenhum aluno encontrado. ')

def main():
    while True:
        print('\n1. Adicionar novo aluno')
        print('2. Ver todos os alunos')
        print('3. Encontrar um aluno pelo nome')
        print('4. Sair')
        escolha = int(input('Sua opção: '))

        if escolha == 1:
            add_aluno()
        elif escolha == 2:
            ver_aluno()
        elif escolha == 3:
            buscar_aluno()
        elif escolha == 4:
            print('Saindo...')
            break
        else:
            print('Escolha inválida, tente novamente.')
if __name__ == "__main__":
    main()
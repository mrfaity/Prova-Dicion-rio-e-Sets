alunos = {} 
while True:
    print("Escolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso.")

    elif escolha == "2":
        matricula = input("Digite o número de matrícula a ser removido: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno removido.")
        else:
            print("Aluno não encontrado.")

    elif escolha == "3":
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

    elif escolha == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

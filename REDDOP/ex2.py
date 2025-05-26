tarefas = []

while True:
    print("1 - Cadastrar tarefa")
    print("2 - Alterar status da tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        data = input("Data de vencimento (dd/mm/aaaa): ")
        status = "Pendente"
        tarefas.append([titulo, descricao, data, status])
        print("Tarefa cadastrada!\n")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.\n")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1} - {tarefa[0]} (Status: {tarefa[3]})")
            num = int(input("Número da tarefa para alterar status: ")) - 1
            if num < 0 or num >= len(tarefas):
                print("Número inválido.\n")
            else:
                print("Status disponíveis:")
                print("1 - Pendente")
                print("2 - Em Andamento")
                print("3 - Concluída")
                novo_status = input("Escolha o status: ")
                if novo_status == "1":
                    tarefas[num][3] = "Pendente"
                elif novo_status == "2":
                    tarefas[num][3] = "Em Andamento"
                elif novo_status == "3":
                    tarefas[num][3] = "Concluída"
                else:
                    print("Opção inválida.")
                print("Status atualizado!\n")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.\n")
        else:
            print("Quer filtrar por status? (s/n)")
            filtra_status = input().lower()
            status_filtro = None
            if filtra_status == "s":
                print("Escolha o status para filtrar:")
                print("1 - Pendente")
                print("2 - Em Andamento")
                print("3 - Concluída")
                opc_status = input()
                if opc_status == "1":
                    status_filtro = "Pendente"
                elif opc_status == "2":
                    status_filtro = "Em Andamento"
                elif opc_status == "3":
                    status_filtro = "Concluída"

            print("Quer filtrar por data de vencimento? (s/n)")
            data_s = input().lower()
            data = None
            if data_s == "s":
                data_filtro = input("Digite a data (dd/mm/aaaa): ")

            print()
            for tarefa in tarefas:
                if status_filtro and tarefa[3] != status_filtro:
                    continue
                if data and tarefa[2] != data:
                    continue
                print(f"Título: {tarefa[0]}")
                print(f"Descrição: {tarefa[1]}")
                print(f"Data de vencimento: {tarefa[2]}")
                print(f"Status: {tarefa[3]}")
                print("-----")
            print()

    elif opcao == "4":
        break

    else:
        print("Opção inválida")

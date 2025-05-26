categoria = []
produto = []

cat_id = 1
prod_id = 1

while True:
    print("1 - Cadastrar categoria")
    print("2 - Cadastrar produto")
    print("3 - Listar produtos")
    print("4 - Buscar produto por ID")
    print("5 - Deletar uma categoria")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: \n"))

    if opcao == 1:
        cat_nome = input("Nome da categoria: \n")
        existe = 0

        for c in categoria:
            if c[1] == cat_nome:
                existe += 1

        if existe != 0:
            print("A categoria já existe!\n")
        else:
            categoria.append([cat_id, cat_nome])
            print(f"ID da categoria {cat_nome} é: {cat_id}\n")
            cat_id += 1

    elif opcao == 2:
        prod_nome = input("Nome do produto: \n")
        cat_escolhida = int(input("ID da categoria: \n"))
        existe = 0

        for c in categoria:
            if c[0] == cat_escolhida:
                existe += 1

        if existe != 0:
            produto.append([prod_id, prod_nome, cat_escolhida])
            print(f"ID do produto: {prod_id}\n")
            prod_id += 1
        else:
            print("Categoria não encontrada\n")

    elif opcao == 3:
        print("Lista de produtos: \n")
        for p in produto:
            cat_nome = "Desconhecida"
            for c in categoria:
                if c[0] == p[2]:
                    cat_nome = c[1]
            print(f"ID: {p[0]}, Nome: {p[1]}, Categoria: {cat_nome}\n")

    elif opcao == 4:
        busca_id = int(input("ID do produto desejado: \n"))
        existe = 0

        for p in produto:
            if p[0] == busca_id:
                existe += 1
                cat_nome = "Desconhecida"
                for c in categoria:
                    if c[0] == p[2]:
                        cat_nome = c[1]
                print(f"ID: {p[0]}, Nome: {p[1]}, Categoria: {cat_nome}\n")

        if existe == 0:
            print("Produto não encontrado\n")

    elif opcao == 5:
        cat_del = int(input("ID da categoria que deseja deletar: \n"))
        s_prod = 0

        for p in produto:
            if p[2] == cat_del:
                s_prod += 1
        if s_prod != 0:
            print("Não é possivel deletar, pois existem produtos na categoria.\n")
        else:
            existe = 0
            for c in categoria:
                if c[0] == cat_del:
                    categoria.pop(categoria.index(c))
                    existe += 1
                    print("Categoria deletada com sucesso!\n")
                    break
            if existe == 0:
                print("Categoria não encontrada.\n")

    elif opcao == 0:
        break
    else:
        print("Escolha uma opção valida!\n")

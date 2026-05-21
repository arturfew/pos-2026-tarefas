import users_wrapper as api

rodando = True

while rodando:

    print("\n------ O que desejas fazer? ------")
    print("1 - Ver todos os usuarios")
    print("2 - Buscar um usuario com o ID")
    print("3 - Cadastrar novo usuario")
    print("4 - Atualizar usuario existente")
    print("5 - Deletar usuario")
    print("0 - Sair")

    escolha = input("\nOpcao: ").strip()

    if escolha == "1":

        print("\nBuscando usuarios...")
        lista = api.list()

        if lista:
            print(f"\n{len(lista)} usuarios encontrados:\n")
            for pessoa in lista:
                print(f"  {pessoa['id']:>2}  {pessoa['name']:<25}  {pessoa['email']}")
        else:
            print("Nenhum usuario encontrado.")

    elif escolha == "2":

        try:
            codigo = int(input("\nID do usuario: "))
        except ValueError:
            print("ID invalido. Digite um numero.")
            continue

        usuario = api.read(codigo)

        if usuario:
            print("\n----- Dados do usuario -----")
            print(f"Nome     : {usuario['name']}")
            print(f"Username : {usuario['username']}")
            print(f"Email    : {usuario['email']}")
            print(f"Telefone : {usuario['phone']}")
            print(f"Site     : {usuario['website']}")

            end = usuario.get("address", {})
            if end:
                print(f"\nEndereco : {end.get('street', '')}, {end.get('city', '')} - {end.get('zipcode', '')}")

            emp = usuario.get("company", {})
            if emp:
                print(f"Empresa  : {emp.get('name', '')}")
        else:
            print("Usuario nao encontrado.")

    elif escolha == "3":

        print("\nPreencha os dados do novo usuario:\n")

        novo = {
            "name":     input("  Nome: "),
            "username": input("  Username: "),
            "email":    input("  Email: "),
            "phone":    input("  Telefone: "),
            "website":  input("  Website: "),
        }

        confirma = input("\nCadastrar este usuario? (s/n): ").strip().lower()

        if confirma == "s":
            resultado = api.create(novo)
            if resultado:
                print(f"Usuario '{resultado['name']}' cadastrado com sucesso.")
            else:
                print("Erro ao cadastrar usuario.")
        else:
            print("Cadastro cancelado.")

    elif escolha == "4":

        try:
            codigo = int(input("\nID do usuario a editar: "))
        except ValueError:
            print("ID invalido. Digite um numero.")
            continue

        usuario = api.read(codigo)

        if not usuario:
            print("Usuario nao encontrado.")
            continue

        print(f"\nEditando: {usuario['name']}")
        print("Deixe em branco para manter o valor atual.\n")

        atualizado = {
            "name":     input(f"  Nome [{usuario['name']}]: ")     or usuario["name"],
            "username": input(f"  Username [{usuario['username']}]: ") or usuario["username"],
            "email":    input(f"  Email [{usuario['email']}]: ")   or usuario["email"],
            "phone":    input(f"  Telefone [{usuario['phone']}]: ") or usuario["phone"],
            "website":  input(f"  Website [{usuario['website']}]: ") or usuario["website"],
        }

        resultado = api.update(codigo, atualizado)

        if resultado:
            print(f"Usuario '{resultado['name']}' atualizado com sucesso.")
        else:
            print("Erro ao atualizar usuario.")

    elif escolha == "5":

        try:
            codigo = int(input("\nID do usuario a deletar: "))
        except ValueError:
            print("ID invalido. Digite um numero.")
            continue

        usuario = api.read(codigo)

        if not usuario:
            print("Usuario nao encontrado.")
            continue

        print(f"\nUsuario selecionado: {usuario['name']} ({usuario['email']})")
        confirma = input("Tem certeza que deseja deletar? (s/n): ").strip().lower()

        if confirma == "s":
            ok = api.delete(codigo)
            if ok:
                print("Usuario deletado com sucesso.")
            else:
                print("Erro ao deletar usuario.")
        else:
            print("Operacao cancelada.")

    elif escolha == "0":
        print("\nAte mais!")
        rodando = False

    else:
        print("Opcao invalida. Tente novamente.")
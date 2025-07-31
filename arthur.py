def cadastrar():
    cartao = input("Digite o número do cartão: ")
    nome = input("Digite o nome do titular: ")
    limite = float(input("Digite o limite do cartão: "))
    print(f"Cartão {cartao} cadastrado com sucesso!")

while True:
    print("\nMenu:")
    print("1. Cadastrar Cartão")
    print("2. verificar saldo")
    print("3. extrair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        print("Verificando saldo...")
    elif opcao == '3':
        print("Extraindo dados...")
        # Aqui você pode adicionar a lógica para extrair dados do cartão
    elif opcao.lower() == 'sair':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
  
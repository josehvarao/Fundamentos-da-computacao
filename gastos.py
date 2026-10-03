totalDespesa = 0
saldo = 0
orcamento = 0

while True:
    print("==================")
    print("1 - Renda Mensal")
    print("2 - Despesas")
    print("3 - Orçamento")
    print("4 - Extrato")
    print("5 - Sair")
    print("==================")

    opcao = int(input("Digite uma opção(1-5): "))

    match opcao:
        case 1:
            rendaMensal = float(input("Digite sua renda: "))
            saldo = rendaMensal

        case 2:
            nomeDespesa = input("Digite o nome da despesa: ")
            valorDespesa = float(input("Digite o valor da despesa: "))
            saldo = saldo - valorDespesa

        case 3:
            print("Saldo atual: ", saldo)
            if valorDespesa > valorOrcamento:
                diferencaDespesaOrcamento = valorDespesa - valorOrcamento 
                print("Você está a",diferencaDespesaOrcamento,"R$ acima do seu orçamento")

            elif valorDespesa == valorOrcamento:
                print("Você está no limite do seu orçamento")

            elif valorDespesa < valorOrcamento:
                diferencaDespesaOrcamento = valorDespesa - valorOrcamento 
                print("Você está a",diferencaDespesaOrcamento,"R$ abaixo do seu orçamento")
            else:
                print("Indetermiado")

        case 4:
            print("A renda mensal é R$ ", saldo)
            input("Digite qualquer tecla para voltar")

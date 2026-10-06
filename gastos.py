totalDespesa = 0
descricaoDespesa = []
quantidadeDespesa = 0
saldo = 0

rendaMensal = float(input("Digite sua renda: R$"))
saldo = rendaMensal
orcamento = float(input("Digite o seu orçamento: R$"))
    

while True:
    print("==================")
    print("1 - Despesas")
    print("2 - Orçamento")
    print("3 - Extrato")
    print("4 - Sair")
    print("==================")

    opcao = int(input("Digite uma opção(1-4): "))

    match opcao:
        case 1:
            nomeDespesa = str(input("Digite o nome da despesa: "))
            valorDespesa = float(input("Digite o valor da despesa: R$"))
            saldo = saldo - valorDespesa
            
            descricaoDespesa.append(nomeDespesa)
            totalDespesa += valorDespesa
            quantidadeDespesa += 1

        case 2:
            print("Saldo atual: ", saldo)
            if orcamento:
               print(orcamento) 

            elif valorDespesa > orcamento:
                diferencaDespesaOrcamento = orcamento - valorDespesa 
                print("Você está a",diferencaDespesaOrcamento,"R$ acima do seu orçamento")

            elif valorDespesa == valorOrcamento:
                print("Você está no limite do seu orçamento")

            elif valorDespesa < valorOrcamento:
                diferencaDespesaOrcamento = orcamento - valorDespesa
                print("Você está a",diferencaDespesaOrcamento,"R$ abaixo do seu orçamento")
            else:
                print("Indetermiado")

        case 3:
            print("==================")
            print("A renda mensal é R$ ",rendaMensal)
            print("O seu orçamento é de: R$",orcamento)
            print("O total de despesas registradas é de: R$",totalDespesa)
            print("Quantidade de despesas: ",quantidadeDespesa)
            for indice, item in enumerate(descricaoDespesa):
                print(indice, "-", item,)
            print("==================")
            
            input("Digite qualquer tecla para voltar")
            
        case 4:
             print("Saindo...")
             menu = False
        case _:
            print("Inválido, digite um número de 1-4")

totalDespesa = 0
descricaoDespesa = []
quantidadeDespesa = 0

rendaMensal = float(input("Digite sua renda: R$"))
saldo = rendaMensal
orcamento = float(input("Digite o seu orçamento: R$"))

menu = True
while menu:
    print("==================")
    print("1 - Despesas")
    print("2 - Orçamento")
    print("3 - Extrato")
    print("4 - Sair")
    print("==================")

    opcao = int(input("Digite uma opção(1-4): "))
    match opcao:
        case 1:
            while True:
             nomeDespesa = str(input("Digite o nome da despesa: "))
             valorDespesa = float(input("Digite o valor da despesa: R$"))
             
             saldo = saldo - valorDespesa
             descricaoDespesa.append((nomeDespesa, valorDespesa))
             totalDespesa += valorDespesa
             quantidadeDespesa += 1
             continuar = str(input('Deseja continuar? Digite qualquer tecla. Deseja encerrar? Digite (1):'))
             if continuar == '1':
                break
             else:
                print('Continuando...')

        case 2:
            print("Saldo atual: R$", saldo)
            print("Orçamento: R$", orcamento)

            if totalDespesa > orcamento:
                excedente = totalDespesa - orcamento   
                print("Fora do orçamento! Você está a R$",excedente," acima do seu orçamento")

            elif totalDespesa == orcamento:
                print("Você está no limite do seu orçamento")

            elif totalDespesa < orcamento:
                diferencaDespesaOrcamento = orcamento - totalDespesa
                print("Dentro do orçamento! Você está a R$",diferencaDespesaOrcamento," abaixo do seu orçamento")
            else:
                print("Indetermiado")

        case 3:
            print("==================")
            print("A renda mensal é R$",rendaMensal)
            print("O seu orçamento é de: R$",orcamento)
            print("O total de despesas registradas é de: R$",totalDespesa)
            print("Quantidade de despesas: ",quantidadeDespesa)
            for indice, (item, valor) in enumerate(descricaoDespesa):
                print(indice, "-", item, ": R$", valor)
            print("==================")
            
            input("Digite qualquer tecla para voltar")
            
        case 4:
             print("Saindo...")
             menu = False
        case _:
            print("Inválido, digite um número de 1-4")

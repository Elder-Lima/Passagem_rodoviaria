lugares1 = [1,2,3,4]
lugares2 = [1,2,3,4]
lugares3 = [1,2,3,4]
lugares4 = [1,2,3,4]

lucro = 0
passagem = 200

while True:

    print(40 * '=')
    print('      Viação VaptVupt')
    print('1- Venda de passagem')
    print('2- Ver poltronas')
    print('3- Finalizar Vendas')
    print('4- Encerrar / sair do programa')
    opcao = int(input(''))
    print(40 * '=')

    if opcao == 1:
        while  True:
            print('Lugares: ')
            print(f'Fileira 1: {lugares1}')
            print(f'Fileira 2: {lugares2}')
            print(f'Fileira 3: {lugares3}')
            print(f'Fileira 4: {lugares4}')
            fileira = int(input('Selecione a fileira: '))

            if fileira == 1:
                lugar = int(input('Informe o numero do lugar: '))
                print(40 * '=')

                if not lugar in lugares1:
                    print('Esse lugar não esta disponivel!')
                    break

                print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                idade = int(input('Infome a Idade: '))
                if idade < 5 or idade > 65:
                    desconto = passagem * 50 / 100
                    total = passagem - desconto
                    print(f'Preço da Passagem R$ {total:.2f}.')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares1.remove(lugar)
                        lucro = lucro + total
                        print(40 * '=')
                        break
                    else: 
                        break
                else:
                    print(f'Preço da Passagem: {passagem}')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares1.remove(lugar)
                        lucro = lucro + passagem
                        print(40 * '=')
                        break
                    else:
                        break

            if fileira == 2:
                lugar = int(input('Informe o numero do lugar: '))
                print(40 * '=')

                if not lugar in lugares2:
                    print('Esse lugar não esta disponivel!')
                    break

                print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                idade = int(input('Infome a Idade: '))
                if idade < 5 or idade > 65:
                    desconto = passagem * 50 / 100
                    total = passagem - desconto
                    print(f'Preço da Passagem R$ {total:.2f}.')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares2.remove(lugar)
                        lucro = lucro + total
                        print(40 * '=')
                        break
                    else: 
                        break
                else:
                    print(f'Preço da Passagem: {passagem}')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares2.remove(lugar)
                        lucro = lucro + passagem
                        print(40 * '=')
                        break
                    else:
                        break

            if fileira == 3:
                lugar = int(input('Informe o numero do lugar: '))
                print(40 * '=')

                if not lugar in lugares3:
                    print('Esse lugar não esta disponivel!')
                    break

                print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                idade = int(input('Infome a Idade: '))
                if idade < 5 or idade > 65:
                    desconto = passagem * 50 / 100
                    total = passagem - desconto
                    print(f'Preço da Passagem R$ {total:.2f}.')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares3.remove(lugar)
                        lucro = lucro + total
                        print(40 * '=')
                        break
                    else: 
                        break
                else:
                    print(f'Preço da Passagem: {passagem}')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares3.remove(lugar)
                        lucro = lucro + passagem
                        print(40 * '=')
                        break
                    else:
                        break
                  

            if fileira == 4:
                lugar = int(input('Informe o numero do lugar: '))
                print(40 * '=')

                if not lugar in lugares4:
                    print('Esse lugar não esta disponivel!')
                    break

                print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                idade = int(input('Infome a Idade: '))
                if idade < 5 or idade > 65:
                    desconto = passagem * 50 / 100
                    total = passagem - desconto
                    print(f'Preço da Passagem R$ {total:.2f}.')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares4.remove(lugar)
                        lucro = lucro + total
                        print(40 * '=')
                        break
                    else: 
                        break
                else:
                    print(f'Preço da Passagem: {passagem}')
                    opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                    if opcao == 1:
                        print('CONFIRMADO!')
                        lugares4.remove(lugar)
                        lucro = lucro + passagem
                        print(40 * '=')
                        break
                    else:
                        break

            if fileira > 4:
                print('Essa fileira não Existe')
                break

        


    elif opcao == 2:
        while True: 
            print('Lugares: ')
            print(f'Fileira 1: {lugares1}')
            print(f'Fileira 2: {lugares2}')
            print(f'Fileira 3: {lugares3}')
            print(f'Fileira 4: {lugares4}')
            
            opcao2 = int(input('Deseja Comprar alguma passagem? 1-SIM / 2-NÃO'))
            if opcao2 == 1:
                
                

                fileira = int(input('Selecione a fileira: '))
                if fileira >= 5:
                    print('Essa Fileira não Existe!!')
                    break

                if fileira == 1:
                    lugar = int(input('Informe o numero do lugar: '))
                    print(40 * '=')

                    if not lugar in lugares1:
                        print('Esse lugar não esta disponivel!')
                        break

                    print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                    idade = int(input('Infome a Idade: '))
                    if idade < 5 or idade > 65:
                        desconto = passagem * 50 / 100
                        total = passagem - desconto
                        print(f'Preço da Passagem R$ {total:.2f}.')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares1.remove(lugar)
                            lucro = lucro + total
                            print(40 * '=')
                            break
                        else: 
                            break
                    else:
                        print(f'Preço da Passagem: {passagem}')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares1.remove(lugar)
                            lucro = lucro + passagem
                            print(40 * '=')
                            break
                        else:
                            break
                            



                if fileira == 2:
                    lugar = int(input('Informe o numero do lugar: '))
                    print(40 * '=')

                    if not lugar in lugares2:
                        print('Esse lugar não esta disponivel!')
                        break

                    print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                    idade = int(input('Infome a Idade: '))
                    if idade < 5 or idade > 65:
                        desconto = passagem * 50 / 100
                        total = passagem - desconto
                        print(f'Preço da Passagem R$ {total:.2f}.')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares2.remove(lugar)
                            lucro = lucro + total
                            print(40 * '=')
                            break
                        else:
                            break
                    else:
                        print(f'Preço da Passagem: {passagem}')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares2.remove(lugar)
                            lucro = lucro + passagem
                            print(40 * '=')
                            break
                        else:
                            break
                        

                if fileira == 3:
                    lugar = int(input('Informe o numero do lugar: '))
                    print(40 * '=')

                    if not lugar in lugares3:
                        print('Esse lugar não esta disponivel!')
                        break

                    print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                    idade = int(input('Infome a Idade: '))
                    if idade < 5 or idade > 65:
                        desconto = passagem * 50 / 100
                        total = passagem - desconto
                        print(f'Preço da Passagem R$ {total:.2f}.')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares3.remove(lugar)
                            lucro = lucro + total
                            print(40 * '=')
                            break
                        else:
                            break
                    else:
                        print(f'Preço da Passagem: {passagem}')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares3.remove(lugar)
                            lucro = lucro + passagem
                            print(40 * '=')
                            break
                        else:
                            break    

                if fileira == 4:
                    lugar = int(input('Informe o numero do lugar: '))
                    print(40 * '=')

                    if not lugar in lugares4:
                        print('Esse lugar não esta disponivel!')
                        break

                    print('Crianças (<5 anos) E idosos (>65 anos) pagam apenas 50% da passagem')
                    idade = int(input('Infome a Idade: '))
                    if idade < 5 or idade > 65:
                        desconto = passagem * 50 / 100
                        total = passagem - desconto
                        print(f'Preço da Passagem R$ {total:.2f}.')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))   
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares4.remove(lugar)
                            lucro = lucro + total
                            print(40 * '=')
                            break
                        else: 
                            break
                    else:
                        print(f'Preço da Passagem: R$ {passagem}')
                        opcao = int(input('Deseja Confirmar? 1-SIM / 2-NAO'))
                        if opcao == 1:
                            print('CONFIRMADO!')
                            lugares4.remove(lugar)
                            lucro = lucro + passagem
                            print(40 * '=')
                            break
                        else:
                            break
            else:
                break                

    elif opcao == 3:
        quant1 = len(lugares1)
        quant2 = len(lugares2)
        quant3 = len(lugares3)
        quant4 = len(lugares4)
        soma = quant1 + quant2 + quant3 + quant4

        if soma <= 7:
            print('Viagem Confirmada!')
            print(f'Faturamento Total das Vendas: R$ {lucro:.2f}')
            break
        elif soma >= 8:
            print('Viagem Cancelada!')
            print('Menos de 50% dos lugares foram vendidos')
            print(f'Faturamneto Total das Vendas: R$ {lucro:.2f}')
            break
            
    elif opcao == 4:
        break

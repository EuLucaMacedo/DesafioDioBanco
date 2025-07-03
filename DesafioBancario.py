
sacar = 0
saldo = 0
deposito = 0
quanti_saque = 0
extrato = ''


while True:
    menu = input('''
          Banco DIO  
                       
         [ 1 ] SACAR
         [ 2 ] DEPOSITAR
         [ 3 ] EXTRATO
         [ 4 ] Sair        
                 
    Escolha uma das Opções: ''')
    print('=' * 50)
    print('')

    if menu == '1':
        sacar = float(input('Digite o Valor do Saque: '))
        if sacar > saldo:
            print('Saldo Indisponivel')
        
        elif sacar > 500:
            print('Limite Máximo por Saque de R$ 500,00')

        elif quanti_saque >= 3:
            print('Execedeu o Limite de Saques Diários!')

        else:
            print(f'Saque de R${sacar} autorizado')
            extrato += f'Saque: R${sacar:.2f}'
            saldo -= sacar
            quanti_saque += 1

        print('=' * 50) 


    elif menu == '2':
        deposito = float(input('Digite o Valor do Deposito: '))

        if deposito < 0:
            print('Valor Inválido!')
        else:
            saldo += deposito
            print(f'Deposito de R${deposito} realizado com Sucesso!')
            print(f'Saldo Final: R${saldo}')
            extrato += f'Depósito: R${deposito:.2f}'
        print('=' * 50)    
            
    elif menu == '3':
        print("\n================ EXTRATO ================")
        print(f'Saldo em conta: R${saldo:.2f}')
        print('Não foram Realizadas Movimentações!' if not extrato else extrato)
        print('=' * 50)

    elif menu == '4':
        break

    else:
        print('⚠️ Opção Invalida! Tente Novamente!')

print('🏦 Obrigado por usar o Banco DIO!')
        
#Nome: Breno Souza do Nascimento
#Data: 31/10/2018

def Tabela(produto,preco,qt,i):
    """Recebe o produto,seu preço e a quantidade que tem no estoque, e os imprime"""
    print('{} - {:<20}'.format(i,produto),end="")
    print('- R${:0.2f}'.format(preco)) if qt > 0 else print('Indisponível')
                                                                                                     

def barra():
    print('*' * 37)

def Pedido():
    """ Retorna qual produto o usuario escolheu"""
    pedido = input('Escolha seu produto: ')
    if pedido != '1' and pedido !='2' and pedido !='3' and pedido !='4' and pedido !='5':
        print('Produto Inválido!')
        return Pedido()
    elif pedido == '1' or pedido == '2' or pedido == '3' or pedido == '4' or pedido == '5':
        pedido = int(pedido)
        if 0 < pedido <=5:
            return pedido
        else:
            pedido()
            
def EntradaDinheiro(valor, d=0):
    """ Recebe o dinheiro do usuário,ate que o mesmo consiga pagar o produto"""
    dinheiro = float(input('Coloque o dinheiro: '))
    if dinheiro + d >= valor:
        return dinheiro + d
    else:
        return EntradaDinheiro(valor,dinheiro +d)

def imprimeTroco(qt,cedula,i=1):
    """Imprime a cédula ou moeda em uma certa quantidade de vez, que é passada como parâmetro"""
    if i <= qt:
        print('R${:0.2f}'.format(cedula))
        imprimeTroco(qt,cedula, i+1)
        
def Troco(valor,div=100):
    """Já recebe o valor do troco, Calcula quantas notas ou moedas serão necessárias e depois
    Chama a função imprimeTroco"""
    qt = valor//div
    if qt > 0:        
        valor = round(valor - (qt * div),2)
        imprimeTroco(qt,div)
    if div == 100:
        div = 50
    elif div == 50:
        div = 20
    elif div == 20:
        div = 10
    elif div == 10:
        div = 5
    elif div == 5:
        div = 2
    elif div == 2:
        div =1
    elif div == 1:
        div = 0.5
    elif div == 0.5:
        div = 0.25
    elif div == 0.25:
        div = 0.10
    elif div == 0.10:
        div = 0.05
    elif div == 0.05:
        div = 0.01
    if valor > 0:
        return Troco(valor,div)
    
    
def Maquina(a,b,c,d,e):
    """ Função Principal, recebe como parâmetros a quantidade de cada produto,
        Essa função tem o nome do produto e seu respectivo preço e a quantidade no estoque"""
    if a > 0 or b > 0 or c > 0 or d > 0 or e >0:
        ############ "Estoque" #############
        #Produto 1
        produto1 = 'Pizza' 
        precop1 = 5.65
        qt1 = a

        #Produto 2
        produto2 = 'Sorvete'
        precop2 = 6.80
        qt2 = b

        #Produto 3
        produto3 = 'Refrigerante'
        precop3 = 3.25
        qt3 = c
        
        #Produto 4
        produto4 = 'Batata Tuple'
        precop4 = 2.25
        qt4 = d
        
        #Produto 5
        produto5 = 'Chocolate'
        precop5 = 4.20
        qt5 = e



        barra()
        Tabela(produto1,precop1, qt1,i=1)
        Tabela(produto2,precop2, qt2,i=2)
        Tabela(produto3,precop3, qt3,i=3)
        Tabela(produto4,precop4, qt4,i=4)
        Tabela(produto5,precop5, qt5,i=5)
        barra()

        pedido = Pedido()
              
        if pedido == 1:
            if qt1 > 0:
                print('\nVocê escolheu: {}\nPreço: R${:0.2f}\n'.format(produto1,precop1))
                dinheiro = EntradaDinheiro(precop1)
                print('\nValor pago: R${:0.2f}'.format(dinheiro))
                qt1 -= 1
                troco = dinheiro - precop1
                if troco >0:
                    print('Troco: R${:0.2f}\n'.format(troco))
                    print('Pegue seu troco:')
                    Troco(round(troco,2))
            else:
                print('Desculpe, mas a {} está indisponível.'.format(produto1))
                
        elif pedido == 2:
            if qt2 > 0:
                print('\nVocê escolheu: {}\nPreço: R${:0.2f}\n'.format(produto2,precop2))
                dinheiro = EntradaDinheiro(precop2)
                print('\nValor pago: R${:0.2f}'.format(dinheiro))
                qt2 -= 1
                troco = dinheiro - precop2
                if troco > 0:
                    print('Troco: R${:0.2f}\n'.format(troco))
                    print('Pegue seu troco:')
                    Troco(round(troco,2))
            else:
                print('Desculpe, mas o {} está indisponível.'.format(produto2))

        elif pedido == 3:
            if qt3 > 0:
                print('\nVocê escolheu: {}\nPreço: R${:0.2f}\n'.format(produto3,precop3))
                dinheiro = EntradaDinheiro(precop3)
                print('\nValor pago: R${:0.2f}'.format(dinheiro))
                qt3 -= 1
                troco = dinheiro - precop3
                if troco > 0:
                    print('Troco: R${:0.2f}\n'.format(troco))
                    print('Pegue Seu Troco:')
                    Troco(round(troco,2))
            else:
                print('Desculpe, mas a {} está indisponível.'.format(produto3))
        elif pedido == 4:
            if qt4 > 0:
                print('\nVocê escolheu: {}\nPreço: R${:0.2f}\n'.format(produto4,precop4))
                dinheiro = EntradaDinheiro(precop4)
                print('\nValor pago: R${:0.2f}'.format(dinheiro))
                qt4 -= 1
                troco = dinheiro - precop4
                if troco >0:
                    print('Troco: R${:0.2f}\n'.format(troco))
                    print('Pegue Seu Troco:')
                    Troco(round(troco,2))
            else:
                print('Desculpe, mas a {} está indisponível.'.format(produto4))

        elif pedido == 5:
            if qt5 > 0:
                print('\nVocê escolheu: {}\nPreço: R${:0.2f}\n'.format(produto5,precop5))
                dinheiro = EntradaDinheiro(precop5)
                print('\nValor pago: R${:0.2f}'.format(dinheiro))
                qt5 -= 1
                troco = dinheiro - precop5
                if troco > 0:
                    print('Troco: R${:0.2f}\n'.format(troco))
                    print('Pegue Seu Troco:')
                    Troco(round(troco,2))
            else:
                print('Desculpe, mas a {} está indisponível.'.format(produto5))

        continuar = str(input('\nDeseja comprar outro produto? (S/N): '))
        if continuar == 'S' or continuar == 's':
            Maquina(qt1,qt2,qt3,qt4,qt5)
        else:
            print('Obrigado pela preferencia.\nVolte Sempre!!!')
    else:
        print('Descupe, mas a máquina está sem produtos.')


Maquina(5,5,5,5,5)




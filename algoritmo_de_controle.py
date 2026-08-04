from comandos import inventario
acesso = inventario()
valores = []
continuando = True
adicionando = True
testando = False
guia = ['Código do Produto', 'Descrição do produto', 'Categoria', 'Quantidade em Estoque', 'Localização', 'Data de Entrada', 'Valor Unitário', 'Valor Total', 'Observações']
while continuando:
    testando = True
    while testando:
        criar = input('Digite 1 para criar uma nova database ou 2 para acessar uma já existente:\n- ')
        if criar == '1':
            nome = input('Crie um nome para a database:\n- ')
            acesso.criar_inventario(nome)
            testando = False
        elif criar == '2':
            nome = input('Qual o nome da database?\n- ')
            acesso.acessar_inventario(nome)
            testando = False
        else:
            print('Valor inválido, tente novamente')
            testando = True

    testando = True
    while testando:
        adicionar = input('Digite 1 para adicionar algum item ou 2 para apenas vizualizar ela:\n- ')
        if adicionar == '1':
            testando = False
            pass
        elif adicionar == '2':
            adicionando = False
            continuando = False
            testando = False
        else:
            print('Valor inválido, tente novamente')
            testando = True

    while adicionando:
        for info in guia:
            valor = input(f'{info}: ')
            valores.append(valor)
        acesso.adicionar_inventario(valores, nome)
        testando = True
        
        while testando:
            continuar = input('Digite 1 para continuar adicionando items ou 2 para sair\n- ')
            if continuar == '1':
                adicionando = True
                testando = False
                valores = []
            elif continuar == '2':
                continuando = False
                adicionando = False
                testando = False
            else:
                print('Valor inválido, tente novamente')
                testando = True

acesso.visualizar_inventario(nome)
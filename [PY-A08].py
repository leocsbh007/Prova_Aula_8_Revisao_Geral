'''
[PY-A08] Você está desenvolvendo um programa para gerenciar uma lista de compras. 
O programa permite:
1 - Adicionar produtos à lista
2 - Visualizar a lista de produtos
3 - Atualizar as informações de um produto existente
4 - Remover produtos da lista. 
5 - O programa calcula o valor total de todos os produtos da lista.

O programa oferece as seguintes opções:
1 - Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

2 - Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.

3 - Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. 
    O programa solicita o nome do produto que deseja atualizar e,
        1 - Permite editar o nome,
        2 - Permite editar a quantidade
        3 - Permite editar o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
        
4 - Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
5 - Encerrar programa: Encerra a execução do programa.

O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.
'''
def Adicionarproduto(nome_produto:str, valor_produto:float, quantidade_produto:int) -> float:
    # Verifica se este produto já esta cadastrado
    f_existe_produto = False    
    for a in produtos:
        for v in a.values():
            if v == nome_produto:
                i += 1
                print("Já existe produto cadastrado")
                f_existe_produto = True                
                return 0               
             
    if f_existe_produto != True:    
        produto["produto"] = nome_produto
        produto["valor"] = valor_produto
        produto["quantidade"] = quantidade_produto
        produto["total"] = valor_produto * quantidade_produto
        produtos.append(produto.copy())        
        return produto["total"]

def Ver_lista_produtos(produtos:list):
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado")  
    else:
        for a in produtos:
            print("="*20)
            for k, v in a.items():
                if k == 'produto' or k == 'quantidade':
                    print(f"{k} : {v}")
                else:
                    print(f"{k} : R$ {v}")

def Atualizarproduto(nome_produto:str, novo_produto:str, valor_produto:float, quantidade_produto:int, totalProdutos: float) -> float:
    # Variavel de controle para verificar se existe produto na base de dados
    flag_produto = True
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado")
        return 0    
    else:
        i = 0
        for a in produtos:            
            for v in a.values():                
                if v == nome_produto:
                    flag_produto = False                       
                    produtos[i]['produto'] = novo_produto
                    produtos[i]['valor'] = valor_produto
                    produtos[i]['quantidade'] = quantidade_produto
                    # Atualiza o valor do total de produtos subtraindo o valor anterior total do produto
                    totalProdutos -= produtos[i]['total']                       
                    produtos[i]['total'] = valor_produto * quantidade_produto     
                    totalProdutos += produtos[i]['total']                            
                    # Retorna o valor atualizado do produto
                    return totalProdutos    
            # Atualiza o indeice de busca dos produtos                                    
            i += 1
    # Verifica de a flag esta "Suja"
    if flag_produto:
        print("Não existe este produto na Base de Dados")
        return 0

def Removerproduto(nome_produto:str, totalProdutos: float) -> float:
    # Variavel de controle para verificar se existe produto na base de dados
    flag_produto = True
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado")
        return 0    
    else:
        i = 0
        for a in produtos:            
            for v in a.values():                
                if v == nome_produto:
                    flag_produto = False                
                    totalProdutos -= produtos[i]['total'] 
                    produtos.pop(i)       
                    return totalProdutos                    
            # Atualiza o indice de busca dos produtos                                    
            i += 1
    # Verifica de a flag esta "Suja"
    if flag_produto:
        print("Não existe este produto na Base de Dados")
        return 0
        
produtos = []
produto = {}
totalProdutos = 0
controle = True

while controle:
    print("""
            ADICIONAR PRODUTOS  ( 1 )
            VISUALIZAR PRODUTOS ( 2 )        
            ATUALIZAR PRODUTOS  ( 3 )      
            EXCLUIR PRODUTOS    ( 4 )          
            SAIR                ( 0 )                                    
          """)
    opcao = input("Digite a Opção: ")

    match opcao:
        case '1':
            print("Inserindo produto")
            try:
                nome_produto = str(input("Nome do produto: ")).strip()
                valor_produto = float(input("Valor do produto: "))       
                quantidade_produto = int(input("Quantidade do produto: "))                        
                
            except ValueError:
                print("Erro: Entre com valores Validos.")
            except Exception as e:
                print(f'Erro inesperado {e}')
            else:
                totalProdutos += Adicionarproduto(nome_produto, valor_produto, quantidade_produto)
            
        case '2':
            print("Listando produtos")
            Ver_lista_produtos(produtos)
            print("="*20)
            print(f'Soma de Todos os produtos : R$ {totalProdutos}')
        case '3':
            print("Atualizando produto")
            try:
                nome_produto = str(input("Nome do produto: ")).strip()
                novo_produto = str(input("Novo nome do Produto: ")).strip()
                valor_produto = float(input("Novo valor do produto: "))       
                quantidade_produto = int(input("Nova quantidade do produto: "))              
                
            except ValueError:
                print("Erro: Entre com valores Validos.")
            except Exception as e:
                print(f'Erro inesperado {e}')
            else:
                totalProdutos = Atualizarproduto(nome_produto, novo_produto, valor_produto, quantidade_produto, totalProdutos)       
            
        case '4':
            print("Removendo produto")
            nome_produto = str(input("Nome do produto: ")).strip()   
            totalProdutos = Removerproduto(nome_produto, totalProdutos)
            
        case '0':
          controle = False
        case _:
            print('OPÇÃO INVALIDA')
else:
    print("Saindo do Sistema")

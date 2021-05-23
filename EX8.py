#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
# (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o 
# salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
#  Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

campo=dict()   #CAMPO ONDE ARMAZENARA OS VALORES
cadastro=list() #LISTA QUE VAI SER LEVADO AO DICIONARIO CAMPO

campo['Nome']=str(input("Informe o seu nome: ")).capitalize()      
campo['Ano nasc']=int(input("Ano do seu nascimento: "))
campo['CTPS']= int(input("Carteira de Trabalho (Caso não tenha, coloque 0): "))
if campo['CTPS']!=0:               #CASO O CTPS NAO FOR IGUAL A 0
    campo['Ano cont']=int(input("Ano de contratação: "))
    campo['Salário']=float(input('Seu salário: '))

    aposenta=campo['Ano cont']-campo['Ano nasc']+35     #ANO DE CONTRATAÇÃO - ANOS DE NASCIMENTO + 35
    campo['Ano de aposento']= f'{aposenta} anos '      #A IDADE EM QUE VAI SE APOSENTAR
    cadastro.append(campo.copy())
cadastro.append(campo.copy())

print(campo)

# for p in cadastro:
#     for v in p.values():
#         print(v,end=' ')
#     print()
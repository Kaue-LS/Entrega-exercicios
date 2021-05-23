#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e
#  devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 
# nb'data inválida' caso a data seja inválida.

from datetime import date, datetime

# datahj= date.today()
# print(datahj)
meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
#MESE ARMAZENADOS EM UMA LISTA NA POSIÇÃO DE 0 A 11


def extenso(data):#FUNÇÃO EXTENSO DA VARIAVEL DATA
    dia=data.day      #A DIA E ANO QUE VAI SER PEDIDO NA FORMATAÇÃO DA PRINT    
    ano=data.year     


    if data.month==1:    #SERIA O MES DA DATA
        mes=meses[1-1]   #O MES SERA PEDIDO NA LISTA, POREM A POSIÇÃO SERA O MES - 1 PARA QUE SEJA COLOCADO O MES POR EXTENSO CORRETO
    if data.month==2:
        mes=meses[2-1]  
    if data.month==3:
        mes=meses[3-1]
    if data.month==4:
        mes=meses[4-1]
    if data.month==5:
        mes=meses[5-1]
    if data.month==6:
        mes=meses[6-1]
    if data.month==7:
        mes=meses[7-1]
    if data.month==8:
        mes=meses[8-1]
    if data.month==9:
        mes=meses[9-1]
    if data.month==10:
        mes=meses[10-1]
    if data.month==11:
        mes=meses[11-1]
    if data.month==12:
        mes=meses[12-1]
    
    

    print(f"Hoje é dia {dia} de {mes} de {ano}")# O DIA E ANO COLOCADO  DO MES POR EXTENSO 
    

datap=str(input("Infome a data : "))       #VAI SER PEDIDO A DATA
data=datetime.strptime(datap,'%d/%m/%Y')   #A DATA SERA FORMATADA COM A STRING PRA SER DATA/MES/ANO
print(f'{data.day}/{data.month}/{data.year}')#imprimi a data 
extenso(data)# MOSTRA O RESULTADO DA FUNSAO EXTENSO(DATA)

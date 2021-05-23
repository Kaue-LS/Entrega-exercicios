#02 - Utilizando estruturas de repetição com variável de controle,
#  faça um programa que receba uma string com uma frase informada pelo usuário e
#  conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela,
#  depois mostre na tela essa mesma frase sem nenhuma vogal.

resp=int(input("""Deseja começar a ação?
[S=1]
[N=0]
"""))
#FOI PEDIDO A RESPOSTA EM NUMEROS, TRUE SERIA =1 E FALSE SERIA =0, 
# INDENPENDENTE DO NUMERO QUE NAO SEJA IGUAL A 1, A AÇÃO SERIA CANCELADA
while resp==True:
    i=0         #USADO PARA VERIFICAR LETRA POR LETRA NO "FOR"
    l_a=0
    l_e=0        #CONTAGEM DE QUANTAS VEZES CADA VOGAL APARECE
    l_i=0
    l_o=0
    l_u=0
    phrase=str(input("Coloque uma frase: ")).lower()#PEDIDO DA FRASE QUE SERA TRANSFORMADA EM MINUSCULA PARA A CONTAGEM
    for i in phrase:
        if i=='a':
            l_a+=1
        
            phrase=phrase.replace(i,' ')# SUBSTITUIRA  A VOGAL COM UM ESPAÇO VAZIO NA FRASE INSERIDA
        if i=='e':
            l_e+=1
            phrase=phrase.replace(i,' ')
        if i=='i':
            l_i+=1
            phrase=phrase.replace(i,' ')
        if i=='o':
            l_o+=1
            phrase=phrase.replace(i,' ')
        if i=='u':
            l_u+=1
            phrase=phrase.replace(i,' ')
        print(f"""
        A letra "a" apareceu {l_a} vezes.
        A letra "e" apareceu {l_e} vezes.
        A letra "i" apareceu {l_i} vezes.
        A letra "o" apareceu {l_o} vezes.
        A letra "u" apareceu {l_u} vezes.

        """)#O RESULTADO DE QUANTAS VEZES AS VOGAIS APARECEM
        
        print(f"Sem as vogais {phrase}")#A FRASE APOS A SOMA E AS SUBSTITUIÇÕES

print("Ação cancelada.")# RESPONDEU 0
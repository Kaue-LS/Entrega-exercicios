#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo
#  o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e 
# a quantidade de letras foram retiradas da frase original.


def refatorar(phrase):

    l_a=l_e=l_i=l_o=l_u=0 #CONTADORES DE QUANTAS VEZES AS VOGAIS APARECE
    for i in phrase:
        if i=='a'or i=='A': # SE CASO AS VOGAIS MAIUSCULAS OU MINUSCULAS APARECEREM SERA CONTADO AS VEZES, E SUBSTITUIÇÃO DA PALAVRA POR ESPAÇO VAZIO
            l_a+=1
            phrase=phrase.replace(i,' ')
        elif i=='e' or i =='E':
            l_e+=1
            phrase=phrase.replace(i,' ')
        elif i=='i' or i=='I':
            l_i+=1
            phrase=phrase.replace(i,' ')
        elif i=='o' or i =='O':
            l_o+=1
            phrase=phrase.replace(i,' ')
        elif i=='u'or i=='U':
            l_u+=1
            phrase=phrase.replace(i,' ')
        
    Lr=l_a+l_e+l_i+l_o+l_u       #Lr SERA O RESULTADO DE QUANTAS VEZES TODAS AS VOGAIS APARECERAM QUE SERAO AS VOGAIS RETIRADAS
    
    print(f"A quantidade de letras retiradas: {Lr}")

    return phrase
phrase=str(input("Escreva uma frase: "))
print('')
print(refatorar(phrase))#FOI PEDIDO A FUNÇÃO QUE USE A FRASE COLOCADA, QUE SERA PRINTADA APOS A FUNÇÃO SER FEITA






nota1=float(input())
nota2=float(input())
nota3=float(input())
media= (nota1+nota2+nota3)/3
if (media>=7):
    print ("aprovado")
elif (media<7)and(media>=3):
    print ("prova final")
else:
    print ("reprovado")
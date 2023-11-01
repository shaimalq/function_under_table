def tableau(tab, x,y):
    tab=[]
    for i in range(x,y):
        tableau.append(tab[i])
        return tableau

while True :
    tab=[]
    for i in range (10):
        n=int(input("entrer le nombre dans le tableau:"))
        tab.append(n)
    x=int(input("entrer premier indice:"))
    y=int(input("entrer dernier indice:"))
    print("tableau est:", tableau(tab,x,y))
    user=input("tu veux saisir  une nouvelle list ( oui,non):")
    if user=="non":
        break
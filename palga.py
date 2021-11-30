   
def lisamine(i,p): 
    """
    i-inimeste nimikiri,p-palka nimikiri 
    """
    kogus = int(input("Lisa inimest: "))
    for j in range(kogus):
        nimi = input("Nimi: ")
        i.append(nimi)
        palgad = int(input("Palk: "))
        p.append(palk)
        return i,p
def otsing_nimi_jargi(inimesed:list,palgad:list):
    """Tagastame jäejend või tekst
    :rtype var: tulemus
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene==nimi:
            n=inimesed.count(nimi)
            print("Inimene on olemas,selline kohtume",n,"korda")
            b=-1
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palgad[k]
                print(nimi,palk)
        else:
             t="Ei ole nimekirjas"
    return t

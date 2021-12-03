   
#def loe_failist(file:str)->str:
#    """Loeme tekst failist
#    """
#    f=open(file, "r")
#    stroka=f.read() #str #Muudab iga teksti vahedega
#    #stroka=f.readlines() list #Teeb teksti üherealiseks
#   f.close()
#    return stroka
#stroka=loe_failist("TextFile.txt")
#print(stroka)
#
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file, "r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

#def salvesta_failisse(fail:str):
#    f=open(fail, "a")
#    text=input("Sisesta tekst:")
#    f.write(text+"\n")
#    f.close()
#for i in range(1): 
#    salvesta_failisse("Loetelu.txt")

#def faili_sisu_umberkirjutamine(file:str,):
#    text=input("Sisesta uus tekst:")
#    with open(file, "w") as f:
#        f.write(text+"\n")
#faili_sisu_umberkirjutamine(input("Faili nimetus")+".txt")
#print()
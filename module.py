   
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file, "r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

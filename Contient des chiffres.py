def ContientChiffres(chaine):
    for caractere in chaine:
        if caractere.isdigit():
            return True 
    
    return False
    
    chiffre = ContientChiffres("sara")
    print(chiffre)
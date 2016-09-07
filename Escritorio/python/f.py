frases = raw_input("Frases: ")
fra = frases.splt(".")
for i in range(1,len(fra)+1):
    pal=len(fra[i].split(""))
    print "Frase ",i,": ", pal

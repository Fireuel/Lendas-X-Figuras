def lendas ():
    escolha = input("""
Escolha a sua história:
                    
[1] Yara
[2] Jaci
[3] Saci
[4] Curupira
[5] Lobisomem
[6] Zumbi dos Palmares
[7] Dandara
[8] Tiradentes
[9] Dom Pedro I
[10] Irmã Dulce """)

    Yara = ""
    Jaci = ""
    Saci = ""
    Curupira = ""
    Lobisomem = ""
    Zumbi_dos_Palmares = ""
    Dandara = ""
    Tiradentes = ""
    Dom_Pedro1 = ""
    Irmã_Dulce = ""

    if escolha == "1":
        print(Yara)
    
    elif escolha == "2":
        print(Jaci)
        
    elif escolha == "3":
        print(Saci)
        
    elif escolha == "4":
        print(Curupira)
        
    elif escolha == "5":
        print(Lobisomem)
        
    elif escolha == "6":
        print(Zumbi_dos_Palmares)
    
    elif escolha == "7":
        print(Dandara)
    elif escolha == "8":
        print(Tiradentes)
    elif escolha == "9":
        print(Dom_Pedro1)
    elif escolha == "10":
        print(Irmã_Dulce)
    else:
        print("Escolha inválida")

while True:
    lendas()
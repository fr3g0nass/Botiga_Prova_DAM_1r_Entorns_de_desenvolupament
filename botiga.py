#CONSTANTS
DESCOMPTE_ROBA = 0.10          # 10% de descompte per roba
RECARGA_ELECTRONICA = 0.15     # 15% de recàrrec per electrònica
XEC_JOVE = 5                    # xec jove per menors de 18 anys

#PRODUCTE
ROBA = "ROBA"
ELECTRONICA = "ELECTRONICA"

#FUNCIONS
def calcular_total(preu, tipus, edat):
    
    total = preu
    
    if tipus == "ROBA":
        total *= (1 - DESCOMPTE_ROBA )# descompte del 10%
    elif tipus == "ELECTRONICA":
        total *= (1 + RECARGA_ELECTRONICA) # recàrrec del 15%
        
    if edat < 18:
        total = XEC_JOVE # xec jove de 5 euros

    #PER EVITAR VALORS NEGATIUS    
    if total < 0:
        total = 0
        
    print("El total es:")
    print(res)

calcular(100, "ROBA", 15)
calcular(200, "ELECTRONICA", 40)
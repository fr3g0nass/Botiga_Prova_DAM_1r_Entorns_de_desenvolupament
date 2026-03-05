#CONSTANTS
DESCOMPTE_ROBA = 0.10          # 10% de descompte per roba
RECARGA_ELECTRONICA = 0.15     # 15% de recàrrec per electrònica
XEC_JOVE = 5                    # xec jove per menors de 18 anys

#PRODUCTE
ROBA = "ROBA"
ELECTRONICA = "ELECTRONICA"

#FUNCIONS
def calcular_total(preu, tipus, edat):
    """ Logica per aplicar el descompte/recarrec segons el tipus de producte"""
    
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

    return total

def mostrar_total(preu,tipus, edat):
    """ Mostrar per la pantalla el total final de el producte"""
    total =calcular_total(preu,tipus,edat)
    print(f"El total per un producte de tipus '{tipus}' amb preu {preu}€ i edat {edat} és: {total}€")


mostrar_total(100, ROBA, 15)
mostrar_total(150, ELECTRONICA, 18)

# @JoeL Roca

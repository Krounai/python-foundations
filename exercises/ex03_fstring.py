#exo3 : display with fstring
machine = "Presse-01"
pieces = 1250
cadence = 62.69
en_marche = True

print(f"{machine} a produit {pieces:,} pieces a {cadence:.1f} pieces/h")
print(f"etat : en marche {en_marche}")

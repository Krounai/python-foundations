# Exo8 : boucle for

pieces = [58, 61, 63, 0, 59, 62, 64, 60]
min_cadence = 50 
total_pieces = sum(pieces)
average_pieces = total_pieces / len(pieces)

for i, value in enumerate(pieces, start = 1):
	
	if value < min_cadence:
		print(f"Hour {i} : cadence : {value} <--- sous le seuil")
	else: 
		print(f"Hour {i} : cadence : {value}")
print(f"Total : {total_pieces}")
print(f"Moyenne : {average_pieces:.1f}")

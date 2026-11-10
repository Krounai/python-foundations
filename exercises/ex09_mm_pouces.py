# Exo9 : Convert mm to inch



def mm_to_inch(mm_values = list[float]):
	for i, value in enumerate(mm_values):
		print(f"{value/25.4:.2f}")
	
mm_to_inch(mm_values = [10, 25.4, 100])

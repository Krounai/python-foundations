# Exo9 : Convert mm to inch

mm_per_inch = 25.4

def mm_to_inch(mm_values: list[float]):
	return mm_values/mm_per_inch
	
if __name__ == "__main__":
     for mm_values in  [10, 25.4, 100]:
     	print(f"{mm_values} mm = {mm_to_inch(mm_values):.2f} in")

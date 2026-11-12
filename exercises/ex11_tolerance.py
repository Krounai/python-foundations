# exo11 : tolerance verifier

dimension_target = 12.0
interval_tolerance = 0.5

def is_within_tolerance(measurements = list[float]):
	nok_counter = 0
	for i, value in enumerate(measurements, start = 1):
		if value <= dimension_target + interval_tolerance and value >= dimension_target - interval_tolerance:
			print(f"Mesure {i} : {value} -> OK")
		else:
			nok_counter += 1
			print(f"Mesure {i} : {value} -> NOK")
	print(f"NOK : {nok_counter}")
measurements = [11.8, 12.4, 12.9, 11.2, 12.1]

is_within_tolerance(measurements)

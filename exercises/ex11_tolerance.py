# ex11: tolerance check

TARGET = 12.0
TOLERANCE = 0.5


def is_within_tolerance(value: float, target: float, tolerance: float) -> bool:
    # <= : une pièce pile en limite (12.5) est conforme
    return abs(value - target) <= tolerance


if __name__ == "__main__":
    measures = [11.8, 12.4, 12.9, 11.2, 12.1]
    nok = 0
    for i, value in enumerate(measures, start=1):
        if is_within_tolerance(value, TARGET, TOLERANCE):
            print(f"Mesure {i} : {value} -> OK")
        else:
            nok += 1
            print(f"Mesure {i} : {value} -> NOK")
    print(f"NOK : {nok}")
    print(f"Conformité : {(len(measures) - nok) / len(measures):.2%}")# exo11 : tolerance verifier

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

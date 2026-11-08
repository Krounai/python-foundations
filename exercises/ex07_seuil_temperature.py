# exo07 : learn if


alarm_threshold = 80
warning_threshold = 70

def temperature_status(temp: float) -> str:
	if temp > alarm_threshold :
		return "ALARME"
	elif temp > warning_threshold :
		return "ATTENTION"
	else:
		return "OK"



if __name__ == "__main__":
    temp = float(input("Enter temperature : "))
    print(f"Température : {temp} °C -> {temperature_status(temp)}")

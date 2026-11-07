# exo07 : learn if


alarm_threshold = 80
warning_threshold = 70
temp = float(input("Enter temperature : "))

def alarm_status(temp: float) -> str:
	if temp > alarm_threshold :
		return "ALARME"
	elif temp > warning_threshold :
		return "ATTENTION"
	else:
		return "OK"



print(f"Température : {temp} °C -> {alarm_status(temp)}")

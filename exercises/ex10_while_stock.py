# ex10 : while loop

stock= 500 
consumption=  62 



def hours_check(stock, consumption):
	nb_hours = 0
	while stock - consumption > 0:
		stock = stock - consumption
		nb_hours += 1
	return nb_hours, stock

hours_check(stock, consumption) 
	

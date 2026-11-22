# ex10 : while loop

 


def hours_check(stock: int, consumption: int) -> tuple [int, int]:
	if consumption <= 0:
		return 0, stock
	nb_hours = 0
	while stock >= consumption:
		stock = stock - consumption
		nb_hours += 1
	return nb_hours, stock

if __name__ == "__main__":
    stock = int(input("Stock : "))
    consumption = int(input("Consommation par heure : "))
    hours, rest = hours_check(stock, consumption)
    print(f"Heures de production : {hours}")
    print(f"Stock restant : {rest}")

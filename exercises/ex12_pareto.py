# ex12 pareto

STOPS = {
    "panne": 140,
    "changement de série": 95,
    "manque matière": 45,
    "qualité": 20,
}

def pareto(stops: dict[str,int]):
	ranked =  sorted(stops.items(), key=lambda item: item[1], reverse=True)
	result=[]
	cumulative = 0
	total = sum(stops.values())
	for cause, stop_duration in ranked:
		
		share = stop_duration/total
		cumulative += share 
		result.append((cause, share, cumulative)) 
		
	return result

if __name__ == "__main__":
    for cause, share, cumulative in pareto(STOPS):
        print(f"{cause:<20} : {share:.2%} % (cumul {cumulative:.2%} %)")

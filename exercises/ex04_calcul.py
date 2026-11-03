# Exo4 : calculate theorical production

pieces = 1250
cadence = 62.69
shift_duration=7.5
real_prod = 400

theo_prod = cadence * shift_duration
delta = theo_prod - real_prod
print(f"The theoretical production is {theo_prod:.1f} pieces")
print(f"the difference between the real productiion is {delta:.1f} pieces")


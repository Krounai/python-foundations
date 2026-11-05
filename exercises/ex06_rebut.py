# Ex06: calcul rebut


nb_pieces = 1250
nb_scrap = 37

taux_rebut = nb_scrap / nb_pieces 
good_pieces = nb_pieces - nb_scrap
rate_good_pieces = good_pieces / nb_pieces

print(f"taux de rebut :{taux_rebut * 100:.2f} %")
print(f"taux de rebut :{taux_rebut:.2%} ")
print(f"Pieces bonnes : {good_pieces}")
print(f"Taux bon du premier coup : {rate_good_pieces:.2%}")

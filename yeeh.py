#moduuli 5 tehtävä 1
import random
nopat = []
noppien_määrä = int(input("Monta noppaa heitetään? "))
toisto = 0
while toisto < noppien_määrä:
  noppa = random.randint(1, 6)
  nopat.append(noppa)
  print(f"Nopasta tuli: {noppa}")
  toisto += 1
noppa_summa = 0
for noppa in nopat:
  noppa_summa += noppa
print((f"Noppien summa on: {noppa_summa}"))
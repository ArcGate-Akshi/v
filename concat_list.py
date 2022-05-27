l1=['hello ','welcome ',]
l2=['Dear','sir']
#Expected output ['hello Dear','hello sir', 'take dear','take sir']

l3=[x + y for x in l1 for y in l2]
print(l3)
 
 #iterate both simultaneously with second in reverse order
for x, y in zip(l1,l2[::-1]):
  print(x,y)
  
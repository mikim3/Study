
li = []
li_hol = []
for i in range(7):
  li.append(int(input())) 
  if li[-1] % 2 == 1:
    li_hol.append(li[-1])

if len(li_hol) > 0:
  li_hol.sort()
  print(sum(li_hol))
  print(li_hol[0])
else:
  print(-1)
     



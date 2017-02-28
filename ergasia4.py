import statistics

x=list(raw_input("dvse lista"))


for j in range (2):
	max=x[0]
	min=x[0]

	for i in x:
		if i>max:
			max=i
		if i<min:
			min=i
			
	x.remove(max)
	x.remove(min)


a=statistics.pstdev(x)
print a 

print x
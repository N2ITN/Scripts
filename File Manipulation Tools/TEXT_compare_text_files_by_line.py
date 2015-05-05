

orig = open(r'C:\drop\4_21_15\PAREF_C__003.$ls.xls','r').readlines()

new = open(r'E:\untouched_data\4_21_15\PAREF_C__003.$ls.xls','r').readlines()

for i in range(len(orig)):
	x=orig[i]
	y =new[i]

	if len(x)>len(y):
		a= len(x)
	elif len(x)>len(y):
		a= len(y)
	elif len(x)==len(y):
		a = len(x)

	for char in range(a):
		if x[char] != y[char]:
			print x[char], y[char]

##
##	if x != y:
##		print "x: ",
##		print x
##		print "y: ",
##		print y
##		print


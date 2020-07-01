password='Rango'
i=0
entry=input('Enter password: ')
if entry==password:
	print('You are logged into the system.')
while entry!=password and i<4:
	entry=input('Invalid password Enter the password: ')
	i+=1
	if entry==password:
		print('You are logged into the system')
		break
	elif i==4 and entry!=password:
		print('You are kicked out of the system')

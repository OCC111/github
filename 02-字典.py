import random
import time

list1=[]

while True:
	print('')
	print('-'*10,'Welcome to police system','-'*10)
	print('')
	print('1.Apply for ID number\n2.Modify citizen information\n3.Delete citizen information\n4.Exit the public security management system')
	print('')
	dic1={}
	
	people = int(input('Please enter the program to be executed:'))
	if people == 1:

		user1 = input('Please enter the name:')
		job = input('Please enter the job:')
		phone = int(input('Please enter the phone:'))
		address = input('Plese enter the address:')
		sex = input('Please enter the sex:')
		age = int(input('Please enter the age:'))

		dic1['user1']=user1
		dic1['job']=job
		dic1['phone']=phone
		dic1['address']=address
		dic1['sex']=sex
		dic1['age']=age
		list1.append(dic1)
		time.sleep(2)
		print(list1)
		time.sleep(1)
		print('Please wait...')
		time.sleep(1)
		print('Your need to confirm the address first.You can only handle the following provinces!')
		print('1.Shandong\n2.Beijing\n3.Shanghai\n4.Tianjin\n5.Hebei')
		useradd = int(input('Please enter the region'))
		if useradd == 1:
			shan_card=random.randint(371312201801016001,371312201801016999)
			time.sleep(3)
			print('Your ID_number is:%d'% shan_card)
		elif useradd == 2:
			bei_card=random.randint(110196201801016001,110196201801016999)
			print('Your ID_number is:%d'% bei_card)
			time.sleep(3)
		elif useradd == 3:
			shang_card=random.randint(310196201801016001,310196201801016999)
			print('Your ID_number is:%d'% shang_card)
			time.sleep(3)
		elif useradd == 4:
			tian_card=random.randint(120105201801016001,120105196201801016999)
			print('Your ID_number is:%d'% tian_card)
			time.sleep(3)
		elif useradd == 5:
			he_card=random.randint(130100201801016001,310100201801016999)
			print('Your ID_number is:%d'% he_card)
			time.sleep(3)
	elif people == 4:
		break
		'''
   		mod = input('Please enter the name to be modified:')
		for n in list1:
			if mod == n[0]:
		pass
		'''		
				
					
			
			
	

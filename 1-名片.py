
import time

list1=[]
while True:
	print('1.添加\n2.修改\n3.删除\n4.退出')
	user = int(input('请输入功能:'))
	if user == 1:
		name = input('请输入姓名:')
		job = input('请输入职业:')
		age = int(input('请输入年龄:'))
		add = input('请输入地址:')
		phone = int(input('请输入电话:'))
		dic1={}
		dic1['name']=name
		dic1['job']=job
		dic1['age']=age
		dic1['add']=add
		dic1['phone']=phone
		list1.append(dic1)
		print(list1)
	elif user == 2:
		user1 = input('请输入要修改的内容:')
		for n in list1:
			if user1 == n["name"]:
				user2 = int(input('请输入功能\n1.修改名字\n2.修改职业\n3.修改年龄\n4.修改地址\n5.修改电话'))	
				if user2 ==	1:
					name = input('请输入要修改的名字:')
					n["name"]=name
					print('修改后的名字是:%s'% dic1)
				elif user2 == 2:
					name1 = input('请输入要修改的职业:')
					n["job"]=name1
					print('修改后的职业是:%s'% list1)		
				elif user2 == 3:
					name2 = input('请输入要修改的年龄:')
					n["age"]=name2
					print('修改后的年龄是:%s'% list1)		
				elif user2 == 4:
					name3 = input('请输入要修改的地址:')
					n["add"]=name3
					print('修改后的地址是:%s'% list1)		
				elif user2 == 5:
					name4 = input('请输入要修改的电话:')
					n["phone"]=name4
					print('修改后的电话是:%s'% list1)
				else:
					break		
	elif user == 4:
		break


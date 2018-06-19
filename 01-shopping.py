print('-'*10,'加尔商超管理系统','-'*10)
import time
list1=[]   #大列表，存储下面小列表的数据

while True:
	print('1.添加商品\n2.修改商品\n3.删除商品\n4.退出系统')
	list2=[]    #此为小列表，存储下面的内容
	sys = int(input('请输入要进行的程序:'))
	if sys == 1:   #添加商品
		time.sleep(2)
		user1 = input('请输入要添加的商品:')  
		price = int(input('请输入商品价格:'))

		list2.append(user1)
		list2.append(price)
		list1.append(list2)
		print(list1)
	elif sys == 2:   #修改商品
		user2 = input('请输入要修改的商品:')
		for n in list1:
			if user2 == n[0]:
				print('1.修改名字\n2.修改商品\n3.修改名字和价格')
				user3 = int(input('请选择功能:'))
				if user3 == 1:
					name = input('please insert shop name:')
					n[0] = name
					print(list1)
				elif user3 == 2:
					name1 = int(input('please insert price:'))
					n[1] = name1
					print(list1)
				elif user3 == 3:
					name = input('please insert shop name:')
					name1 = int(input('please insert price:'))
					n[0] = name
					n[1] = name1
					print(list1)
				break 
	elif sys == 3:   #删除商品
		user4 = input('please insert delete shop name:')
		for position,l in enumerate(list1):   #for循环，，，索引，，，l代表一个列表，enumerate函数名下的list1在l中
			if user4 == l[0]:   #如果user4
				list1.pop(position)   #删除列表索引值
		break  



	

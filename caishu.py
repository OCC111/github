import random 
pc=random.randint(1,100)
i = 0
while i < 3:
	user = int(input('输入1~100其中一个数字，猜猜：'))
	if user > pc :
		print('数大了，好好想想')
	elif user < pc:
		print('数小了，干哈玩意的')
	else:
		print('恭喜您猜对喽！')
		i += 1

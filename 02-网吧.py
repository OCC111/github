i = 1
import random 
import time
while i < 24:
	print('玩游戏%d小时'% i)
	if i == 8:
		time.sleep(3)
		print('老爹来啦！暂停游戏、！')
		print('$'*30)
		time.sleep(3)
		print('1.逃跑\n2.假装在学习\n3.装睡')
		user = input('请输入要进行的程序:')
		time.sleep(3)
		pc = random.randint(1,100)
		if user == '1':
			print('正在加速逃跑中......')
			pc = random.randint(1,100)
			time.sleep(3)
			user2 = input('请输入逃跑路线:')
			if user2 == pc:
				time.sleep(3)
				print('哦，谁都救不了你，挨揍吧！')
			else:
				time.sleep(3)
				print('逃跑成功')
		elif user == '2':
			print('学习中,,,')
		elif user == '3':
			print('sleeping......')
			sleep = 0
			pc2 = random.randint(1,5)
			if pc2 <= 2:
				time.sleep(3)
				print('你这熊孩子，竟敢装睡！！！')
				time.sleep(3)
				print('已经被暴揍，医院治疗中...')
			elif pc2 > 4:
				print('昏睡中...')
	i += 1

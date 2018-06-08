
print('')
print('$'*30)
print('欢迎来到时空大陆！')
print('$'*30)
print('')
print('-'*30)
print('')

while True:
	week = int(input('请输入星期:'))
	if week == 1 or week == 2 or week == 3 or week == 4 or week == 5: 
		duan = input('请输入时间段:')
		if duan == '上午':
			time = int(input('请输入时间:'))
			if time > 8 and time < 12:
				print('正在上课')
			elif time >= 10 and time < 12:
				print('正在玩游戏')
		elif duan == '下午':
			time1 = int(input('请输入时间:'))
			if time1 > 14 and time1 < 17:
				print('正在上课')
			else:
				print('不知道在干什么')
		else:
			print('你谁啊！想怎样？')
	elif week == 6:
		print('全体上课')
	elif week == 7:
		print('逛街吧！浪吧~')

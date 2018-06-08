while True:
	name = input('please insert you name:')
	if name == '拜拜👋':
		print('老兄，你要造反啊！拜拜啦！')
		break
	elif name == '老王':
		print('老兄，一起happy啊。玩啊。反正有大把时光！！！')
	else:
		print('一起吃烧烤喝啤酒吧！')
		age = int(input('please insert you age:'))
		if age >= 18:
			print('可以进网吧！')
		else:
			print('快回家学习去！')

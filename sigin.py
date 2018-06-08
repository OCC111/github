while True:
	username = input('请输入用户名:')
	passwd = int(input('请输入密码:'))
	if username == '123' and passwd == 123:
		print('恭喜您登录成功☺')
	else:
		print('登录失败喽！拜拜')
		break

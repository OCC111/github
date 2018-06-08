
print('欢迎来到游戏世界！！！')
print('1.王者荣耀')
print('2.植物大战僵尸')
print('3.退出')
while True:
	app = input('请输入要进行的程序：')
	if app == '1':
		account = int(input('请输入账号：'))
		passwd = input('请输入密码：')
		if account == 859899882 and passwd == 'jiayi123':
			print('欢迎来到王者荣耀！')
		else:
			print('登录失败喽！下次再来吧！')
		break
	elif app == '2':
   		print('欢迎来到植物大战僵尸！')
	elif app == '3':
	    print('拜拜')
	break

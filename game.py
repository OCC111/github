
import time
print('欢迎来到游戏世界！！！')
print('1.王者荣耀')
print('2.植物大战僵尸')
print('3.退出')

list1=['打野中，，，','草丛躲避等待开团,,,','正在推塔，，，','壮烈牺牲']
while True:
	app = input('请输入要进行的程序：')
	if app == '1':
		account = int(input('请输入账号：'))
		passwd = input('请输入密码：')
		if account == 859899882 and passwd == 'jiayi123':
			print('欢迎来到王者荣耀！')
			sup = input('请输入您要使用的英雄~\n1.疾风剑豪')
			if sup == '1':
				print('您已选中疾风剑豪！')
				time.sleep(1)
				print('即将进入王者峡谷，敌军还有五秒到达战场！')
				time.sleep(5)
				print('全军出击')
				time.sleep(1)
				print(list1[2])
				time.sleep(1)
				print(list1[1])
			continue
		else:
			print('登录失败喽！下次再来吧！')
		break


	elif app == '2':
   		print('欢迎来到植物大战僵尸！')
	elif app == '3':
	    print('拜拜')
	break
	else:
		print('你输入错误，请面壁思过！')






'''
			sup = input('请输入您要使用的英雄~\n')
			if sup == '疾风剑豪':
				print('即将进入王者峡谷，敌军还有五秒到达战场！')
				time.sleep(5)
				print('全军出击')
	elif app == '2':
   		print('欢迎来到植物大战僵尸！')
	elif app == '3':
	    print('拜拜')
	break
'''

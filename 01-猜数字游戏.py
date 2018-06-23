import random 
import time

pc=random.randint(1,100)

i = 0
def xinxi():
	for i in range(1,4):
		user = int(input('猜数字,1~100:'))

		if user == pc:
			time.sleep(3)
			print('猜对了')

		elif user == 0:
			pc2=random.randint(1,50)
			user4 = int(input('输入数字,每一次的数字都是随机的~：'))
			if user4 == pc2:
				print('你可真够幸运的~')
				continue
			else:
				print('刚刚那个数字竟然是:%d'% pc2)
				print('祈祷吧!或许能猜对!')
			continue
		elif user % 4 == 0:
			time.sleep(2)
			print('刚刚那个神秘的数字是:%d'% pc)			
			time.sleep(2)
			print('也许你该祈祷上帝带给你幸运了~')
			time.sleep(3)
			
			break
		elif user == 87:
			time.sleep(2)
			print('您猜错了!进行下一环节吧!')
			time.sleep(2)
			age = int(input('输入年龄吧:'))
			gong = int(input('输入工龄:'))

			if (age > 18) or (gong > 3):
				print('您可以在这里进行无限的嗨皮~')
				time.sleep(3)
				print('1.退出系统\n2.退出系统\n3.退出系统')
				user2 = int(input('随意选择一个吧!我也不知道里面是什么:'))
				if user2 == 1:
					print('可能你是遇到我了，否则你这是不礼貌的行为，希望下次不会见到你！')
					continue
				elif user2 == 3:
					print('如果你想来玩的话,我的电脑可以供应你!')
					time.sleep(3)
					print('好吧，这是一个网吧！你可以玩啦!')
					time.sleep(2)
					user3 = input('好吧，这里其实只能去输入一些文字，并且可劲的打也没人管你。不过别按回车键。')
					if (user3 == '傻子') or (user3 == '二嘎子') or (user3 == 'shit'):
						time.sleep(1)
						print('请你礼貌一些!!!')
						continue
				elif user2 == 2:
					print('忘记告诉你了,2是退出系统哦!')
					break
					
			else :
				print('我想您可能不适合在这里!')
				continue

	i += 1
xinxi()	

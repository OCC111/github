print('')
print('$'*30)
print('欢迎来到北京国际宾馆')
print('$'*30)
print('')

print('-'*30)
print('')
while True:
	sex = input('请输入性别：')
	if sex == '男':
		height = int(input('请输入身高：'))
		money = int(input('请输入财富：'))
		yan = int(input('请输入颜值：'))
		if height == 180 and money > 1000000 and yan > 90:
			print('高富帅啊！来玩嘛？')
		else: 
			print('你是谁啊！稳一点吧！拜拜')
	elif sex == '女':
		pifu = input('请输入皮肤颜色:')
		mon = int(input('请输入财富:'))
		yanzhi2 = int(input('请输入颜值:'))
		if pifu == '白色' and mon > 800 and yanzhi2 > 90:
			print('白富美啊，快活啊！')
		else:
			print('哈哈哈哈哈哈哈')

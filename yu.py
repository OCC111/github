print('$'*30)
print('$'*30)
print('')
print('欢迎进入超级管理系统！')
print('')
print('$'*30)
print('$'*30)

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)
while True:
    shuzi = int(input('大爷，输入数字：'))
    if shuzi >= 0 and shuzi <= 10:
        print('你是个巨婴啊！别闹')
    else:
        print('大爷啊，这是儿童俱乐部好不啦！')

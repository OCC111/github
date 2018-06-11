print('')
print('>'*30)
print('欢迎进入本次的娱乐随机游戏')
print('>'*30)
print('')
import random
import time
list1=['邵广超','嘉怡','王学文','常瑞贤','柴子健','李冰','张伟','石现龙','郑成峰','臧一凡','崔健','李爽','李依哲','温思思','赵伟奇','李宁','王伟璐','邢凯']
slice1=random.sample(list1,2)
time.sleep(3)
print('等等，别急。。。。')
time.sleep(3)
print('马上就好了。。。。')
time.sleep(3)
print('即将选中的人要唱歌，跳舞')
time.sleep(5)
print(slice1)

if slice1 == '邵广超':
	print('您的系统即将在五秒钟退出！')
	time.sleep

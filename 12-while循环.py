'''
result = 0
i = 1
for i in range(1,100):
	if (i%2) == 1:
		print(i)
		i += 1
		result += i	
	elif (i%2) != 1:
		print(i)
'''

sum1 = 0
sum2 = 0
i = 0
while i <= 100:
	if i % 2 == 0:
#print(i)
		sum1 = sum1 + i
	elif i % 2 != 0:
	    sum2 = sum2 + i
	else:
		pass
	i += 1
print('偶数的和是:%d'% sum1)
print('奇数的和是:%d'% sum2)
print('总和是:%d'% (sum1+sum2))


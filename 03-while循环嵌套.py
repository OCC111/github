
'''
i = 1
while i < 5:
	j = 1
	while j < 9 :
		print('%d+%d=%d'% (i,j),end = '')
		j += 1
	print('')
#	print('第%d列'% i)
	i += 1
'''
count = 1
while count <= 9:
	row = 1
	while row <= count:
		print('%d*%d=%d'% (count,row,count*row),end = '')
		row += 1
	print('')
	count += 1



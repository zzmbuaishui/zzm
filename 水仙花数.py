
shuixianhuacount=0
i=100
while  i < 1000:
    baiwei = i // 100
    shiwei = int((i%100)/10)
    gewei  = int( i%10 )
    if  baiwei ** 3 + shiwei ** 3 + gewei ** 3==i :
        print("是水仙花数")
        print("水仙花数为",i)
        shuixianhuacount += 1
    i += 1
	#baiwei= int(i/100)      #百位
	#shiwei= int((i%100)/10)    # 十位
	#gewei = int( i%10 )     #个位
	#if  baiwei ** 3 + shiwei ** 3 + gewei ** 3==i :
		#print("是水仙花数")
		#print("水仙花数为",i)
		#shuixianhuacount+=1
    
else :
	print("水仙花数个数为：",shuixianhuacount)		
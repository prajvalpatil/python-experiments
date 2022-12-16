possum=0
negsum=0
poscount=0
negcount=0
avgpos=0
avgneg=0
while(1):
    num=int(input("Enter the number\n"))
    if(num>0):
        possum=possum+num
        poscount=poscount+1
        avgpos=possum/poscount
    elif(num<0):
        if(num==-1):
            break
        else:
            negsum=negsum+num
            negcount=negcount+1
            avgneg=negsum/negcount
    else:
        pass
print("The sum of positive number is \n",possum)
print("The average of positive number is \n",avgpos)
print("The sum of negative number is \n",negsum)
print("The average of negative number is \n",avgneg)

kmers= input()
str = input()

d = int(input())

szptr = len(kmers)
sizestr = len(str)

for i in range (0, sizestr) :
    cnt = 0
    idx = i
    for j in range(0,szptr,1) :
        if( kmers[j] != str[idx] ) :
            cnt+=1
        idx+=1
    
    if( cnt <= d ) :
        print(i)
    

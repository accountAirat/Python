file = open( "file.txt",'r+')
f = file.read()
print(f)


count = 1
rle = list()
for i in range(1,len(f)):
    if f[i] == f[i-1]:
        count+=1
    else:
        rle.append(str(count)+str(f[i-1]))
        count = 1
print(*rle)
file.writelines('\n')
file.writelines(rle)


file.close()

#qwertyaabbbccccddsspoiu
#1q 1w 1e 1r 1t 1y 2a 3b 4c 2d 2s 1p 1o 1i 1u
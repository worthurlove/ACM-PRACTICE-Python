data = []
data.extend(input().split())

N = int(data[0])

split_data = []



def qiege(data):

    l1 = len(data)
    last = '00000000'
    i = 0
    while l1 - 8 > 0:
        split_data.append(data[i*8:(i + 1)*8])
        l1 -= 8
        i += 1
    if l1 != 0:
        last = str(data[len(data)-l1:len(data)])
        for i in range(8 - l1):
            last += '0'
        split_data.append(last)

for i in range(1,N+1):
    qiege(data[i])


split_data = sorted(split_data)


for i in split_data:
    print(i,end=' ')
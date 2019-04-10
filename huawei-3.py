M,N = map(int,input().split())

map_data = [0]*M

for i in range(M):
    map_data[i] = []

    map_data[i].extend(map(int,input().split()))

x1,y1,x2,y2 = map(int,input().split())

num = [0]
print(map_data)
def step(x1,y1,x2,y2):
   
    #确定上下左右有没有路

    #向上走
    if x1 - 1 >= 0 and map_data[x1 - 1][y1] > map_data[x1][y1]:
        step(x1-1,y1,x2,y2)
    
    #向下走
    if x1 + 1 <= M - 1 and map_data[x1 + 1][y1] > map_data[x1][y1]:
        step(x1 + 1,y1,x2,y2)

    #向左走
    if y1 - 1 >= 0 and map_data[x1][y1 - 1] > map_data[x1][y1]:
        step(x1,y1 - 1,x2,y2)
    #向右走
    if y1 + 1 <= N -1 and map_data[x1][y1 + 1] > map_data[x1][y1]:
        step(x1,y1 + 1,x2,y2)   

    if x1 == x2 and y1 == y2:
        num[0] += 1
    else:
        return 0


step(x1,y1,x2,y2)

print(num[0])


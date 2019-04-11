'''
leetcode系列：题号-79
Description:Given a 2D	board	and	a	word,	find	if	the	word	
        exists	in	the	grid. The	word	can	be	constructed	
        from	letters	of	sequentially	adjacent	cell,	where	
        "adjacent"	cells	are	those	horizontally	or	
        vertically	neighboring.	The	same	letter	cell	may	
        not	be	used	more	than	once.
Author:worthurlove
Date:2019.411
'''
import numpy as np
board =[
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
]

board = np.array(board)


M,N = board.shape[0], board.shape[1]

visited = np.zeros((M,N))

word = 'SEE'

have = [0]
#每个单词不能被用两次，所以不能倒退
def matchAlpha(i,j,t):
   

    visited[i][j] = 1#访问标记
    #上下左右寻找下一个匹配字母
    #上
    if i - 1 >= 0 and board[i - 1][j] == word[t] and visited[i - 1][j] == 0:
        if t == len(word) - 1:
            have[0] = 1
        else:
            matchAlpha(i-1,j,t+1)

    #下
    if i + 1 <= M - 1 and board[i + 1][j] == word[t] and visited[i + 1][j] == 0:
        if t == len(word) - 1:
            have[0] = 1
        else:
            matchAlpha(i + 1,j,t+1)

    #左
    if j - 1 >= 0 and board[i][j - 1] == word[t] and visited[i][j - 1] == 0:
        if t == len(word) - 1:
            have[0] = 1
        else:
            matchAlpha(i,j - 1,t+1)
    #右
    if j + 1 <= N - 1 and board[i][j + 1] == word[t] and visited[i][j + 1] == 0:
        if t == len(word) - 1:
            have[0] = 1
        else:
            matchAlpha(i,j + 1,t+1)
        

def search(board,word):
    for i in range(M):
        for j in range(N):
            #匹配第一个字母后开始寻找
            if board[i][j] == word[0]:
                t = 1
                visited[:,:] = 0
                matchAlpha(i,j,t)
                if have[0] == 1:
                    return True
    return False

search(board,word)
result = True if have[0] == 1 else False
print(result)


'''
leetcode系列：题号-64
Description:Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Author:worthurlove
Date:2019.5.16
'''
grid = [
  [1,3],
  [1,5]

]
    
x_end = len(grid[0])
y_end = len(grid)

for i in range(y_end):
    for j in range(x_end):
        if i != 0 or j != 0:
            if i == 0:
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            elif j == 0:
                grid[i][j] = grid[i][j] + grid[i - 1][j]
            else:
                grid[i][j] = grid[i][j] + min(grid[i][j - 1],grid[i - 1][j])
print(grid[y_end - 1][x_end - 1])
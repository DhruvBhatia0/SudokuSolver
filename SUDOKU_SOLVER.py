def display(board):
    for i in range(9):
        if i%3==0:
            print('-'*25)
        for j in range(9):
            if j%3==0:
                print('| ',end='')
            if j!=8:
                print(board[i][j],end=' ')
            else:
                print(board[i][j],end=' |\n')
    print('-'*25)
def find(b):
    for i in range(9):
        for j in range (9):
            if b[i][j]==0:
                return (i,j)
    return None
def check(b,num,row,col):
    for i in range(9):
        if b[row][i]==num:
            return False
        if b[i][col]==num:
            return False
    bx=(row//3)*3
    by=(col//3)*3
    for i in range(bx,bx+3):
        for j in range(by,by+3):
            if num==b[i][j]:
                return False
    return True
def solve(b):
    if find(b)==None:
        return True
    else:
        row,col=find(b)
    for i in range(1,10):
        if check(b,i,row,col):
            b[row][col]=i

            if solve(b):
                return True
            b[row][col]=0
    return False
        
boards = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
board=[[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]
    ]
display(board)
print()
solve(board)
print()
display(board)


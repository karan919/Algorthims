def printBoard():
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(board[i][j])
        print(temp)

def getPossibilities(x,y):
    move_x=(2,1,-1,-2,-2,-1,1,2)
    move_y=(1,2,2,1,-1,-2,-2,-1)
    possibilities=[]
    for i in range(n):
        if x+move_x[i]>=0 and y+move_y[i]>=0 and x+move_x[i]<n and y+move_y[i]<n and board[x+move_x[i]][y+move_y[i]]==0:
            possibilities.append([x+move_x[i],y+move_y[i]])
    return possibilities

def solve():
    counter=2
    x=0
    y=0
    for i in range(n*n-1):
        pos=getPossibilities(x,y)
        minimum=pos[0]
        for p in pos:
            if len(getPossibilities(p[0],p[1])) <= len(getPossibilities(minimum[0], minimum[1])):
                minimum = p
        x=minimum[0]
        y=minimum[1]
        board[x][y]=counter
        counter+=1

n=8
board=[[0]*n for i in range(n)]
board[0][0]=1
solve()
printBoard()

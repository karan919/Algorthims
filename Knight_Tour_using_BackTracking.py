def isSafe(n,x,y,board):
    if x>=0 and y>=0 and x<n and y<n and board[x][y]==-1:
        return True
    return False

def printSolution(n, board):
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(board[i][j])
        print(temp)

def solveKT(n):
    board = [ [-1]*n for i in range(n)]
    move_x=[2,1,-1,-2,-2,-1,1,2]
    move_y=[1,2,2,1,-1,-2,-2,-1]
    pos=1
    board[0][0] = 0
    if(not solveKTUtil(n,0,0,move_x, move_y, board, pos)):
        print("no solution")
    else:
        printSolution(n,board)

def solveKTUtil(n, curr_x, curr_y, move_x, move_y, board, pos):
    if n**2==pos:
        return True
    for i in range(8):
        new_x=curr_x+move_x[i]
        new_y=curr_y+move_y[i]
        if(isSafe(n,new_x,new_y,board)):
            board[new_x][new_y]=pos
            if solveKTUtil(n, new_x, new_y, move_x, move_y, board, pos+1):
                return True
            #backtracking
            board[new_x][new_y]=-1
    return False

n=5
solveKT(n)

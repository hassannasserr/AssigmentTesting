size = int (input("Enter The size of matrix: "))
matrix1=[list(map(int , input("Enter your matrix1: ").split())) for _ in range(size)]
matrix2=[list(map(int , input("Enter your matrix2: ").split())) for _ in range(size)]

matrix3=[[matrix1[i][j]+matrix2[i][j]for j in range (size) ]for i in range (size)]
print(matrix3)
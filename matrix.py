matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#to calculate number of rows
print(len(matrix))
#to print the first row
print(matrix[0])
#to calculate number of columns
print(len(matrix[0]))
print(matrix[2][1])

for i in range(3):
    print("\n")
    for o in range(3):
        print(matrix[i][o],end=" ")

matrixA=[[2,9,6],[4,1,7],[8,5,4]]
matrixB=[[7,5,9],[3,9,8],[1,3,2]]
sum=[[0,0,0],[0,0,0],[0,0,0]]
difference=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        sum[i][j]=matrixA[i][j]+matrixB[i][j]
        difference[i][j]=matrixA[i][j]-matrixB[i][j]
for p in range(3):
    print("\n")
    for l in range(3):
        print(sum[p][l],end=" ")
for p in range(3):
    print("\n")
    for l in range(3):
        print(difference[p][l],end=" ")

flag=True
while (flag):

	print('''
Below is a list of all matrix operations this program supports:

1. Addition of Two Matrices
2. Subtraction of Two Matrices
3. Multiplication of Two Matrices
4. Transpose of a Single Matrix 
5. Checks if the matrix is symmetric or non-symmetric
6. Checks if the matrix is skewSymmetric or not #HAS A PROBLEM
7. Finds out the determinant of a 2x2 Matrix ONLY
8. Finds out the determinant of a 3x3 Matrix ONLY
9. Inverse of a 2x2 Matrix
10. Power ''') 

	def matrixInput(rows, columns): #this function takes input of matrix to divide its elements into sub-lists that are equal to the number of rows of a matrix

		list01=[]

		for row in range(rows):

			list02=[]

			for column in range(columns):

				try:

					element=int(input("Enter the element in Row %d and Column %d :" %(row+1, column+1)))

				except:

					print("Invalid Input. A zero has been added in this position instead. ")
					list02.append(0)

				else:

					list02.append(element)

			list01.append(list02)

		return list01

	def printMatrix(matrix): #this function prints a matrix in a way that it appears in the standard matrix form on the screen

		for element in matrix:

			print(element)

	def sum(matrix01, matrix02): #adds two matrices of the same dimensions

		addition=[]
		
		for i in range(len(matrix01)):

			list01=[]

			for j in range(len(matrix01[i])):

				list01.append(matrix01[i][j] + matrix02[i][j])

			addition.append(list01)

		print("The sum of the two matrices is:" )
		printMatrix(addition)

	def sub(matrix01, matrix02): #subtracts two matrices of the same dimensions.

		subtraction=[]
		
		for i in range(len(matrix01)):

			list01=[]

			for j in range(len(matrix01[i])):

				list01.append(matrix01[i][j] - matrix02[i][j])

			subtraction.append(list01)

		print("The resultant matrix is: ")
		printMatrix(subtraction)

	def product(matrix01,matrix02): #computes the product of two matrices.

		product=[]

		for rowMatrix01 in range(len(matrix01)):

			product.append([])

			for rowMatrix02 in range(len(matrix01)):

				sum=0

				for rowElement in range(len(matrix01[rowMatrix01])):

					sum+=((matrix01[rowMatrix01][rowElement]) * (matrix02[rowElement][rowMatrix02]))

				product[rowMatrix01].append(sum)


		print("The product of the two matrices is:")
		printMatrix(product)
		return product

	def transpose(matrix, rows, columns): #replaces the columns of a matrix with it's rows, hence transposing the matrix.

		transpose= []

		for i in range(columns):
			
			list01=[]

			for j in range(rows):

				list01.append(matrix[j][i])

			transpose.append(list01)

		print("The transposed matrix is: ")
		printMatrix(transpose)
		return transpose

	def skewSymmetric(matrix, transpose, rows, columns): #finds out if the transpose of a matrix multiplied with -1 is equal to the original matrix or not.

		for i in range(rows):

			flag=False

			for j in range(columns):
				
				if (matrix[i][j] != -(transpose[i][j])):
					flag=True

		if flag==False:

				print("The matrix is skewSymmetric. ")

		else:

				print("The matrix is NOT skewSymmetric.")

	def determinantfunc(matrix): #finds the determinant of a 2x2 matrix ONLY.

		return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	def determinent(mat):	 #finds the determinant of a 3x3 matrix only.

		summ01=0
		summ=0
		finalSum=0 

		for a in range(3):

			for b in range(2):

				mat[a].append(mat[a][b])
		
		for i in range(-1,2):

			for j in range(i+1, i+2):

				for k in range(i+2, i+3):

					for l in range(i+3, i+4):

						summ01+=(mat[0][j] * mat[1][k] * mat[2][l])

		for i in range(-1, 2):

			for j in range(i+1, i+2):

				for k in range(i+2, i+3):

					for l in range(i+3, i+4):

						summ+=(mat[2][j] * mat[1][k] * mat[0][l])

		finalSum= summ01 - summ
		return finalSum
		
	def inverse2x2(matrix): #finds the inverse of a 2x2 matrix ONLY.

		determinent= determinantfunc(matrix)
		temp01= matrix[1][1]
		temp02= matrix[0][1]*-1
		matrix[1][1]= matrix[0][0]
		matrix[0][1]= matrix[1][0] * -1
		matrix[0][0]= temp01
		matrix[1][0]= temp02
		inverse= [[0,0],[0,0]]

		for a in range(2):
			for b in range(2):
				inverse[a][b]= matrix[a][b]/determinent

		print("The inverse of the matrix is :")
		printMatrix(inverse)

	def power(matrix, rowsInMatrix01): #multiplies a matrix to itself for a given number of times.

		power= int(input("Enter the power of matrix: "))

		for c in range(power-1):

			matrix= product(matrix, matrix)

		print("The final result of matrix raised to the power %d is :" % power)
		printMatrix(matrix)

	def inputMatrixInfo(operation): #takes input details of matrices to make sure that the user isn't trying to do an operation that cant be performed on matrices of that dimension. Hence spots out any error before having to type in the matrices.

		try:

			rowsInMatrix01= int(input("Enter the number of rows in matrix 1: "))
			columnsInMatrix01= int(input("Enter the number of columns in matrix 1: "))

			if operation<4: #asks for the second matrices details only if the operation given is greater than 4, i.e. it's an operation that requires two matrices.

				rowsInMatrix02= int(input("Enter the number of rows in matrix 2: "))
				columnsInMatrix02= int(input("Enter the number of columns in matrix 2: "))

		except Exception as e:

			print("Invalid Input.")
			print(e)

		else:

			if operation<4:

				decider(operation, rowsInMatrix01, columnsInMatrix01, rowsInMatrix02, columnsInMatrix02)

			else:

				decider01(operation, rowsInMatrix01,columnsInMatrix01)

	def decider01(operation, rowsInMatrix01,columnsInMatrix01): #this function is for operations that require a single matrix. It first ensures that the function can be perfomed on the matrix of that dimension, and then calls the respective function.

		if (operation==7 or operation==9) and (rowsInMatrix01!=2 or columnsInMatrix01!=2):

				print("Please enter a 2x2 matrix only.")

		elif (operation==8) and (rowsInMatrix01!=3 or columnsInMatrix01!=3):

			print("Please enter a 3x3 matrix only.")

		else:

			matrix01= matrixInput(rowsInMatrix01, columnsInMatrix01)
			print("Matrix 1 is :") 
			printMatrix(matrix01)

			if operation==4:

				transpose(matrix01, rowsInMatrix01, columnsInMatrix01)

			elif operation==5:

				transposed= transpose(matrix01, rowsInMatrix01, columnsInMatrix01)

				if transposed==matrix01:

					print("The matrix is symmetric. ")

				else:

					print("The matrix is non-symmetric. ")

			elif operation==6:

				transpose01= transpose(matrix01,rowsInMatrix01,columnsInMatrix01)
				skewSymmetric(matrix01,transpose01, rowsInMatrix01,columnsInMatrix01)

			elif operation==7:

				print("The determinant of the matrix is : " ,determinantfunc(matrix01))

			elif operation==8:

				print("The determinant of the matrix is : ", determinent(matrix01))

			elif operation==9:

				print("The inverse of the matrix is: \n", inverse2x2(matrix01))

			elif operation==10:

				power(matrix01, rowsInMatrix01)

	def decider(operation, rowsInMatrix01, columnsInMatrix01, rowsInMatrix02, columnsInMatrix02): #checks for errors first, and then calls the needed function for the required operation. Is only for operations that require two matrices.

		flag=False

		if operation==1 or operation==2: 

			if rowsInMatrix01!=rowsInMatrix02 or columnsInMatrix01!=columnsInMatrix02:

				print("Cannot perform this function on matrices with different dimensions. Please input valid matrices.")
				flag=True

		elif operation==3:

			if columnsInMatrix01!=rowsInMatrix02:

				print("The number of Columns in Matrix 1 is not equal to the number of Rows in Matrix 2.")
				flag=True

		if flag==False:

			matrix01= matrixInput(rowsInMatrix01, columnsInMatrix01)
			matrix02= matrixInput(rowsInMatrix02, columnsInMatrix02)
			print("Matrix 1 is:")
			printMatrix(matrix01)
			print("Matrix 2 is :")
			printMatrix(matrix02)

			if operation==1:
				
				sum(matrix01, matrix02)

			elif operation==2:

				sub(matrix01, matrix02)

			elif operation==3:

				product(matrix01, matrix02)
				
	def main(): 

		try:

			operation= int(input("Enter the NUMBER for the operation you wish to perform :"))

			if operation>10 or operation<1:
				raise Exception

		except Exception as e:

			print("Invalid input.")
			print(e)

		else:

			inputMatrixInfo(operation)
		
	main()
'''
	Lesson: 7
	Exersice: 1
	Author: Aleksandr Plyukhin	
'''

class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix

	def __str__(self):
		string = ""
		for r in self.matrix:
			string += " ".join(map(str,r)) + '\n'
		return string

	def __add__(self, other):
		new_matrix = Matrix(self.matrix)

		for i, r in enumerate(other.matrix):
			for j, c in enumerate(r):
				new_matrix.matrix[i][j] += c

		return new_matrix


matrix_1 = []
matrix_1.append([1,2,3])
matrix_1.append([4,5,6])
matrix_1.append([7,8,9])

matrix_2 = []
matrix_2.append([9,8,7])
matrix_2.append([6,5,4])
matrix_2.append([3,2,1])

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
print(m_1)
print(m_1 + m_2 + m_2)
''' You are given an integer, N, your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation patterns.) Examples: 
N = 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
N = 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def print_rangoli(size):
	'''
	This function implements the main logic to draw the alphabet rangoli on screen.
	Input: size -- Desired size.
	Output: Prints the  alphabet rangoli.
	'''
	width  = (size*4) - 3
	mat = []		#Stores the half of the alphabet rangoli items since the other half is the same in different order
	for i in range(size):
		line = '-'.join([str(chr(j)) for j in range(97+i, 97+size)])
		#Transforms 'a-b-c' into 'c-b-a-b-c' from line
		#line[::-1] reverses the string
		#line[1:] prints from the first position 
		mat.append((line[::-1]+line[1:]).center(width, "-"))
	#We have the half of the alphabet rangoli in mat, print the mat in reverse order and add the other half.
	print('\n'.join(mat[::-1]+mat[1:]))

if __name__ == '__main__':
	n = int(input())
	print_rangoli(n)
	

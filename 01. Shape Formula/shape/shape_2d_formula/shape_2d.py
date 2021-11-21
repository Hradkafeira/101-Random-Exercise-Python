import math

class Shape2DFormula:
	"""Collection of 2D Shape Formula"""
	def __init__(self):
		print("2D Shape Formula")

	def is_positive(self,*number):
		"""Check is the number positive or not.

		Parameters
		----------
		*number : `int` or `float`
		    non-negative number

		Returns
		-------
		check the number: boolean
			result of number is positive or not
		"""
		pos=0
		neg=0
		zero=0
		for num in number:
			if num > 0:
				pos+=1
			elif num == 0:
				zero+=1	
			else:
				neg+=1

		if zero > 0:
			print("number can't be 0")

		if len(number) == pos:
			return True
		else:
			return False

	def is_square(self,integer):
		"""Compute area of square.
			return the area of square

		Parameters
		----------
		integer : `int`
		    

		Returns
		-------
		check the number: boolean
			result of number is square or not
		
		"""
		root = math.sqrt(integer)
		return integer == int(root + 0.5) ** 2

	def square(self,a):
		"""Compute area of square.
			return the area of square

		Parameters
		----------
		a : `int` or `float`
		    input the length of area

		Returns
		-------
		area of square: `int` or `float`
			result of area of square
		"""
		if self.is_positive(a)==True:
			return a*a
		else:
			print("negative number!")
			return False

	def triangle(self,b,h):
		"""Compute area of triangle.
			return the area of triangle.

		Parameters
		----------
		b : `int` or `float`
		    base of triangle
		h : `int` or `float`
		    height of triangle

		Returns
		-------
		area of triangle: `int` or `float`
			result of area of triangle
		
		"""
		hypotenuse=b**2+h**2

		if self.is_positive(b,h)==True:
			if self.is_square(hypotenuse):
				print("90 degree triangle!!")
				return 0.5*b*h
			else:
				return 0.5*b*h
		else:
			print("negative number!")
			return False

	def circle(self,r):
		"""Compute area of circle.
			return the area of circle.

		Parameters
		----------
		r : `int` or `float`
		    radius of the circle

		Returns
		-------
		area of circle: `int` or `float`
			result of area of circle
		
		"""
		if self.is_positive(r)==True:
			return (22/7)*r*r
		else:
			print("negative number!")
			return False

	def rectangle(self,l,w):
		"""Compute area of rectangle.
			return the area of rectangle.

		Parameters
		----------
		l : `int` or `float`
		    length
		w : `int` or `float`
		    length

		Returns
		-------
		area of rectangle: `int` or `float`
			result of area of rectangle
		
		"""
		if self.is_positive(l,w)==True:
			return l*w
		else:
			print("negative number!")
			return False

	def parallelogram(self,b,h):
		"""Compute area of parallelogram.
			return the area of parallelogram.

		Parameters
		----------
		b : `int` or `float`
		    base
		h : `int` or `float`
		    heigth

		Returns
		-------
		area of parallelogram: `int` or `float`
			result of area of parallelogram
		
		"""
		if self.is_positive(b,h)==True:
			return b*h
		else:
			print("negative number!")
			return False
	
	def trapezium(self,a,b,h):
		"""Compute area of trapezium.
			return the area of trapezium.

		Parameters
		----------
		a : `int` or `float`
		    length of parallel sides
		b : `int` or `float`
		    length of parallel sides
		h : `int` or `float`
		    height

		Returns
		-------
		area of trapezium: `int` or `float`
			result of area of trapezium
		
		"""
		if self.is_positive(a,b,h)==True:
			return 1/2*(a+b)*h
		else:
			print("negative number!")
			return False
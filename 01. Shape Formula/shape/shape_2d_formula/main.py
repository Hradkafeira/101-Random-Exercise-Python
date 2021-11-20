import math

class Shape2DFormula:
	"""Collection of 2D Shape Formula"""
	def __init__(self):
		print("2D Shape Formula")
			 

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
		return a*a

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
		sisi_miring=b**2+h**2
		if self.is_square(sisi_miring):
			print("90 degree triangle!!")
			return 0.5*b*h
		else:
			return 0.5*b*h

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
		return (22/7)*r*r

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
		return l*w

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
		return b*h
	
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
		return 1/2*(a+b)*h

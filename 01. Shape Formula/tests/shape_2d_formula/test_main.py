import pytest
from shape.shape_2d_formula.main import Shape2DFormula as sd

sd=sd()

message ="must be positive number"


class TestSquare(object):

	def test_square_normal(self):		
		actual = sd.square(2)
		expected = 4
		assert actual == expected, message

	def test_square_normal2(self):		
		actual = sd.square(1.5)
		expected = 2.25
		assert actual == expected, message

class TestTriangle(object):

	def test_triangle_normal(self):		
		actual = sd.triangle(2,4)
		expected = 4
		assert actual == expected, message

	def test_triangle_normal2(self):
		actual = sd.triangle(2,3)
		expected = 3
		assert actual == expected, message

	def test_triangle_special(self):
		actual = sd.triangle(12,9)
		expected = 54
		assert sd.is_square((12*12+9*9)) == True
		assert actual == expected, message

class TestRectangle(object):

	def test_rectangle_normal(self):		
		actual = sd.rectangle(2,4)
		expected = 8
		assert actual == expected, message

	def test_rectangle_normal2(self):		
		actual = sd.rectangle(3,4)
		expected = 12
		assert actual == expected, message

class TestCircle(object):

	def test_circle_normal(self):		
		actual = sd.circle(7)
		expected = 154
		assert actual == expected, message

	def test_circle_normal2(self):		
		actual = sd.circle(21)
		expected = 1386
		assert actual == expected, message

class TestParrallelogram(object):

	def test_parallelogram_normal(self):
		actual = sd.parallelogram(20,10)
		expected = 200
		assert actual == expected, message
		
	def test_parallelogram_normal2(self):		
		actual = sd.parallelogram(1,2)
		expected = 2
		assert actual == expected, message		

class TestTrapezium(object):

	def test_trapezium_normal(self):
		actual = sd.trapezium(2,3,2)
		expected = 5
		assert actual == expected, message
		
	def test_trapezium_normal2(self):		
		actual = sd.trapezium(4,4,3)
		expected = 12
		assert actual == expected, message
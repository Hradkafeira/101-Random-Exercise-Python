import pytest
from numberone.shape_2d_formula.main import Shape2DFormula as sd

sd=sd()

class TestSquare(object):
	def test_square_normal(self):		
		assert sd.square(2) == 4
	def test_square_normal2(self):
		assert sd.square(1.5)==2.25

class TestTriangle(object):
	def test_triangle_normal(self):		
		assert sd.triangle(1,4) == 2
	def test_triangle_normal2(self):
		assert sd.triangle(2,3)==3
	def test_triangle_special(self):
		assert sd.is_square(225) == True
		assert sd.triangle(12,9)==54

class TestRectangle(object):
	def test_rectangle_normal(self):		
		assert sd.rectangle(2,4) == 8
	def test_rectangle_normal2(self):		
		assert sd.rectangle(4,4) == 16

class TestCircle(object):
	def test_circle_normal(self):		
		assert sd.circle(7) == 154
	def test_circle_normal2(self):		
		assert sd.circle(21) == 1386

class TestParrallelogram(object):
	def test_parallelogram_normal(self):		
		assert sd.parallelogram(20,10) == 200
	def test_parallelogram_normal2(self):		
		assert sd.parallelogram(1,2) == 2

class TestTrapezium(object):
	def test_trapezium_normal(self):		
		assert sd.trapezium(2,3,2) == 5
	def test_trapezium_normal2(self):		
		assert sd.trapezium(4,4,3) == 12 
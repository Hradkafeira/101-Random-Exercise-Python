from loop_shape.loop_shape import *

class TestShape(object):
    def test_cube1(self):
        actual= [*cube(4)]
        expected=['\n****', '\n****', '\n****', '\n****']
        assert actual == expected

    def test_cube2(self):
        actual= [*cube(2)]
        expected=['\n**', '\n**']
        assert actual == expected

    def test_pyramid1(self):
        actual= [*pyramid(5)]
        expected=[*reversed(['\n*****', '\n****', '\n***', '\n**', '\n*'])]
        assert actual == expected

    def test_pyramid2(self):
        actual= [*pyramid(5,False)]
        expected=['\n*****', '\n****', '\n***', '\n**', '\n*']
        assert actual == expected

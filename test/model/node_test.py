import unittest
from pacman_game.model import node
from pacman_game.model.coordinate import Coordinate

class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self.node = node.Node(Coordinate(0., 0.))

    def test_x(self):
        assert(self.node.x == 0.)

    def test_y(self):
        assert(self.node.y == 0.)

    def test_neighbours(self):
        assert(self.node.neighbours == [])

    def test_geoneighbours(self):
        assert(self.node.geoneighbours == [])

    def test_add_neighbour(self):
        n = node.Node(None)
        self.node.add_neighbour(n)
        assert(self.node.neighbours == [n])
        self.node.add_neighbour(n)
        assert(self.node.neighbours == [n])

    def test_remove_neighbour(self):
        n = node.Node(None)
        self.node.add_neighbour(n)
        self.node.remove_neighbour(n)
        assert(self.node.neighbours == [])

    def test_add_geoneighbour(self):
        n = node.Node(None)
        self.node.add_geoneighbour(n)
        assert(self.node.geoneighbours == [n])
        self.node.add_geoneighbour(n)
        assert(self.node.geoneighbours == [n])

    def test_remove_geoneighbour(self):
        n = node.Node(None)
        self.node.add_geoneighbour(n)
        self.node.remove_geoneighbour(n)
        assert(self.node.geoneighbours == [])

    def test_is_neighbour(self):
        n = node.Node(None)
        assert(self.node.is_neighbour(n) == False)
        self.node.add_neighbour(n)
        assert(self.node.is_neighbour(n) == True)
        self.node.remove_neighbour(n)
        assert(self.node.is_neighbour(n) == False)

    def test_is_geoneighbour(self):
        n = node.Node(None)
        assert(self.node.is_geoneighbour(n) == False)
        self.node.add_geoneighbour(n)
        assert(self.node.is_geoneighbour(n) == True)
        self.node.remove_geoneighbour(n)
        assert(self.node.is_geoneighbour(n) == False)

    def test_distance(self):
        n = node.Node(Coordinate(1., 0.))
        assert(self.node.distance(n) == 1.)
        assert(n.distance(self.node) == 1.)

node_tests = unittest.makeSuite(NodeTestCase, "test")

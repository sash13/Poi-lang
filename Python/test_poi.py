import unittest

from poi import PoiPoi

class PoiInterpreterTest(unittest.TestCase):

	def setUp(self):
		self.p = PoiPoi()

	def testInterpreterForwardOpCode(self):
		self.p.index = 0
		self.p.forward()
		self.assertEqual(1, self.p.index)

	def testInterpreterBackwardOpCode(self):
		self.p.index = 1
		self.p.backward()
		self.assertEqual(0, self.p.index)

	def testInterpreterIncOpCode(self):
		self.p.index = 0
		self.p.array[self.p.index] = 0
		self.p.inc(self.p.index)
		self.assertEqual(1, self.p.array[self.p.index])

	def testInterpreterDecOpCode(self):
		self.p.index = 0
		self.p.array[self.p.index] = 1
		self.p.dec(self.p.index)
		self.assertEqual(0, self.p.array[self.p.index])

if __name__ == '__main__':
	unittest.main()
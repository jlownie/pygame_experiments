import blockwarrior, unittest
from blockwarrior import getDist, worldObject

class TestGetDist(unittest.TestCase):

	def test_Up(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=5
		objB.y=7

		result = getDist(objA, objB)
		self.assertEqual(result, 2.0)

	def test_UpRight(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=7

		result = getDist(objA, objB)
		self.assertEqual(result, 2.8284271247461903)

	def test_Right(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=5

		result = getDist(objA, objB)
		self.assertEqual(result, 2.0)

	def test_DownRight(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=3

		result = getDist(objA, objB)
		self.assertEqual(result, 2.8284271247461903)

	def test_Down(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=5
		objB.y=3

		result = getDist(objA, objB)
		self.assertEqual(result, 2.0)

	def test_DownLeft(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=3

		result = getDist(objA, objB)
		self.assertEqual(result, 2.8284271247461903)

	def test_Left(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=5

		result = getDist(objA, objB)
		self.assertEqual(result, 2.0)

	def test_UpLeft(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=7

		result = getDist(objA, objB)
		self.assertEqual(result, 2.8284271247461903)
		
	def test_UpReversed(self):
		# Reverses the order the objects are sent to the function
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=5
		objB.y=7

		result = getDist(objB, objA)
		self.assertEqual(result, 2.0)

	def test_UpRightReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=7

		result = getDist(objB, objA)
		self.assertEqual(result, 2.8284271247461903)

	def test_RightReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=5

		result = getDist(objB, objA)
		self.assertEqual(result, 2.0)

	def test_DownRightReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=7
		objB.y=3

		result = getDist(objB, objA)
		self.assertEqual(result, 2.8284271247461903)

	def test_DownReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=5
		objB.y=3

		result = getDist(objB, objA)
		self.assertEqual(result, 2.0)

	def test_DownLeftReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=3

		result = getDist(objB, objA)
		self.assertEqual(result, 2.8284271247461903)

	def test_LeftReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=5

		result = getDist(objB, objA)
		self.assertEqual(result, 2.0)

	def test_UpLeftReversed(self):
		objA = worldObject()
		objA.x=5
		objA.y=5

		objB = worldObject()
		objB.x=3
		objB.y=7

		result = getDist(objB, objA)
		self.assertEqual(result, 2.8284271247461903)
if __name__ == '__main__':
    unittest.main()

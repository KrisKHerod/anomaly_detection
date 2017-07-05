import src
from src.data import Friends, Purchases

from src import load
from src import process_friend
from src import process_purchase
# from src import process_log

import unittest



class TestFeatures(unittest.TestCase):

	def test_load_single (self):
		path = './tests/log_input/test_input1.json'
		d, s = load.readFile_batch(path)

		self.assertEqual(s, {"D":"3", "T":"50"})
		self.assertEqual(d[0], {"event_type":"purchase", "timestamp":"2017-06-13 11:33:01", "id": "1", "amount": "16.83"})


	def test_load_bad (self):

		path = './tests/log_input/test_input2.json'
		d, s = load.readFile_batch(path)

		self.assertEqual(s, {"D":"3", "T":"50"})
		self.assertEqual(d, [])


	def test_befriend1 (self):

		friends_list = Friends()

		process_friend.befriend({"event_type":"befriend", "timestamp":"2017-06-13 11:33:01", "id1": "1", "id2": "2"}, friends_list)
		self.assertEqual(friends_list.friends, {"1": ["2"], "2": ["1"]})


	def test_defriend1 (self):

		friends_list = Friends()

		process_friend.befriend({"event_type":"befriend", "timestamp":"2017-06-13 11:33:01", "id1": "1", "id2": "2"}, friends_list)
		self.assertEqual(friends_list.friends, {"1": ["2"], "2": ["1"]})

		process_friend.defriend({"event_type":"defriend", "timestamp":"2017-06-13 11:33:01", "id1": "1", "id2": "2"}, friends_list)
		self.assertEqual(friends_list.friends, {"1":[], "2":[]})


	def test_purchase1 (self):

		friends_list = Friends()
		purchase_list = Purchases()

		



if __name__=='__main__':
	unittest.main()


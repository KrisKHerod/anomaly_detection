import src
from src.data import Friends, Purchases

from src import load
from src import process_friend
from src import process_purchase

import unittest
from datetime import datetime


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
		purchases_list = Purchases()
		path = "./log_output/flagged_purchases.json"

		process_purchase.purchase({"event_type":"purchase", "timestamp":"2017-06-13 11:33:01", "id": "1", "amount": "59.28"}, {'T': 50, 'D':2}, path, friends_list, purchases_list, True)
		self.assertEqual(purchases_list.purchases, {"1": [(datetime(2017, 6, 13, 11, 33, 1), 59.28)]})


	def test_purchase2 (self):

		friends_list = Friends()
		purchases_list = Purchases()
		path = "./tests/log_output/flagged_purchases.json"
		batch_path = './tests/log_input/test_input3.json'

		with open(path, 'w') as f: pass

		data, settings = load.readFile_batch(batch_path)

		for index, item in enumerate(data):
			if item['event_type'] == 'befriend':
				process_friend.befriend(item, friends_list)

			elif item['event_type'] == 'purchase':
				process_purchase.purchase(item, settings, path, friends_list, purchases_list, False)

			elif item['event_type'] == 'unfriend':
				process_friend.defriend(item, friends_list)



		process_purchase.purchase({"event_type":"purchase", "timestamp":"2017-06-13 11:33:02", "id": "2", "amount": "1601.83"}, {'T': 50, 'D':2}, path, friends_list, purchases_list, True)
		
		with open('./tests/log_output/flagged_purchases.json') as test: test = test.read()
		with open('./tests/log_output/test_output3.json') as real: real = real.read()

		self.assertEqual(test, real)




if __name__=='__main__':
	unittest.main()


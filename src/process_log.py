# build initial state of the user network as well as the purchase history
# i need to check if the last purchase is more than 3 standard deviations
# higher than the mean of the last T purchases over the dth degree network

# I need to find out their dth degree network
# I need the last tth purchases for all ids
# one dictionary with all user friends to the dth degree
# one dictionary with all the last purchases
# for new purchases check all the friends, average their purchases


import os
import sys
import json


# import data classes
from data import Friends, Purchases

import process_friend
import process_purchase
import load




def init (path):

	# check if the path exists and create a new file
	if os.path.isfile(path):
		with open(path, 'w') as f:
			pass
	else:
		with open(path, 'w') as f:
			pass





# this function will iterate through the lines of the file
def main (data, settings, path, friends_list, purchases_list):

	for index, item in enumerate(data):
		if item['event_type'] == 'befriend':
			process_friend.befriend(item, friends_list)

		elif item['event_type'] == 'purchase':
			process_purchase.purchase(item, settings, path, friends_list, purchases_list)

		elif item['event_type'] == 'defriend':
			process_friend.defriend(item, friends_list)







if __name__ == "__main__":

	# print (paths)
	paths = sys.argv

	# get the path names
	filename = paths[0]
	batch_path = paths[1]
	stream_path = paths[2]
	output_path = paths[3]

	# check the output path
	init(output_path)


	# initialize the data storage classes
	friends_list = Friends()
	purchases_list = Purchases()


	# read the batch file
	data, settings = load.readFile_batch(paths[1])
	main(data, settings, paths[3], friends_list, purchases_list)


	# read the stream file
	data = load.readFile_stream(paths[2])
	main(data, settings, paths[3], friends_list, purchases_list)

	# print (friends_list.friends)
	# print (purchases_list.purchases)




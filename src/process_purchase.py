
from datetime import datetime



def calculate_anomaly (item, settings, path, friends_list, purchases_list):

	# # calculate the mean of the whole network

	# not including users own purchase
	# i need to get the top T purchases from the entire network

	# empty network purchases list
	network_purchases = []
	# empty network friends list to check if the friend exists twice
	network_friends = []

	# check if the user has any friends
	if len(friends_list.friends[item['id']]) > 0:

		# add the 1st degree freinds to the
		friend_ids = friends_list.friends[item['id']]

		for degree in range(int(settings['D'])):

			# create a list to contain the ids of the next degree of friends
			if degree != 0: friend_ids = next_friend_ids
			next_friend_ids = []

			# iterate through the ids of the friends
			for ids in friend_ids:

				if ids == item['id']: continue

				# make sure that the id has not already been processed and that the id exists in the purchases list
				if ids not in network_friends and ids in purchases_list.purchases.keys():
					network_friends.append(ids)
					# add the last T purchases of that user to the network purchases list
					network_purchases += purchases_list.purchases[ids]

				# get the ids of the friends of that friend and add them into the next degree list
				if ids in friends_list.friends.keys():
					next_friend_ids = next_friend_ids + friends_list.friends[ids]

	else:
		return 0

	


	# check if there are enough purchases to calculate the anomaly
	if len(network_purchases) < 2: return 0

	# sort the purchases by timestamp
	network_purchases = sorted(network_purchases)
	
	# select the top "T" purchases from the whole network
	network_purchases = network_purchases[:int(settings['T'])]
	# separate the timestamps from the amounts
	timestamps, network_purchases = zip(*network_purchases)
	print (network_purchases)


	# calculate the mean of the top "T" purchases
	mean = sum(network_purchases)/float(len(network_purchases))
	# calculate the sd of the top "T" purchases
	sd = (sum([(x-mean)**2 for x in network_purchases])/float(len(network_purchases)))**0.5


	print (mean, sd, item['amount'])

	# check if the amount is greater than 3 standard deviations of the mean of the users social network
	if float(item['amount']) > mean+3*sd:

		# create the data to be written to the output file
		line = '{"event_type": "purchase", "timestamp": "' + item["timestamp"] + '", "id": "' + item["id"] + '", "amount": "' + item['amount'] + '", "mean": "%0.2f", "sd": "%0.2f"}\n' %(mean, sd)
		# print (line)
		with open(path, 'a') as f:
			f.write(line)









# this function will handle purchases
def purchase (item, settings, path, friends_list, purchases_list, stream):

	# check if user exists in purchases
	if item['id'] in purchases_list.purchases.keys():
		pass
	else:
		purchases_list.purchases[item['id']] = []


	# check that the length is greater than the Tracked number
	if len(purchases_list.purchases[item['id']]) < int(settings['T']):
		purchases_list.purchases[item['id']].append((datetime.strptime(item['timestamp'], '%Y-%m-%d %H:%M:%S'), float(item['amount'])))
	else:
		purchases_list.purchases[item['id']].pop(0)
		purchases_list.purchases[item['id']].append(float(item['amount']))


	# check if the current item is part of batch or streaming
	if stream:

		if item['id'] in friends_list.friends.keys():
			calculate_anomaly(item, settings, path, friends_list, purchases_list)




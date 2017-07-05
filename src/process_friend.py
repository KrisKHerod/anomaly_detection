
# this function handles the case when a friend request
def befriend (item, settings, friends_list):

	# check if id1 is in the overall friends_list dictionary
	if item['id1'] in friends_list.friends.keys():
		pass
	else:
		friends_list.friends[item['id1']] = []

	# append id2 to id1 friends list
	friends_list.friends[item['id1']].append(item['id2'])


	# check if id2 is in the overall friends_list dictionary
	if item['id2'] in friends_list.friends.keys():
		pass
	else:
		friends_list.friends[item['id2']] = []

	# append id1 to id2 friends list
	friends_list.friends[item['id2']].append(item['id1'])

	return 0





def defriend(item, settings, friends_list):

	# check the id1 friend list and remove the id2 from that list
	for i, ids in enumerate(friends_list.friends[item['id1']]):
		if ids == item['id2']:
			del friends_list.friends[item['id1']][i]
			break

	# check the id2 friend list and remove id1 from that list
	for i, ids in enumerate(friends_list.friends[item['id2']]):
		if ids == item['id1']:
			del friends_list.friends[item['id2']][i]
			break

	return 0



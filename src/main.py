

# this function will iterate through the lines of the file
def main (data, settings, path, friends_list, purchases_list, stream):

	for index, item in enumerate(data):
		if item['event_type'] == 'befriend':
			process_friend.befriend(item, friends_list)

		elif item['event_type'] == 'purchase':
			process_purchase.purchase(item, settings, path, friends_list, purchases_list, stream)

		elif item['event_type'] == 'unfriend':
			process_friend.defriend(item, friends_list)



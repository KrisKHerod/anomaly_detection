import json


# Read the batch file which contains settings which contains friending/defriending events, and purchase events.
def readFile_batch (path):
	# store data in list
	data = []

	# check that keys exist
	type1 = ['amount', 'event_type', 'timestamp', 'id']
	type2 = ['event_type', 'timestamp', 'id1', 'id2']
	type3 = ['D', 'T']

	# open the file
	with open(path, 'r') as file:
		for index, line in enumerate(file):

			line = json.loads(line)
			

			if index == 0:
				# check that the first line has the settings
				if all(key in line for key in type3):
					settings = line
				else:
					# if the settings are not defined then create the default
					settings = {'T': 2, 'D': 1}
					pass


			else:
				# check that the right keys are in the dictionary
				if all(key in line for key in type1) or all(key in line for key in type2):
					data.append(line)
				else:
					pass


	return data, settings


# Reads the stream file which contains all of the settings.
def readFile_stream(path):

	data = []

	type1 = ['amount', 'event_type', 'timestamp', 'id']
	type2 = ['event_type', 'timestamp', 'id1', 'id2']

	with open(path, 'r') as file:
		for index, line in enumerate(file):

			line = json.loads(line)

			# check that the right keys are in the dictionary
			if all(key in line for key in type1) or all(key in line for key in type2):
				data.append(line)
			else:
				pass

	return data
	



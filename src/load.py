import json


# read the file

def readFile_batch (path):

	data = []
	# check that keys exist
	type1 = ['amount', 'event_type', 'timestamp', 'id']
	type2 = ['event_type', 'timestamp', 'id1', 'id2']
	type3 = ['D', 'T']

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



def readFile_stream(path):

	data = []

	with open(path, 'r') as file:
		for index, line in enumerate(file):

			line = json.loads(line)

			# check that the right keys are in the dictionary
			if all(key in line for key in type1) or all(key in line for key in type2):
				data.append(line)
			else:
				pass

	return data
	



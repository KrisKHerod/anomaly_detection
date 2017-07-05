import json


# read the file

def readFile_batch (path):

	data = []

	with open(path, 'r') as file:
		for index, line in enumerate(file):

			line = json.loads(line)

			if index == 0:
				settings = line
			else:
				data.append(line)

	return data, settings



def readFile_stream(path):

	data = []

	with open(path, 'r') as file:
		for index, line in enumerate(file):

			line = json.loads(line)
			data.append(line)

	return data
	

import numpy as np
import random
import os

data_dir = "./bio_datasets/"

datasets = os.listdir(data_dir)

# datasets = ["Blakeley"]

# datasets = ["Usoskin", "Jurkat"]
# datasets = ["Usoskin"]


def write_to_file(all_rated, all_unrated, name, min_unrated):
	random.shuffle(all_rated)
	
	train = open(data_dir+name+"/"+name+".train.rating", "a+")
	for i in range(len(all_rated)-1):
		# train.write()
		to_write = str(all_rated[i][0]) + "\t" + str(all_rated[i][1]) + "\t" + str(all_rated[i][2]) + "\t" + "100\n"
		train.write(to_write)
	train.close()

	test = open(data_dir+name+"/"+name+".test.rating", "a+")
	to_write = str(all_rated[-1][0]) + "\t" + str(all_rated[-1][1]) + "\t" + str(all_rated[-1][2]) + "\t" + "100\n"
	test.write(to_write)
	test.close()

	random.shuffle(all_unrated)
	negative = open(data_dir+name+"/"+name+".test.negative", "a+")
	to_write = "(" + str(all_rated[-1][0]) + "," + str(all_rated[-1][1]) + ")\t" 
	negative.write(to_write)
	to_write = ""
	for i in range(min_unrated):
		if i!=min_unrated-1:
			to_write+=(str(all_unrated[i][1])+"\t")
		else:
			to_write+=(str(all_unrated[i][1])+"\n")
	negative.write(to_write)
	negative.close()



def read_file(pth):
	mat = []
	num_users = None
	with open(pth, "r") as f:
		line = f.readline()
		num_users = len(line.split(","))
		# print line
		print num_users
		line = f.readline()
		# print line
		while line!=None and line!="":
			vals = line.strip().split(",")[1::]
			# print vals
			# break
			rate = [int(vals[i]) for i in range(num_users)]
			# print rate
			# break
			mat.append(rate)
			line = f.readline()

	# print len(mat)
	mat = np.array(mat)
	# print mat

	mat = mat.T
	print mat.shape
	return mat


def read_all():
	for d, data in enumerate(datasets):
		print data, d+1, len(datasets)

		path = "./scRNA-seq datasets/"+ data + "_raw_data.csv"
		
		matrix = read_file(path)
		# print len(matrix)
		print matrix.shape
		# exit(0)
		all_rated = []
		
		unrated = []
		for i in range(len(matrix)):
			# print len(matrix[i])
			cur_unrated = 0
			for j in range(len(matrix[i])):
				if matrix[i][j]==0:
					cur_unrated+=1
			# print cur_unrated
			unrated.append(cur_unrated)

		min_unrated = min(unrated)
		# print min_unrated
		min_unrated = min(999, min_unrated)
		for i in range(len(matrix)):
			print data, i+1, len(matrix)
			all_rated = []
			all_unrated = []
			print len(matrix[i])
			for j in range(len(matrix[i])):
				if matrix[i][j]!=0:
					all_rated.append((i, j, matrix[i][j]))
				else:
					all_unrated.append((i, j, matrix[i][j]))
			write_to_file(all_rated, all_unrated, data, min_unrated)
		print

read_all()
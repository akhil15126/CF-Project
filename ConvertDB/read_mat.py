import scipy.io
import os
import random

data_dir = "./bio_datasets/"

datasets = os.listdir(data_dir)

# print datasets

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

def read_all():
	for d, data in enumerate(datasets):
		print data, d+1, len(datasets)
		fname = os.listdir(data_dir+data)[0]
		mat = scipy.io.loadmat(os.path.join(data_dir+data, fname))
		# print (mat)
		# print (type(mat))
		# print mat.keys()
		# print type(mat['Xrec'])

		# print mat['Xrec'].shape
		matrix = mat['Xrec']

		# print len(matrix)
		
		# all_rated = []
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
		for i in range(len(matrix)):
			print data, i+1, len(matrix)
			all_rated = []
			all_unrated = []
			for j in range(len(matrix[i])):
				if matrix[i][j]!=0:
					all_rated.append((i, j, matrix[i][j]))
				else:
					all_unrated.append((i, j, matrix[i][j]))
			write_to_file(all_rated, all_unrated, data, min_unrated)
		print


# mat = scipy.io.loadmat(os.path.join(data_dir+"Blakeley", "rec.mat"))

# matrix = mat['Xrec']

# unrated = []

# for i in range(len(matrix)):
# 			# print len(matrix[i])
# 	cur_unrated = 0
# 	for j in range(len(matrix[i])):
# 		if matrix[i][j]==0:
# 			cur_unrated+=1
# 	# print cur_unrated
# 	unrated.append(cur_unrated)

# print unrated

def unrate_read_all():
	cur_datasets = ['Blakeley']
	# cur_datasets = ['Blakeley', 'Jurkat']
	# cur_datasets = ['Jurkat']
	for d, data in enumerate(cur_datasets):
		print data, d+1, len(cur_datasets)
		fname = os.listdir(data_dir+data)[0]
		mat = scipy.io.loadmat(os.path.join(data_dir+data, fname))
		# print (mat)
		# print (type(mat))
		# print mat.keys()
		# print type(mat['Xrec'])

		print mat['Xrec'].shape
		matrix = mat['Xrec']

		# print len(matrix)
		
		# all_rated = []
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
		print min_unrated

		for i in range(len(matrix)):
			print data, i+1, len(matrix)
			all_rated = []
			all_unrated = []
			for j in range(len(matrix[i])):
				if matrix[i][j]!=0:
					all_rated.append((i, j, matrix[i][j]))
				else:
					all_unrated.append((i, j, matrix[i][j]))
			if min_unrated==0:
				if len(all_unrated)==0:
					# print "here", len(matrix[i])
					all_unrated.append((i, len(matrix[i]), 0))
				write_to_file(all_rated, all_unrated, data, min_unrated+1)
			else:
				write_to_file(all_rated, all_unrated, data, min_unrated)
		print

# unrate_read_all()

def get_shapes():
	for d, data in enumerate(datasets):
		print data, d+1, len(datasets)
		fname = os.listdir(data_dir+data)[0]
		mat = scipy.io.loadmat(os.path.join(data_dir+data, fname))
		# print (mat)
		# print (type(mat))
		# print mat.keys()
		# print type(mat['Xrec'])

		# matrix = mat['Xrec']
		print mat['Xrec'].shape

get_shapes()
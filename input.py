import os
os.chdir("F:\Gan\char-rnn-tensorflow-master")
stdlibloc = "'C:\\Program Files\\Python35\\lib"
max_file=100
count=0
with open("input.txt","a",encoding="utf-8") as input_f:
	for path,directories, files in os.walk(stdlibloc):
		for file in files:
			count+=1
			if count > max_files:
				break
			elif ".py" in files:
				break
			try:
				with open(os.path.join(path,file),"r") as data_f:
					contents = data_f.read()
				input_f.write(contents)
				input_f.write('\n')
			except Exception as e:
				print(str(e))
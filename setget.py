'''

'''
def main():
	f = open('input.txt', 'r+')
	sg = open('output.txt', 'w')

	variabel = []
	setter = []
	getter = []

	for line in f:
		arr = line.split()

		cont = arr[0]
		nama = arr[2][:-1]
		tipedata = arr[1]
		paramInput = nama[0].lower() + nama[1:]

		varx = cont + ' var ' + nama + ': ' + tipedata + '!'
		variabel.append(varx)

		setx = cont + ' func set' + nama.title() +'('+ paramInput +': ' + tipedata + ') { \n\tself.'+ nama +' = '+ paramInput + '\n}'
		setter.append(setx)

		getx = cont + ' func get'+ nama.title() +'() -> ' + tipedata + ' {\n\treturn ' + nama + '\n}'
		getter.append(getx)
		

	for i in variabel:
		sg.write(i+'\n')

	sg.write('\n')

	for i in setter:
		sg.write(i+'\n\n')

	sg.write('\n')

	for i in getter:
		sg.write(i+'\n\n')

if __name__ == '__main__':
		main()	
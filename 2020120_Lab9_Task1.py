def dcprt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result = result + chr((ord(char) - s-65) % 26 + 65)
		else:
			result = result + chr((ord(char) - s - 97) % 26 + 97)

	return result

def encrpt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result


text = "DEFENDTHEFORT"
s = 7
print ("\n")

enc = encrpt(text,s)
dec = dcprt(enc,s)
a =int( input())
print(a,'sll oin youtr')
print (f"Original Text: {text}")
print (f"Shift : {s}")
print (f"Encrypted Text: {enc}")
li = [i+i for i in range(10)]
print(li)
print (f"Encrypted Text : {enc}")
print (f"Shift : {s}")
print (f"Original Text: {dec}")

print("This is a Change!@!!!!!!!")

print("These are changes from GIT UI!"+str(2))
print("Hello again World!")


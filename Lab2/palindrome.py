def palindrome():
	x = raw_input("Type in a word!:)")
	if x==x[::-1]:
		return True
	else:
		return False
print palindrome()



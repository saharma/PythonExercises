def valid(isbn):
	if len(str(isbn)) == 13:
		if isbn.count("-"):
			return True
		return False
	return False

print(valid("0-102-466-674"))			
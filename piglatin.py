def pigLatin(text):
	translatedText = ''
	words = []
	words = text.split(' ')
	for word in words:
		if word[0].lower() in 'aeiouy':
			translatedText += word.lower() + 'yay '
		else:
			firstVowelIndex = 0
			for letterIndex in range(len(word)):
				if word[letterIndex].lower() in 'aeiouy':
					firstVowelIndex = letterIndex
					break
			translatedText += word[firstVowelIndex:].lower() + word[:firstVowelIndex].lower() + 'ay '
	return translatedText
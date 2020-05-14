def highlight_word(sentence, word):
    if word in sentence:
        toChange = sentence.index(word)
        sentence = sentence[:toChange] + word.upper()
        return(sentence)
        #return word
	#return(___)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
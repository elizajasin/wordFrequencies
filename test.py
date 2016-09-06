__author__ = 'elizajasin'

text_file = open('coba.txt','r')

wordstring = text_file.read()

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")

text_file.close()
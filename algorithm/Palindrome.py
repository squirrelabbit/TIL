word = input()
reverse_word = ''

for idx in range(len(word)-1,-1,-1):
	reverse_word +=word[idx]
	
if word == reverse_word:
	print(1)
else:
    print(0)
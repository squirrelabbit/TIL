T = int(input())
for tc in range(1, T + 1):
	NM = list(map(int,input().split()))
	N = NM[0]
	M = NM[1]
	array = []
##############2차원배열만들기###########
	for i in range(N):
		row = input()
		row_list = []
		for j in range(N):
			row_list.append(row[j])
		array.append(row_list)
##########################################3 M길이의 문자열 만들기	
	for i in range(N):
		for j in range(N-M+1):
			word_h = [] #가로문자열
			word_v = [] #세로문자열
			for k in range(M):
				word_h.append(array[i][k+j]) 
				word_v.append(array[j+k][i])
############################################## 회문확인
			reverse_word_h = word_h[::-1]
			
			if word_h == reverse_word_h:
				answer = "".join(word_h)
				break
			
			reverse_word_v = word_v[::-1]

			if word_v == reverse_word_v:
				answer = "".join(word_v)
				break
###############################################답출력
	print(f'#{tc} {answer}')
	


cards = [4, 8, 7, 3, 1, 5, 5, 6]
cards_count=[0]*10
for card in cards :
    cards_count[card]+=1

answer_run=[]


for j in range(len(cards_count)-2):
    for i in cards_count[j:j+3]:
        if i ==0:
            answer_run.append(0)
        else :
            answer_run.append(1)
if 1 in answer_run:
    print("run!")
    


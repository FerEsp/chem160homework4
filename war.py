from cards import*
from collections import Counter
ntrials=10000
list=[]
for i in range(ntrials):
    deck1=deck()
    deck1.shuffle()
    deck2=deck()
    deck2.shuffle()
    p1=0
    p2=0
    while deck1.cardsleft()!=0 and deck2.cardsleft()!= 0:
        card1=deck1.dealcard()
        card2=deck2.dealcard()
        if card1.value()>card2.value():
            p1+=2
        if card2.value()>card1.value():
            p2+=2
        if card2.value()== card1.value():
            p1+=1
            p2+=1
    if p1>p2:
        list.append(p1-p2)
    if p2>p1:
        list.append(p2-p2)
    if p1==p2:
        list.append(0)
for j in range(53):
    print(j , list.count(j)/ntrials )
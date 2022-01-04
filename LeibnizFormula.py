#v1.0
a=1
check=1 #(1 for positives, 0 for negatives)
negatives=[]
positives=[]
for i in range (100): # (getting closer to pi with each steps.)
    num=1/a
    if check==1:
        check=0
        positives.append(num)
        a+=2
    else:
        check=1
        negatives.append(num)
        a+=2
total_positives=0
for i in positives:    
    total_positives+=i
total_negatives=0
for i in negatives:
    total_negatives+=i
print(4*(total_positives-total_negatives))

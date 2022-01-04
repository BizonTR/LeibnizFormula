#v1.1
a=1
check=1 #(1 for positives, 0 for negatives)
numbers=[]
for i in range (100): # (getting closer to pi with each steps.)
    num=1/a
    if check==1:
        check=0
        numbers.append(num)
        a+=2
    else:
        check=1
        numbers.append(-num)
        a+=2
total_numbers=0
for i in numbers:    
    total_numbers+=i
print(4*total_numbers)
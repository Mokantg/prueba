import time
h=0
m=0
s=0

while (h<=23):
    m=0
    while (m<60):
        s=0
        while(s<60):
            print(f'{h} : {m} : {s}')
            time.sleep(1)
            s+=1
        m+=1
    h+=1
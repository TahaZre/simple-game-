import time 

for i in range(1,12):
    if i % 5 == 0:
        time.sleep(1)
        print('hop')
    else:
        time.sleep(1)
        print(i)    

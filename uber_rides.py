import random
import math as m
rate = float(input('what is your uber rating (out of 5)?=> '))
num_rates = int(input('how many rating do you have? => '))
target_rating = float(input('what is your targat rating (out of 5)? => '))
five = int(input("how likely are you to get a 5?(from range 1 to 10) => "))
five = five / 10
num_rates = 100
rating_list = [rate] * num_rates
count = 0
total_count = []
rating = 0
t = time.time()
checker = True
for i in range(100):
    count = 0
    U_rating = rating_list.copy()
    avg_rating = sum(U_rating)/len(U_rating)
    while avg_rating < target_rating:
        person_rate = random.random()
        if person_rate <= .85:
            U_rating.append(5)
        elif .85 < person_rate <= .9:
            U_rating.append(4)
        elif .9 < person_rate <= .95:
            U_rating.append(3)
        else:
            rate_list = [1,2]
            rate = random.choice(rate_list)
            U_rating.append(rate)
        count += 1
        avg_rating = round(sum(U_rating)/len(U_rating),2)
        if len(U_rating) == 10000:
            checker = False
            break
    if checker == False:
        break
        
    total_count.append(count)
if checker == False:
    print('not going to happen')
else:
    
    avg_drives = sum(total_count)/len(total_count)
    drives = m.ceil(avg_drives)
    #print(total_count)
    print('it well take you about {} rides to reach this goal'.format(drives))
    print('At least: {} drives'.format(min(total_count)))
    print('At most: {} drives'.format(max(total_count)))
      

    
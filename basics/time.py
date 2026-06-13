import time
timestamp_h = time.strftime("%H")
timestamp_m = time.strftime("%M")
timestamp_s = time.strftime("%S")
ti = int(timestamp_h)
ti2 = int(timestamp_m)
ti3 = int(timestamp_s)
#print("Time is ",ti,"-",ti2,"-",ti3)

if 12>=ti>=0:
    print("Good Morning")
elif 15>=ti>12:
    print("Good Afternoon")
else: print("Good Night")

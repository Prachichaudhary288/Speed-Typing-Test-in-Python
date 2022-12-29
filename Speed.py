from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

test=["A teacher is called builder of the nation. The profession of teaching needs men and women with qualities of head and heart.",
      "Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher.",
      "Recently, an exhibition ‘Building A New India’ was held in the capital. It was organized by the Ministry of Information and Broadcasting, Government of India."]
test1=r.choice(test)
print("  ***** typing speed *****  ")
print(test1)
print()
print()
time_1=time()
testinput=input(" Enter : ")
time_2=time()

print('Speed:',speed_time(time_1,time_2,testinput),"w/sec")
print("Error:",mistake(test1,testinput))
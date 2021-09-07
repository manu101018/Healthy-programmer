from pygame import mixer
import datetime
import time

def  getdate():
    return datetime.datetime.now()



def musicloop(file,stopper):
    
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        a =input()
        if  a == stopper:
            mixer.music.stop()
            break
        
            
while True:
    time.sleep(5)
    print(f"Drink water ")
    musicloop("water.mp3", "w")
    
    with open("water_routine_report.exe","a") as wrr:
        wrr.write(str(str(getdate()))+"\n")
        print("Good\n")

    
    time.sleep(5)
    print("eyes exercise time")
    musicloop("eyes.mp3","e")
    with open("eyes_exr_data.exe","a") as eed:
        eed.write(str(str(getdate()))+"\n")
        print("Good\n")

    time.sleep(5)
    print("Exercise time")
    musicloop("exercise.mp3","e")
    with open("exr_routine_data","a") as erd:
        erd.write(str(str(getdate()))+"\n")
        print("Good\n")
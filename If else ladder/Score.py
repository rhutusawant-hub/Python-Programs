pcm = int(input("Enter your PCM score : "))
pcb = int(input("Enter your PCB score : "))

if(pcm > 145) or (pcb < 145):
    print("Tu engineering/pharmacy kar sakta hai ")
elif(pcm > 120) or (pcb < 120):
    print("Kuch jugaad ho skata hai!")
elif pcb > 0:
    print("Pharmacy kar!!")
else:
    print("BSC lele")
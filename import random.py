import random
b=0
while True:
    a=random.choice(range(1,101))
    print(a)
    b=b+1
    if a<30:
        print(f"运行了{b}次")          #运行次数   
        break


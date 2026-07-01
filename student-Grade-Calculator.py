name=[""]*5
mark=[""]*5
print("Welcome to grade calc")
for i in range(5):
 
 name[i]=input("Enter your name: ")
 mark[i]=int(input("Enter your mark: "))

for i in range (5): 
 if 100>mark[i]>80:
    grade="A"
    print(f"Grade :{grade} for :{name[i]}")

 elif 79>mark[i]>70:
    grade="B"
    print(f"Grade :{grade} for :{name[i]}")
 elif 69>mark[i]>60:
    grade="C"
    print(f"Grade :{grade} for :{name[i]}")      

 elif 59>mark[i]>50:
    grade="D"
    print(f"Grade :{grade} for :{name[i]}") 
 else:
    grade="F"
    print(f"Grade :{grade} for :{name[i]}")     
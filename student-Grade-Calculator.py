name = [""] * 5
mark = [0] * 5

print("Welcome to Grade Calculator")

for i in range(5):
    name[i] = input("Enter your name: ")

    while True:
        try:
            mark[i] = int(input("Enter your mark: "))

            if 0 <= mark[i] <= 100:
                break
            else:
                print("Enter a mark between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")

for i in range(5):
    if mark[i] >= 80:
        grade = "A"
    elif mark[i] >= 70:
        grade = "B"
    elif mark[i] >= 60:
        grade = "C"
    elif mark[i] >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"{name[i]} scored {mark[i]} and got Grade {grade}")

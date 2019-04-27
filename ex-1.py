num = input("Enter the number: ")
n = int(num)
if n > 1 and n % 2 == 0:
    if 2 <= n <= 5:
        print("Not weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not weird")
else:
    print("Weird")
quit()

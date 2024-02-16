welcome =int( input("Welcome to the tip calculator!\n What was the total bill?\n"))
percent = int(input("what percentage tip would you like to give? 10 , 12  or 20?\n"))
remain = int(welcome)-int(percent)
people = int(input("How many people to split the bill?\n"))
total = int(remain) / int(people)



print(f"Each person will pay {total}")

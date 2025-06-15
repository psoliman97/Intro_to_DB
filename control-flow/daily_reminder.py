task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))
match priority :
    case "high" :
            print (f"Reminder:{task} is a high priority task") 
    case "medium" :
            print (f"Reminder:{task} is a medium priority task") 
    case "low" :
            print (f"Reminder:{task} is a low priority task") 
    case _ :
         print (f"Reminder:{task} is a Unknown priority task") 

if time_bound == "yes":
    print (" This task requires immediate attention today!") 
else :
      print()

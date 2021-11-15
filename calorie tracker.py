# Prompt user for total calories consumed for the day.
calories = int(input("How many calories did you consume today?\n"))

# Store in two variables the amount of average calories burned in one mile and per a tenth of a mile. 
calories_mile = 100  
tenth_mile = 10

# Prompt user for how many miles ran for today.
miles = float(input("How many miles did you run today?\n"))

# If the value for miles is a float multiply the float value by the number of calories in one-tenth of a mile.
if miles == float:
     float * tenth_mile

# Multiply calories per mile by the value for miles. Subtract daily calorie input by calories burned and store in a variable.   
calories_burned = int(calories_mile * miles)
new_total = calories - calories_burned

# Display how many calories are burned off the total calorie intake. 
print("You have burned",calories_burned, "calories of today's total calorie intake of" , calories)

# Display the number of miles ran for today and display the new total calorie count after subtracting the burned calories.
print("After running" ,miles, "miles your new total calorie count for today is" ,new_total)

# Prompt user for how many miles they expect to run tomorrow. Multiply that value by calories in a mile and store in a variable.
miles_tomorrow = float(input("This is a good start, now how many miles do you plan to run tomorrow?\n"))
calories_tomorrow = int(miles_tomorrow * calories_mile)

# If the amount of miles expected to run tomorrow is greater than today display a message showing how many calories would be burned tomorrow. 
if miles_tomorrow > miles:
    print("Awesome! you are motivated. That would be" ,calories_tomorrow, "calories burned tomorrow")
# If the amount of miles expected to run tomorrow is less than today dispaly a message telling the user to push for more miles in the future.    
elif miles_tomorrow < miles:
    print("You do deserve a break after today but try to push for longer distance in the future.")
# If the amount of miles expected for tomorrow is the same as today display a message for being consistent.
elif miles_tomorrow == miles:
    print("Way to go on being consistent!")

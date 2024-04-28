# Display a list of months to the user
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

# Request input from the user to enter the name of a month and assign it to the variable 'month_name'
month_name = input("Input the name of Month: ")

# Check the input 'month_name' and provide the number of days based on the entered month
if month_name == "February":
    print("No. of days: 28/29 days")  # Display the number of days in February (28 or 29 days for leap years)
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")  # Display the number of days for months having 30 days
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")  # Display the number of days for months having 31 days
else:
    print("Wrong month name")  # If the entered month name doesn't match any of the above conditions, display an error message 

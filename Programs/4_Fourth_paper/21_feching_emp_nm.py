'''21. Imagine a scenario where you are required to fetch the employee names who joined after 02 Sep 2022 and location is Hyderabad
empIoyee_ data = {
“priya”:{“location”	: “Hyderabad” “joining_date” :“05/09/2022” },
“mahi”: {“location”: “Bangalore” “joining_date”: “20/02/2023”}, 
“raja”: {“location”	: “Hyderabad”, “joining_date” : “14/10/2022”},
“prabhu”:{“location”: “Bangalore” “joining_date” : “02/01/2023”}
}
'''

employee_data = {
    "priya": {"location": "Hyderabad", "joining_date": "05/09/2022"},
    "mahi": {"location": "Bangalore", "joining_date": "20/02/2023"},
    "raja": {"location": "Hyderabad", "joining_date": "14/10/2022"},
    "prabhu": {"location": "Bangalore", "joining_date": "02/01/2023"}
}


employees = []                                      # Initialize a list to store the names of eligible employees
for name, data in employee_data.items():            # Iterate through the dictionary    
    if data["location"] == "Hyderabad" and data["joining_date"] > "02/09/2022": # Check if the location is Hyderabad and the joining date is after 02 Sep 2022
        employees.append(name)

print(f'name of the employees whose location Hyd and joining date after 02/09/2022: {employees}' )           # Print the list of eligible employees


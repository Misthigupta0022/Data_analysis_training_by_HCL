import pandas as pd
import numpy as np
salary_series = pd.Series([50000, 60000, 70000, 80000, 90000])
print(salary_series)

employee_data = {
     "Employee_ID" : [101, 102, 103, 104, 105],
     "Employee_Name" : ["Diya", "Janvi", "Dolly", "Smita", "Isha"],
     "Department" : ["HR", "Finance", "IT", "Marketing", "Sales"],
     "City": ["Chennai", "Bangalore", "Hyderabad", "Pune", "Mumbai"],
     "Salary" : [50000, 60000, 70000, 80000, 90000],
     "Experience" : [2, 3, 4, 5, 6],
     "Rating" : [4.5, 4.2, 4.8, 4.1, 4.6]
}
employee_df = pd.DataFrame(employee_data)
print(employee_df)
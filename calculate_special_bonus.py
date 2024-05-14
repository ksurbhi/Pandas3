# Calculate Special Bonus
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # result = []
    # for i in range(len(employees)):
    #     emp_id = employees['employee_id'][i]
    #     name = employees['name'][i]
    #     if emp_id %2 != 0 and name[0] != 'M':
    #         result.append([emp_id,employees['salary'][i]])
    #     else:
    #         result.append([emp_id, 0])
    # df = pd.DataFrame(result, columns = ['employee_id','bonus'])
    # return df.sort_values(by = 'employee_id')
    for i in range(len(employees)):
        emp_id = employees['employee_id'][i]
        name = employees['name'][i]
        if emp_id % 2 == 0 or name[0] =='M':
            employees['salary'][i] = 0
    df =  employees[['employee_id','salary']].rename(columns = {'salary':'bonus'})
    return df.sort_values(by = 'employee_id')

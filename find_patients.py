import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # result = []
    # for i in range(len(patients)):
    #     p_id = patients['patient_id'][i]
    #     name = patients['patient_name'][i]
    #     cond = patients['conditions'][i]
    #     for condition in cond.split():
    #         if condition.startswith('DIAB1'):
    #             result.append([p_id,name,cond])
    #             break
    # print(result)
    # df = pd.DataFrame(result, 
    # columns = ['patient_id','patient_name','conditions'])
    # return  df

# using st.startswith('DIAB1') and str.contains(' DIAB1')
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # df = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    # return df

# Using str.contains(r'\bDIAB1',regex = True)
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.contains(r'\bDIAB1', regex = True)]
    return df
    

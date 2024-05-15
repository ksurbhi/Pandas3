def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper()  + users['name'].str[1:].str.lower()
    print(users['name'].str[0])
    return users.sort_values(by='user_id')
# using st.capitalize() method
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id')

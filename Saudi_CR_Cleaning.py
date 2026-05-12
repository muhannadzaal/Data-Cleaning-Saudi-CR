import pandas as pd

def clean_data(df):
    
    df = df.drop(columns=['Main_CR_Number'])
    
    df = df.fillna({'Capital': 0})
    
    df['CR_Type'] = df['CR_Type'].str.strip()
    df['Commercial_Name'] = df['Commercial_Name'].str.strip()
    df['CR_Legal_Structure_AR'] = df['CR_Legal_Structure_AR'].str.strip()
    df['CR_Region_Name_AR'] = df['CR_Region_Name_AR'].str.strip()
    df['CR_City_Name_AR'] = df['CR_City_Name_AR'].str.strip()
    df['CR_Issue_Date_GR'] = df['CR_Issue_Date_GR'].str.strip()
   
    df = df.fillna({'CR_Legal_Structure_AR': "Unknown"})
  
    df = df.dropna(subset=['NationalNo'])
    
    df = df.drop_duplicates()
    return df


df = pd.read_csv(r'Commercial_registration_2023_Q1.csv')

df_clean = clean_data(df.copy())
df_clean.head()


df.to_csv('cleaned_data.csv', index=False)
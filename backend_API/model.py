import pandas as pd
import numpy as np

def operation1(data):
    #filter out all the data for metabolite ids ending with:
    #‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets (1 for each compound id)

    dataPC = data[pd.Series(list(bool((type(data["Accepted Compound ID"][x]) == str) and data["Accepted Compound ID"][x].endswith('PC') and not data["Accepted Compound ID"][x].endswith('LPC') ) for x in range(data.shape[0])))]
    dataLPC = data[pd.Series(list(bool((type(data["Accepted Compound ID"][x]) == str) and data["Accepted Compound ID"][x].endswith('LPC') ) for x in range(data.shape[0])))]
    dataplasmalogen = data[pd.Series(list(bool((type(data["Accepted Compound ID"][x]) == str) and data["Accepted Compound ID"][x].endswith('plasmalogen') ) for x in range(data.shape[0])))]
    
    dataPC.to_excel("D:/Projects/Elucidata Assignment/Results/result1.xlsx")
    dataLPC.to_excel("D:/Projects/Elucidata Assignment/Results/result2.xlsx")
    dataplasmalogen.to_excel("D:/Projects/Elucidata Assignment/Results/result3.xlsx")
    return 1 #testing

    #operation 1 done

def func(row):
    return round(row['Retention time (min)'])
def operation2(data):
    data["Retention Time Roundoff (in mins)"] = data.apply(func,axis=1)
    data.to_excel("D:/Projects/Elucidata Assignment/Results/result4.xlsx")
    return 2 #testing

    #operation2 done

def operation3(data):
    data["Retention Time Roundoff (in mins)"] = data.apply(func,axis=1)
    col_list = list(data.columns)
    col_list = [e for e in col_list if e not in {'Accepted Compound ID','Retention time (min)','m/z'}]
    new_data = data[col_list]
    temp = col_list
    temp.remove('Retention Time Roundoff (in mins)')
    new_data = new_data.groupby('Retention Time Roundoff (in mins)')[temp].mean()
    
    new_data.to_excel("D:/Projects/Elucidata Assignment/Results/result5.xlsx")
    return 3 #testing

    #operation3 done
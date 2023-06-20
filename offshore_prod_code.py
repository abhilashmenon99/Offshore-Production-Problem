'''Packages to import'''
from pulp import*
import numpy as np
import pandas as pd
'''∑_iϵI▒〖x_ij<y_ij K_j 〗'''

''' reading Data'''
data_file =r"C:\Users\olw08\OneDrive - ORMAE\Desktop\AMM\excel_files_dat\data_task_prod_prob.xlsx"
'''reading files'''
fact_var_df=pd.read_excel(data_file,sheet_name="factory_variables")

demand_df=pd.read_excel(data_file,sheet_name="demand")
#fact_var_df.head(), demand_df.head()

''' Defining Capacity Variables'''
'''Minimum capacity'''
min_cap=[]
max_cap=[]
min_cap.append(np.array(fact_var_df["MIN_CAPACITY"][fact_var_df["FACTORY"]=='A']))
min_cap.append(np.array(fact_var_df["MIN_CAPACITY"][fact_var_df["FACTORY"]=='B']))
'''Maximum capacity'''
max_cap.append(np.array(fact_var_df["MAX_CAPACITY"][fact_var_df["FACTORY"]=='A']))
max_cap.append(np.array(fact_var_df["MAX_CAPACITY"][fact_var_df["FACTORY"]=='B']))

demand=np.array(demand_df["DEMAND"])

''' Defining the costs'''
var_cost=[]
fixed_cost=[]
'''Variable costs'''
var_cost.append(np.array(fact_var_df["VARIABLE_COSTS"][fact_var_df["FACTORY"]=='A']))
var_cost.append(np.array(fact_var_df["VARIABLE_COSTS"][fact_var_df["FACTORY"]=='B']))

'''Fixed costs'''
fixed_cost.append(np.array(fact_var_df["FIXED_COSTS"][fact_var_df["FACTORY"]=='A']))
fixed_cost.append(np.array(fact_var_df["FIXED_COSTS"][fact_var_df["FACTORY"]=='B']))

num_month=len(demand)
'''calling solver'''
lp=LpProblem("production",LpMinimize)

'''Defining Variables'''
month=[]
fact=[]
for i in range(0,2):
    month+=[j for j in range(0,num_month)]
    fact+=[i for j in range(0,num_month)]
var_keys=list(zip(fact,month))

x=LpVariable.dicts("quantity",var_keys,lowBound=0)
y=LpVariable.dicts("open or closed",var_keys,lowBound=0,upBound=1,cat="Integer")


#objective function
objective_terms=[]
for j in range(0,len(var_keys)):
        objective_terms.append(var_cost[var_keys[j][0]][var_keys[j][1]]*x[var_keys[j][0],var_keys[j][1]]+\
                               fixed_cost[var_keys[j][0]][var_keys[j][1]]*y[var_keys[j][0],var_keys[j][1]])
lp+=(lpSum(objective_terms))


'''constraints
demand constraint for each month'''
for j in range(0,num_month):
    lp+=(lpSum([x[i,j] for i in [0,1]])==demand[j])
    
'''capacity constraints'''
for j in range(0,num_month):
    for i in [0,1]:
        lp+=(x[i,j]<=(max_cap[i][j]*y[i,j]))
        lp+=(x[i,j]>=(min_cap[i][j]*y[i,j]))

status=lp.solve()
print("status",status)#optimal-->1, not solved-->2, infeasible-->3, unbounded-->4,undefined-->5

'''reading the optimal values'''
for var in lp.variables():
    print(var,"=",value(var))
print("OPT=",value(lp.objective))

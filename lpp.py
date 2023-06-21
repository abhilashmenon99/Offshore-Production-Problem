from pulp import *
import numpy as np
import pandas as pd


def solve_production_problem(data_file):
    """
    Solve the production problem using Linear Programming.

    Args:
        data_file (str): Location of the data file.

    Returns:
        int: Status of the optimization problem.
    """
    # Reading Data
    fact_var_df = pd.read_excel(data_file, sheet_name="factory_variables")
    demand_df = pd.read_excel(data_file, sheet_name="demand")

    # Define Capacity Variables
    min_cap = []
    max_cap = []

    # Extract minimum and maximum capacity for each factory
    min_cap.append(np.array(fact_var_df["MIN_CAPACITY"][fact_var_df["FACTORY"] == 'A']))
    min_cap.append(np.array(fact_var_df["MIN_CAPACITY"][fact_var_df["FACTORY"] == 'B']))
    max_cap.append(np.array(fact_var_df["MAX_CAPACITY"][fact_var_df["FACTORY"] == 'A']))
    max_cap.append(np.array(fact_var_df["MAX_CAPACITY"][fact_var_df["FACTORY"] == 'B']))

    # Demand
    demand = np.array(demand_df["DEMAND"])

    # Define Costs
    var_cost = []
    fixed_cost = []

    # Extract variable and fixed costs for each factory
    var_cost.append(np.array(fact_var_df["VARIABLE_COSTS"][fact_var_df["FACTORY"] == 'A']))
    var_cost.append(np.array(fact_var_df["VARIABLE_COSTS"][fact_var_df["FACTORY"] == 'B']))
    fixed_cost.append(np.array(fact_var_df["FIXED_COSTS"][fact_var_df["FACTORY"] == 'A']))
    fixed_cost.append(np.array(fact_var_df["FIXED_COSTS"][fact_var_df["FACTORY"] == 'B']))

    num_month = len(demand)
    lp = LpProblem("production", LpMinimize)

    # Define Variables
    month = []
    fact = []

    # Create month and factory variables for indexing
    for i in range(0, 2):
        month += [j for j in range(0, num_month)]
        fact += [i for j in range(0, num_month)]
    var_keys = list(zip(fact, month))
    x = LpVariable.dicts("quantity", var_keys, lowBound=0)
    y = LpVariable.dicts("open_or_closed", var_keys, lowBound=0, upBound=1, cat="Integer")

    # Objective Function
    objective_terms = []

    # Calculate objective function terms based on variable and fixed costs
    for j in range(0, len(var_keys)):
        objective_terms.append(
            var_cost[var_keys[j][0]][var_keys[j][1]] * x[var_keys[j][0], var_keys[j][1]] +
            fixed_cost[var_keys[j][0]][var_keys[j][1]] * y[var_keys[j][0], var_keys[j][1]]
        )
    lp += lpSum(objective_terms)

    # Constraints
    for j in range(0, num_month):
        # Demand constraint for each month
        lp += lpSum([x[i, j] for i in [0, 1]]) == demand[j]

    for j in range(0, num_month):
        for i in [0, 1]:
            # Capacity constraints
            lp += x[i, j] <= max_cap[i][j] * y[i, j]
            lp += x[i, j] >= min_cap[i][j] * y[i, j]

    # Solve the LP problem
    status = lp.solve()
    return status


if __name__ == '__main__':
    data_file = r"C:\Users\olw08\OneDrive - ORMAE\Desktop\AMM\excel_files_dat\data_task_prod_prob.xlsx"
    status = solve_production_problem(data_file)
    print("Status:", status)

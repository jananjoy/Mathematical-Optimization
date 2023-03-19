"""
Python code for linear programming optimization problem
Problem Equation:
Maximize  10x1+6x2+4x3
s.t  x1+x2+x3<=100
     10x1+4x2+5x3<=600
     10x1+4x2+5x3<=600
     10x1+4x2+5x3<=600
      x1≥0,x2≥0,x3≥0
"""
# File : math_optimization.py
# Description: Python code for linear programming optimization problem
# Others: Use the optlang (modeling language for solving mathematical optimization problem)
from __future__ import print_function
from optlang import Model, Variable, Constraint, Objective

# Declaration of the variables with optionally a lower and/or upper bound.
x1 = Variable('x1', lb=0)
x2 = Variable('x2', lb=0)
x3 = Variable('x3', lb=0)

# Declaration of constraint  with optionally a lower bound (lb) and/or upper bound(ub).
constraint_1 = x1 + x2 + x3
constraint_2 = 10 * x1 + 4 * x2 + 5 * x3
constraint_3 = 2 * x1 + 2 * x2 + 6 * x3

# An expression of the objective function to be maximized
expression = 10 * x1 + 6 * x2 + 4 * x3

# Setting Variables, constraints and equation expression in a Model object for running optimization model
model = Model(name ='Maximization model')
model.objective = Objective(expression, direction='max')
model.add([Constraint(constraint_1, ub=100),
           Constraint(constraint_2, ub=600),
           Constraint(constraint_3, ub=300)])
status = model.optimize()
print("====================================================")
print("Status after optimization:", model.status)
print("Calculated objective value:", model.objective.value)
print("====================================================")
for name_variable, value in model.variables.iteritems():
    print(name_variable, ":=", value.primal)

from ctypes import py_object
import pyomo.environ as pyo 
from pyomo.environ import *
from sympy import solve 

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(None,3))
model.y = pyo.Var(bounds=(0,None))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr=x+y<=8)
model.C2 = pyo.Constraint(expr=8*x+3*y>=-24)
model.C3 = pyo.Constraint(expr=-6*x+8*y<=48)
model.C4 = pyo.Constraint(expr=3*x+5*y<=15)

model.obj = pyo.Objective(expr=-4*x-2*y, sense=minimize)

opt = SolverFactory('glpk')
opt.solve(model)

print('x=', pyo.value(x))
print('y=', pyo.value(y))
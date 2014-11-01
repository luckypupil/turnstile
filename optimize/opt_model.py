#!/usr/bin/env python
from coopr.pyomo import *


def make_model(arg=6):
    model = ConcreteModel()
    model.x_1 = Var(within=NonNegativeReals)
    model.x_2 = Var(within=NonNegativeReals)
    model.k   = Param(initialize=arg)
    model.obj = Objective(expr=arg*model.x_1 + arg*model.x_2)
    model.con1 = Constraint(expr=model.k*model.x_1 + 4*model.x_2 >= 1)
    model.con2 = Constraint(expr=2*model.x_1 + 5*model.x_2 >= 2)

    return model


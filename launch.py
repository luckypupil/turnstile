#!/usr/bin/env python

from coopr.opt import SolverFactory
from optimize.opt_model import make_model
from optimize.luckypupil import wk_demand


def model_solver(solver="glpk"):
    data = wk_demand()
    model = make_model(arg=data)
    instance = model.create()
    #instance.pprint()
    opt = SolverFactory(solver)
    results = opt.solve(instance)
    print results
    instance.load(results)
    #print('*********break***********')
    #print (instance.x_2.value)


if __name__ == '__main__':
    print wk_demand()
    model_solver()

#!/usr/bin/env python

from coopr.opt import SolverFactory
from optimize.test import make_model


def model_solver(solver="glpk"):
    model = make_model()
    instance = model.create()
    #instance.pprint()
    opt = SolverFactory(solver)
    results = opt.solve(instance)
    print results.items()
    instance.load(results)
    print('*********break***********')
    print (instance.x_2.value)


if __name__ == '__main__':
    model_solver()    

# Runge-Kutta-4
## RK-4 for single ODE

This repository contains the code for analyzing the results of RK-4 method for a single ODE. You can also provide the analytical function to compare the estimate versus the actual value. You will need to define your function separately in the provided file.

## RK-4 for a System of ODE's

A basic skeleton for a system of ODE's solution is provided. Currently, it handles only two equation system, You will need to define your own functions for each ODE and pass it to the `rk4_system` function. Note that you will also need to provide all the initial conditions. Don't forget to also add the `k13`, `k14`, `k23`, `k24` and so variables if you plan to solve a system of 4 ODE's.

I will work on it at a later time to make it generic so you don't have to do all the work.


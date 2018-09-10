#This is the “Himmelblau function” where x lies between ±6 and y lies between ±6.
import numpy as np
import random
import math

# Objective function: Accepts solution x and calculates the objective function value for x
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = (x1**2+x2-11)**2 + (x1+(x2**2)-7)**2
    return obj

''' Randomly selected innitial solution vector  x_init '''
x_init = [1, 1]

# Number of tempratures
m = 1000

# Number of moves at certain tempratures
n = 10

# Seed for the random number generator
random.seed(121)

# Number of accepted solutions; could be used as a stopping criteria
n_acept_sol = 0.0

# Probability of acceptance of worst solution at the beggining of the search
Po = 0.7

# Probability of acceptance of worst solution at the end of the search
Pf = 0.001

# Starting temperature
To = -1.0/math.log(Po)
# Final temperature
Tf = -1.0/math.log(Pf)

# α - Cooling parameter
α = (Tf/To)**(1.0/(m-1.0))

# Createing and innitializing solution vector with size equal to number of tempratures
x = np.zeros((m+1,2))  
x[0] = x_init                        # Set the first row of the solution vector to innitial solution
xi = np.zeros(2)                     # Create a vector for iterarion through the solution vector
xi = x_init                          # Set the iteration vector to the innitial solution
n_acept_sol = n_acept_sol + 1.0      # Increament the no. aceepted solution by one, for the innitial solution

# Create and innitialize current solution vector and current objective function value
Xtmp = np.zeros(2)            # Holds the current best solution
Xtmp = x[0]                   # The current best solution starts from the starting solution
Ftmp = f(xi)                # The current objective function value
Ff = np.zeros(m+1)          # Create m size array to save the current best final solution 
Ff[0] = Ftmp                # Store the current solution value 

# Current temperature value
Tt = To     # set the current temprature value to the starting temprature
# Delta: The change in objective function value
delta_avg = 0.0  
for i in range(m):
    print('Stage: ' + str(i) + ' Temperature: ' + str(Tt))
    for j in range(n):
        # Generate new solutions by moving from the current solution
        xi[0] = Xtmp[0] + random.random() - 0.5
        xi[1] = Xtmp[1] + random.random() - 0.5
        # Clip to upper and lower bounds
        xi[0] = max(min(xi[0],6.0),-6.0)
        xi[1] = max(min(xi[1],6.0),-6.0)
        delta = abs(f(xi)-Ftmp)
        if (f(xi)>Ftmp):       # Worst solution found
            # Set delta_avg to the starting change in energy (objective functio)
            if (i==0 and j==0): 
                delta_avg = delta
            # Compute probability of acceptance of the worst solution found
            Pa = math.exp(-delta/(delta_avg * Tt))
            
            # Compare the Pa with random value to decide whether to accept the worst solution or not
            if (random.random()<Pa):
                # accept the worst solution, it is better than the random value
                accept = True
            else:
                # Do not accept the worst solution
                accept = False
        else:
            # Optimal objective function value found, accept it
            accept = True
        if (accept==True):
            # update the current solution with the newly accepted solution
            Xtmp[0] = xi[0]
            Xtmp[1] = xi[1]
            Ftmp = f(Xtmp)
            # increament number of accepted solutions
            n_acept_sol = n_acept_sol + 1.0
            # Recalculate and update delta_avg
            delta_avg = (delta_avg * (n_acept_sol-1.0) +  delta) / n_acept_sol
    # Save the best solution for the current temprature stage
    x[i+1][0] = Xtmp[0]
    x[i+1][1] = Xtmp[1]
    Ff[i+1] = Ftmp
    # Cool the temperature for the next stage
    Tt = α * Tt

# Display solution
print('Final solution values: ' + str(Xtmp))
print('Final Objective function value: ' + str(Ftmp))
#print('Starting Temprature ' + str(To))
#print('Final Temprature ' + str(Tf))
#print('starting objective value for (x1 =3 & x2 = 2):=  ' + str(Ff[0]))

# Implementation of Simulated Annealing Algorith to solve the Quadratic Assignment Problem (QAP).
This is the “Himmelblau function” where x lies between +/-6 and y lies between +/ - 6. The objective 
is to minimize z.  One of the global minima lies at (3.0000, 2.0000) where z = 0.0000. 
z =  (x^2  +  y - 11)^2  +  (x +  y^2  - 7)^2

For convenience of the implementation the decision variables X and Y are changed to X1 and X2 respectively. 
The solution vector X is defined as a vector containing X1 and X2.
X = [X1, X2], and we are given that the range of the decision variables is +/-6. The number of temperature 
stages is found to be 1000 for the best result I got. And for each temperature stage m, the number of iteration 
n is set to 10.

After defining the starting solution X_init, probability of acceptance of the worst solution at the beginning 
and at the end of the search as shown on the tables below, I conducted a number of trials and observed the 
corresponding changes on the solution.

Thereafter once the iteration starts the neighbors of the next move are selected by adding random value to the 
current solution and subtracting 0.5. Then, the resulting values for the neighborhood are clipped to make sure 
that they do not exceed the boundary range of the decision variables -/+6. Next, the newly found neighbors are 
substituted in to the objective function, and the change in the objective function value is calculated and recorded
as delta. If the solution found is worse than the current best solution, its probability of acceptance is compared
with a random value to decide whether to accept it or reject it. Otherwise, the newly found solution will be stored 
as the best solution for the current iteration.

Delta average is used to store the cumulative change in the objective function to observe by how much is the best 
solution improved from the starting solution. This value could be used as stopping criteria; stop searching after 
the best solution is improved by the required amount.

The number of accepted solution is also recorded along the way through the iteration. This provides information 
regarding how many better solutions have been found for certain number of iterations or parameter settings. 
And it also could be used as a stopping criterion if we want to stop the search after we satisfied by the improvement we get.




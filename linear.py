from scipy.optimize import linprog

def problem1():
    ''' maximize        z = x + 2y
        subject to:     x + y <= 10
                        x + 4y >= 20
                        x >= 0
                        y >= 0

        convert into the appropriate standard form
        minimize        -z = -x - 2y   (multiply by -1)
        subject to:     x + y <= 10
                        -x - 4y <= -20
                        x >= 0
                        y >= 0
    '''
    obj_func = [-1, -2]       # objective function

    ineq_left = [[ 1,  1],    # constraints
                [-1,  -4]] 
    ineq_right = [10, -20]  

    bnd = [(0, float("inf")),  # Bounds of x
           (0, float("inf"))]  # Bounds of y

    # run optimization
    opt = linprog(c=obj_func, A_ub=ineq_left, b_ub=ineq_right, bounds=bnd,
                  method="revised simplex")
    print (opt)

if __name__ == '__main__':
    problem1()
    
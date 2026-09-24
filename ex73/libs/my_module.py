from math import  sqrt
def calculate(a,b,c):
    if a==0:
        if b==0 and c==0:
            return "Infinite solutions"
        elif b==0 and c!=0:
            return "No solutions"
        else:
            x=-c/b
            return f"Solution x={x}"
    else:
        delta=b**2-4*a*c
        if delta<0:
            return "No solutions"
        elif delta==0:
            x=-b/(2*a)
            return f"Double solutions x1=x2={x}"
        else:
            x1=round(((-b-sqrt(delta))/(2*a)),2)
            x2=round(((-b+sqrt(delta))/(2*a)),2)
            return f"x1={x1} and x2={x2}"
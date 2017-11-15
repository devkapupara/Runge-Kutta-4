import parser, math

def parseEquation(exp):
    return parser.expr(exp).compile()

def f(exp, x,y):
    return eval(exp)

def RungeKutta(n, exp, x, y, h):
    if n == 0:
        return []
    else:
        k1 = h * f(exp,x,y)
        k2 = h * f(exp,x+h/2,y+k1/2)
        k3 = h * f(exp,x+h/2,y+k2/2)
        k4 = h * f(exp,x+h,y+k3)
        ans = y + (1/6*(k1 + 2*k2 + 2*k3 + k4))
        return [ans] + RungeKutta(n-1,exp,x+h,ans,h)


if __name__ == "__main__":
    exp = parseEquation(input("Enter f(x) = "))
    y = float(input("Enter y0: "))
    x = float(input("Enter x0: "))
    h = float(input("Enter step size: "))
    n = int(input("How many values of y to calculate? "))
    ans = RungeKutta(n,exp,x,y,h)
    track = h
    for i in ans:
        print("y{:.2f} = {:.5f}".format(track, i))
        track += h
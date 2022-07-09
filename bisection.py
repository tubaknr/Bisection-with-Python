def f(x):
    return x**3-5*x-9

def ask():
    a = float(input("a:"))
    b = float(input("b:"))
    e = float(input("e:"))
    # print(f"First point a: {a}")
    # print(f"Second point b: {b}")
    # print(f"epsilon value :{e}")
    # print(f"f(a)={f(a)}")
    # print(f"f(b)={f(b)}")
    if f(a)*f(b)>0.0:
        print("ncorrect interval.")
    else:
        bisection(a,b,e)

def bisection(a, b, e):
    """
    :param a: starting interval's left point
    :param b: starting interval's right point [a,b]
    :return: solution of the function
    """
    iteration=0
    if b<a:
        b,a=a,b

    while True:
        iteration+=1
        if f(a)==0:
            print(f"Exact solution: f(a) = {f(a)}!!")
            print(f"Iteration :{iteration} ")
            break
        elif f(b)==0:
            print(f"Exact solution: f(b) = {f(b)}!!")
            print(f"Iteration :{iteration} ")
            break
        else:
            mid = (a+b)/2
            if f(mid)==0:
                print(f"Exact solution: f(mid) = {f(mid)}!! ")
                print(f"Iteration :{iteration} ")
                break

            elif abs(f(mid)) <= e:
                print(f"We arrived epsilon valuee mid={mid}!!")
                print(f"Iteration :{iteration} ")
                break
            elif f(a)*f(mid)<0:
                b=mid
                continue
            elif f(a)*f(mid)>0:
                a=mid
                continue

ask()













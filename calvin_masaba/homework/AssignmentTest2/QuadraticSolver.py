#QUESTION 10


def solveQuadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # If discriminant is positive, there are two real roots
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return (root1, root2)
    # If discriminant is zero, there is one real root (repeated)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    # If discriminant is negative, there are no real roots
    else:
        return None

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = solveQuadratic(a, b, c)

if roots is None:
    print("The quadratic equation has no real roots.")
else:
    print("The roots of the quadratic equation are:", roots)

    #By CALVIN MASABA

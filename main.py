import math
def count (x1,x2,y1,y2):
    a=(pow(x1+x2,2)+pow(y1+y2,2))
    b=math.sqrt(a)
    return(f"Długość odcinka to √{a} czyli {b}")
print("Obliczanie długości odcinka \nwartości podaj bez nawasiu zamiast przecinka użyj spacji")
x,y=input("punkt a\n").split()
a,b=input("punkt b\n").split()
print(count(int(x),int(a),int(y),int(b)))

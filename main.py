def polar_calculator():
    import math
    YA = float(input('enter Y component of coordinate in metres:'))
    XA = float(input('enter X component of coordinate in metres:'))
    D = float(input('enter distance in metres:'))
    B = float(input('enter direction in degrees:'))
    r = (B/180)*math.pi
    YB = YA + D*math.sin(r)
    XB = XA + D*math.cos(r)
    print(f'Y component of calculated coordinate: {YB} m')
    print(f'X component of calculated coordinate: {XB} m')

polar_calculator()




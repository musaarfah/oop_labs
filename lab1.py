#Task 1
def main():
    tx=2
    ty=1
    tz=5
    mx=3
    my=-2
    mz=4
    bx=4
    by=-1
    bz=-2
    print(f't: ({tx},{ty},{tz})')
    print(f'm: ({mx},{my},{mz})')
    print(f'b: ({bx},{by},{bz})')
    print(f't+b: ({tx+bx},{ty+by},{tz+bz})')
def stp_calculate(tx,ty,tz,mx,my,mz,bx,by,bz):
    s=tx*(my*bz-by*mz)-ty*(mx*bz-bx*mz)+tz*(mx*by-bx*my)
    print(f'stp:{s}')
    print()

#Task 2

def unit_vector(a,b,c):
    x=(a**2+b**2+c**2)**0.5
    print(f'{a/x+b/x+c/x}')

# Task 3
def scalar_multiple(a,b,c):
    num=int(input('Scalar Multiple :'))
    print(f'{a*num},{b*num},{c*num}')

# Task 4
def cross_product(ax,ay,az,bx,by,bz):
    x=(ay*bz-az*by)
    y=(ax*by-ay*bx)
    z=(ax*by-ay*bx)
    print(x,y,z)

# Task 5
def equality_vector(ax,ay,az,bx,by,bz):
    if ax==bx and ay==by and az==bz:
        print('Vectors are equal')
    else:
        print('Vectors are not equal')
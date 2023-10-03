class Mat2by2:
    def __init__(self,a11,a12,a21,a22):
        self.a11=a11
        self.a12=a12
        self.a21=a21
        self.a22=a22



    def add_matrices(m1,m2):
        a=Mat2by2(0,0,0,0)
        a.a11=m1.a11+m2.a11
        a.a12=m1.a12+m2.a12
        a.a21=m1.a21+m2.a21
        a.a22=m1.a22+m2.a22
        return a

    def subtract_matrices(m1,m2):
        s = Mat2by2(0,0,0,0)
        s.a11 = m1.a11 - m2.a11
        s.a12 = m1.a12 - m2.a12
        s.a21 = m1.a21 - m2.a21
        s.a22 = m1.a22 - m2.a22
        return s

    def scalar_multiple(m1,n):
        b=Mat2by2(0,0,0,0)
        b.a11=m1.a11*n
        b.a12=m1.a12*n
        b.a21=m1.a21*n
        b.a22=m1.a22*n
        return b

    def transpose(m1):
        c=Mat2by2(0,0,0,0)
        c.a11=m1.a11
        c.a12=m1.a21
        c.a21=m1.a12
        c.a22=m1.a22
        return c

    def determinant(m1):
        d=Mat2by2(0,0,0,0)
        x=m1.a11*m1.a22-m1.a12*m1.a21
        print ('Determinant : ',x)

    def matrix_multiplaction(m1,m2):
        e=Mat2by2(0,0,0,0)
        e.a11=m1.a11*m2.a11+m1.a12*m2.a21
        e.a12=m1.a11*m2.a12+m1.a12*m2.a22
        e.a21=m1.a21*m2.a11+m1.a22*m2.a21
        e.a22=m1.a21*m2.a12+m1.a22*m2.a22
        return e

    def singular(m1):
        f=Mat2by2(0,0,0,0)
        x=m1.a11*m1.a22-m1.a12*m1.a21
        if x==0:
            print('Matrix is Singular')
        else:
            print('Matrix is not singular')

    def null_matrix(m1):
        g=Mat2by2(0,0,0,0)
        if m1.a11==0 and m1.a22==0:
            print('Matrix is Null')
        else:
            print('Matrix is not a Null Matrix')

    def identity_matrix(m1):
        g=Mat2by2(0,0,0,0)
        if m1.a11==1 and m1.a22==1 and m1.a12==0 and m1.a21==0:
            print('Matrix is Identity')
        else:
            print('Matrix is not an Identity')

    def matrix_inverse(m1):
        h=Mat2by2(0,0,0,0)
        x = m1.a11 * m1.a22 - m1.a12 * m1.a21
        if x != 0:
            h.a11=1/x*m1.a22
            h.a22=1/x*m1.a11
            h.a12=1/x*-(m1.a12)
            h.a21=1/x*-(m1.a21)
            return h
        else:
            print('Matrix is Non-Singular,inverse not possible')

    def division_of_matrix(m1,m2):
        h=Mat2by2(0,0,0,0)
        x = m1.a11 * m1.a22 - m1.a12 * m1.a21
        if x != 0:
            h.a11 = 1 / x * m1.a22
            h.a22 = 1 / x * m1.a11
            h.a12 = 1 / x * -(m1.a12)
            h.a21 = 1 / x * -(m1.a21)
            h.a11 = h.a11 * m2.a11 + h.a12 * m2.a21
            h.a12 = h.a11 * m2.a12 + h.a12 * m2.a22
            h.a21 = h.a21 * m2.a11 + h.a22 * m2.a21
            h.a22 = h.a21 * m2.a12 + h.a22 * m2.a22
            return h

        else:
            print('Matrix is Non-Singular,Division not possible')



def main():
    m1=Mat2by2(1,2,3,4)
    m2=Mat2by2(2,7,1,4)

    a=m1.add_matrices(m2)
    print(f'm1+m2: \n {a.a11} {a.a12} \n {a.a21} {a.a22}')

    b = m1.subtract_matrices(m2)
    print(f'm1-m2: \n {b.a11} {b.a12} \n {b.a21} {b.a22}')

    c=m1.scalar_multiple(3)
    print(f'Scalar Multiple: \n {c.a11} {c.a12} \n {c.a21} {c.a22}')

    d = m1.transpose()
    print(f'Transpose: \n {d.a11} {d.a12} \n {d.a21} {d.a22}')

    e = m1.determinant()

    f = m1.matrix_multiplaction(m2)
    print(f'm1*m2: \n {f.a11} {f.a12} \n {f.a21} {f.a22}')

    g = m1.singular()

    h=m1.null_matrix()

    i=m1.identity_matrix()

    j= m1.matrix_inverse()
    print(f'm1 inverse: \n {j.a11} {j.a12} \n {j.a21} {j.a22}')

    k=m1.division_of_matrix(m2)
    print(f'm1 / m2: \n {k.a11} {k.a12} \n {k.a21} {k.a22}')





main()
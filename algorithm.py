n = 5
a = 0
b = 3


def add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p[0] != q[0]:
        s = (p[1] - q[1]) * pow(p[0] - q[0], -1, n)
    else:
        if (p[1] + q[1]) % n != 0:
            s = (3 * p[0] * p[0] + a) * pow(2 * p[1], -1, n)
        else:
            return None
    r0 = s * s - p[0] - q[0]
    r1 = s * (p[0] - r0) - p[1]
    return r0 % n, r1 % n


p = 2, 1
q = 3, 0
print(add(p, q))

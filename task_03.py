a = 3
b = 6
c = 5

def is_triplet(one, two, thre):
    result = one + two > thre
    return result

def is_triangles(a,b,c):
    print(is_triplet(a,b,c))
    print(is_triplet(a,c,b))
    print(is_triplet(c,b,a))

is_triangles(a,b,c)


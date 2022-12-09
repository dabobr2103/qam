a = 3
b = 6
c = 5
d = 1
e = 2


def is_triplet(one, two, thre):
    result = one + two > thre
    return result

def is_triangles(a,b,c):
    nabir_1 = is_triplet(a,b,c)
    nabir_2 = is_triplet(a,c,b)
    nabir_3 = is_triplet(c,b,a)
    if nabir_1 and nabir_2 and nabir_3:
        return "is triangle"
    return "is not"

print(is_triangles(a,b,c))
print(is_triangles(a,d,e))

a = 3
b = 6
c = 5
d = 1
e = 2


def is_triplet(one, two, thre):
    result = one + two > thre
    return result

def is_triangles(a,b,c):
    value_list = [a, b, c]
    value_list.sort()
    if is_triplet(value_list[0],value_list[1],value_list[2]):
        return "is triangle"
    return "is not"

print(is_triangles(a,b,c))
print(is_triangles(a,d,e))
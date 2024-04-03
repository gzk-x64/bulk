# To replace
product_key_input = "T48TD4VFCWVV7HYB2PXYMY47H"

characters = "BCDFGHJKMPQRTVWXY2346789"

encoded_id = [characters.index(c) for c in product_key_input]

product_key = ""
for i in range(25):
    c = 0
    for j in range(14, -1, -1):
        c = (c << 8) ^ encoded_id[j]
        encoded_id[j] = c // 24
        c %= 24
    product_key = characters[c] + product_key

for i in range(4, 0, -1):
    insertion_point = i * 5
    product_key = product_key[:insertion_point] + "-" + product_key[insertion_point:]

print(product_key)
def capital_indexes(a):
    return([i for i, x in enumerate(u) if x.isupper()])
print(capital_indexes("HeLlO"))
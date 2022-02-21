def param_count(*args):
    for i in args:
        return len(args)
print(param_count(1,2,3))
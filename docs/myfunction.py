def myfunction(a, b , double=True):
    import pudb
    pudb.set_trace()
    c=a+b
    if double:
       c=c*2
       return c

print myfunction(1,2, double=True)
print myfunction(1,2)
print myfunction(1,2, False)



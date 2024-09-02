# and, or, not

resultado_final = True and True

resultado_final2 = True and True and False

resultado_final3 = True and True and 10 > 20


""" print(resultado_final)
print(resultado_final2)
print(resultado_final3) """


resultado_or = True and True

resultado_or2 = False and False and 100 > 20


""" print(resultado_or)
print(resultado_or2) """

# True and False
resultado_comb = True and (False or 5 > 10)

# True and True
resultado_comb2 = True and (False or 50 > 10)


""" print(resultado_comb)
print(resultado_comb2) """


resultado_not = not True
resultado_not2 = not False

print(resultado_not)
print(resultado_not2)

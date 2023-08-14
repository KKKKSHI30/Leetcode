# Consider a string, expression consisting of the characters  <  and  >  only.
# We consider the string to be balanced  if each <  always appears before
# (i.e., to the left of) a corresponding  >  character (they do not need to be adjacent).
# Moreover, each  <  and >  act as a unique pair of symbols and neither symbol can be considered
# as part of any other pair of symbols. For example, the strings  <<>>,  <>, and  <><> are all balanced,
# but the strings  >>,  <<>, and  ><><  are unbalanced.

def balancedOrNot(expressions, maxReplacements):
    results = []
    for i in range(len(expressions)):
        expression, replacements = expressions[i], maxReplacements[i]
        count = 0
        unbalanced = False
        for char in expression:
            if char == "<":
                count += 1
            elif char == ">":
                if count == 0:
                    if replacements <= 0:
                        unbalanced = True
                        break
                    replacements -= 1
                else:
                    count -= 1
        if count == 0 and not unbalanced:
            results.append(1)
        else:
            results.append(0)
    return results
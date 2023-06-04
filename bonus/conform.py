"""
Input is a vector of F's and B's, in terms of forwards and backwards caps
Output is a set of commands (printed out) to get either all F's or all B's
Fewest commands are the goal!

Please see the problem write-up to get more details
"""

# caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
# caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "B", "F"]
caps = ['F','F','B','H','B','F','B','B','B','F','H','F','F'] 


def pleaseConform(caps):
    F_lst = []
    B_lst = []
    H_lst = []
    start = 0
    # split list to consecutive same values
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            if caps[start] == "F":
                F_lst.append((start, i-1))
                start = i
            elif caps[start] == "B":
                B_lst.append((start, i-1))
                start = i
            else:
                H_lst.append((start, i-1))
                start = i

    # add the last value
    if caps[-1] == "F":
        F_lst.append(["F", start, len(caps)-1])
    else:
        B_lst.append(["B", start, len(caps)-1])

    if len(F_lst) < len(B_lst):
        for r in F_lst:
            if r[0] != r[1]:
                print(f"Person in position {r[0]} through {r[1]} flip your cap!")   
            else:
                print(f"Person in position {r[0]} flip your cap!")
    else:
        for r in B_lst:
            if r[0] != r[1]:
                print(f"Person in position {r[0]} through {r[1]} flip your cap!")
            else:
                print(f"Person in position {r[0]} flip your cap!")


pleaseConform(caps)
##pleaseConform(cap2)

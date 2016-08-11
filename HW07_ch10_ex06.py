# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(listtocheck):
    flag=True
    for i in range(len(listtocheck)):
        if i == 0:
            continue
        elif listtocheck[i-1] < listtocheck[i]:
            flag=True
        else:
            flag=False
            break
    return flag

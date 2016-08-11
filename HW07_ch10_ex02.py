# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(listtocapitalize):
    newlist=[]
    for elements in listtocapitalize:
        if type(elements) is list:
            newlist.append(capitalize_nested(elements))
        else:
            try:
                newlist.append(elements.capitalize())
            except:
                print('Only values starting with alphabets are allowed. Other values have been omitted.')
    return newlist

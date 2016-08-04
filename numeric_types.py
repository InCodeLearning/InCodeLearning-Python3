# Boolean


# class must be defined before use
class UserDefined1:
    def __bool__(self):
        return False


# class name should use camel cases like Java...
class UserDefined2:
    # class user_defined1:
    def __len__(self):
        return 0

# Any object can be tested for truth, following are considered false.
if (not (None or False or
         0 or 0j or 0.0 or # pep8 aligning to opening parenthesis
         '' or () or [] or
         {} or
         UserDefined1() or UserDefined2())):
    print("hello all the False's, everything else is True.")

# legacy from python 2 True=1 False=0
logic_ops = {
    "True + True =": True + True,
    "True - False =": True - False,
    "True * 3 =": True * 3,
    # True/False division by zero Error 
}

for k,v in logic_ops.items():
    print('  ', '{:<12}{:>4}'.format(k, v))


# *args and **kwargs


def intro(name, age, city, language):
    print('I am {}. I am {} years old. I live in {}. I love {}'.format(
        name, age, city, language
    ))


lst = ['dokelung', 27, 'Taipei', 'Python']
dic = {'name': 'dokelung', 'age': 27, 'city': 'Taipei', 'language': 'Python'}

intro(*lst)
intro(*dic)
intro(**dic)

# unpacking list
t = ('start', 1, 2, 3, 4, 5, 'end')
s, *nums, e = t
print(s, nums, e)


def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: {0}: {1}".format(key, kwargs[key]))


test_var_kwargs(farg=1, myarg2="two", myarg3=3)

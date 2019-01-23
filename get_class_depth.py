

# The class as per you mentioned on the question
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    }
}

# Main Solution Start From here
i = 1
j = 0


# Method to check internal element/property.
def props(x):
    return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


# Init list data object
listData = {}


def print_depth(data=a):

    if not data:
        data = a

    global i  # call global variable
    global j  # call global variable
    global listData  # global object variable
    for x, v in data.items():  # loop to get specific item element data
        if x == 'user':  # if match string
            j = 1  # set flag/define for next data - profile(first_name, last_name, father)

        if j == 0:
            # print(x, i)        # Print depth for keys - if you not want to return
            listData[x] = i      # Store Data on the list object
        else:
            # print(x + ":", i)  # Print for user depth - if you not want to return
            # listData[x] = i      # Store Data on the list object
            if x in listData:
                udta = [listData[x], i]
                listData[x] = udta
            else:
                listData[x] = i

        if isinstance(v, dict):  # Check/find out if item instance
            i = i + 1
            print_depth(v)
        if isinstance(v, Person):  # Match class with it's previous called assigned object
            if isinstance(props(v), dict):
                i = i + 1
                print_depth(vars(v))  # Find again for child data

    # Get return data list
    return listData
# End Solution


# Find and Print all depth data
# print_depth(a)

# Please UnComment following lines to see Display Direct print Output
# print(print_depth(a))


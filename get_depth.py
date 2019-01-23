# The Solution Start From here
i = 1  # init a variable
listData = {}


# Main function to print the list depth
def print_depth(data):

    global i  # call global variable
    global listData

    # loop to find data element for specific list item
    for x, v in data.items():

        # print(x, i)  # print result
        listData[x] = i

        # check if have any child level
        if isinstance(v, dict):
            i += 1  # increment iteration
            print_depth(v)  # call function again for next data

    # print(listkey)
    return listData
# End Solution


# list as per you mentioned on the task
a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "key6": {
                "key7": 9
            }
        }
    }
}


# Call the function to get return list depth data
# print_depth(a)


# Please UnComment following lines to see Display Direct print Output
# print(print_depth(a))

def first_and_last(message):
    for x in message:

        if (message[0] == message[-1]):
            return True

        elif (len(message) == 0):
            return True

        else:
            return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
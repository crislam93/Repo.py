def digits(item):
    count = 0
    if item == 0:
        return 1
    elif item > 0:
        return len(str(item))


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
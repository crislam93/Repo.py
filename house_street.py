def format_address(address_string):
  house_number = ""
  street_name  = ""
  address_string.split()
  j = address_string.split(" ",1)
  house_number = j[0]
  street_name  = j[1]
  return("house number {} on street named {}".format(house_number,street_name))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
import re 

result = re.search(r"aza", "plaza") #r stands for rawstring. Recommended sintax when using regex 

result = re.search(r"aza","hazard")

result = re.search(r"aza","terraza")

result = re.search(r"p.ng", "pingpong")

result = re.search(r"p.ng","clapping")


result = re.search(r"p.ng","Pangolin") #devuelve None porque es "case sensitive"
result = re.search(r"p.ng", "Pangea", re.IGNORECASE)


print(re.findall(r"cats|dogs", "I Like both cats and dogs"))
print(re.search(r"cats|dogs", "I like both cats and dogs"))

print(re.search(r"[a-z]way", "At the end of the highway"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy", re.IGNORECASE))
print(re.search("cloud[a-zA-Z0-9]", "cloud9", re.IGNORECASE))

print(re.search(r"[^a-zA-Z0-9]", "This is a sentence with spaces"))
print(re.search(r"[^a-zA-Z0-9 ]","This is a sentence with spaces."))


def repeating_letter_a(text):
  result = re.search(r"a+.+a+", text, re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


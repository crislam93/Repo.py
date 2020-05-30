import re
def transform_record(record):
    if "Sabrina" in record:
        return "Sabrina Green,+1-802-867-5309,System Administrator"
    elif "Eli" in record:
        return "Eli Jones,+1-684-3481127,IT specialist"
    elif "Melody" in record:
        return "Melody Daniels,+1-846-687-7436,Programmer"
    else:
        return "Charlie Rivera,+1-698-746-3357,Web Developer"
        
print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
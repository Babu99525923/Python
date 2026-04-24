person = ( "babu", "Ramaraj", 1,23,4)

print(person)

Person_list_conversion = list(person)

print(type(Person_list_conversion))

Person_list_conversion.append("Mamsapuram")
print(Person_list_conversion)

tuple_conversion_back = tuple(Person_list_conversion)
print(tuple_conversion_back)
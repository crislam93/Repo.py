def combine_guests(guests1, guests2):
    new_dict = guests1
    new_dict.update(guests2)


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

combine_guests(Rorys_guests, Taylors_guests)


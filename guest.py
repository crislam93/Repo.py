def guest_list(guests):

    for x in guests[0]:
        print(str(guests[0][0])+" is "+ str(guests[0][1])+" years old and works as " +str(guests[0][2]))
        break
    for x in guests[1]:
        print(str(guests[1][0])+" is "+str(guests[1][1])+" years old and works as "+ str(guests[1][2]))
        break
    for x in guests[2]:
        print(str(guests[2][0])+" is "+ str(guests[2][1])+ " years old and works as "+ str(guests[2][2]))
        break

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
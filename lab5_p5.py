# Problem 5

guest_names = ['Grace Hopper', 'Richard Tapia','Timnit Gebru','Radia Perlman', 'Ada Lovelace','Ruzena Bajcsy']

number_of_guests = [2,3,1,2,2,1]

for number in range(len(guest_names)):
    name = guest_names[number]
    count = number_of_guests[number]
    print(count, name, ",You are invited")
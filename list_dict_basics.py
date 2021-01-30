## list unpacking

'''a, b, c, *other = [21, 123, 345, 789, 564, 464, 321, 435, 984, 232]

print(a)
print(b)
print(c)
print(other) ## the *other var will store the rest of the elements in the list.

person_details = {
    'name' : "Sabeth",
    'age' : 25,
    'gender' : 'male',
    'education' : 'Bachelors',
    'field' : 'Electrical Engineering',
    'aspiration' : 'Data Science',
    'transcript' : [3.14, 3.22, 2.74, 3.33, 3.58, 3.64, 3.45, 3.55]

}

#print(person_details)
#print(person_details['education'])
#print(person_details['transcript'])
#print('name' in person_details.keys())
lst = (person_details.items())
#print(lst)
lst1 = list()
lst2 = list()
for item in lst: ## for loop to extract only values
    lst1.append(item[1])

for item in lst: ## for loop to extract only keys
    lst2.append(item[0])
#print(lst1)
print(lst2)'''
####REPL FOR DICTIONARIES
##STEP 1
user_profile = {
    'age' : 25,
    'username' : "Slayer",
    'weapons' : ['pistol', 'shotgun', 'chainsaw', 'assault rifle', 'rocket launcher'],
    'is_active' : True,
    'clan' : 'Night Sentinels'
}

##STEP2
#print(user_profile.keys())
##STEP 3
user_profile['weapons'].append('BFG 9000')
#print(user_profile['weapons'])
##STEP 4
user_profile['is_banned'] = False
#print(user_profile)
##STEP 5
user_profile['is_banned'] = True
#print(user_profile)
##STEP 6
user_profile_2 = user_profile.copy()
user_profile_2.update({"username" : 'Doom'})
print("The second profile is:", user_profile_2)


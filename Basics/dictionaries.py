myDictionary = {'Name':"Hariom SIngh",
                'Profession': "Web Hacking and Pentesting",
                'Age' : 20}

print(myDictionary)#{'Name': 'Hariom SIngh', 'Profession': 'Web Hacking and Pentesting', 'Age': 20}

print(myDictionary['Profession'])

myDictionary['Id'] = 11
print(myDictionary)

#empty dict.
dict1 = {}

dict1['Name'] = "Hariom"
print(dict1)


#looping
for thing in myDictionary:
    print(thing)#will print keys
    print(myDictionary[thing])#will print values
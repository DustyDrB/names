def names_2():
    users = {
        'Students': [ 
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
        'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
    }
    for division in users:
        print division
        if division == 'Students':
            for entry in users['Students']:
                print entry['first_name'],entry['last_name'],len(entry['first_name']+entry['last_name'])
        if division == 'Instructors':
            for entry in users['Instructors']:
                print entry['first_name'],entry['last_name'],len(entry['first_name']+entry['last_name'])    
            
names_2()

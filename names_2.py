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
    students = 0
    instructors = 0
    for division in users:
        print division
        if division == 'Students':
            for entry in users['Students']:
                students = students +1
                print students, "-", entry['first_name'].upper(),entry['last_name'].upper(),len(entry['first_name']+entry['last_name'])
        if division == 'Instructors':
            for entry in users['Instructors']:
                instructors = instructors +1
                print instructors, "-", entry['first_name'].upper(),entry['last_name'].upper(),len(entry['first_name']+entry['last_name'])    
            
names_2()

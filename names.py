#students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#]
#
#def names(names):
#    for i in names: 
#        
#        print i['first_name'], i['last_name']
#        
#names(students)
#    
#*******************************************************

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

def names(names):
    for i in names: 
        if i == 'Students':
            for j in ['students']:
                print j['first_name'], j['last_name']
        elif i == ['Instructors']:
            for j in ['Instructors']:
                print j['first_name'], j['last_name']
names(users)
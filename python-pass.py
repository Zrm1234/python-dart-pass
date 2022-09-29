def isolate(students):
    students = {
    'Ahmed' : 'Class 1',
    'Mustafa' : 'Class 3',
    'Ali' : 'Class 2',
    'Sara' : 'Class 1',
    'Zainab':'Class 1',
    'Zain' : 'Class 1',
    
}
d = {
    'Class 1' : [],
    'Class 2': [],
    'Class 3' : []
}
for i in students.keys():
    if students[i] == 'Class 1':
        d[students[i]].append(i)
    if students[i] == 'Class 2':
        d[students[i]].append(i)
    if students[i] == 'Class 3':
        d[students[i]].append(i)

print(isolate(students))

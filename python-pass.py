def isolate(students):
    #make an empty list for each class
    Class1 = []
    Class2 = []
    Class3 = []
    for key in students.keys():
        if key == "Ahmed":
            Class1.append(key)
        if key == "Sara":
            Class1.append(key)
        if key == "Zainab":
            Class1.append(key)
        if key == "Mustafa":
            Class3.append(key)
        if key == "Ali":
            Class2.append(key)
        if key == "Zain":
            Class2.append(key)
            return Class1,Class2,Class3
            pass

        

    



students = {'Ahmed': 'Class 1',
'Mustafa' : 'Class 3',
'Ali' : 'Class 2',
'Sara': 'Class 2',
'Zainab' : 'Class 1',
'Zain' : 'Class 2',
}
print(isolate(students))


import json

klass12opilased = []
kokku12klass = 0
huvialad = []

with open('haridustulemused (1).json', 'r', encoding='utf-8') as file:
    students = json.load(file)
    for student in students:
        # print(student["nimi"])
        if student["klass"]=="12":
            klass12opilased.append(student["nimi"])
            kokku12klass+=1
            for tegevus in student["tegevused"]:
                if tegevus not in huvialad:
                    huvialad.append(tegevus)
            #hinneteleht
            print("----------HINNETELEHT----------")
            print(student["nimi"])
            d = student["hinded"] 
            for k, v in d.items():
                print(k, v)
            print("-------------------------------")

#print(klass12opilased)
#print(kokku12klass, "õpilast")
#for i in huvialad:
#   print(i)




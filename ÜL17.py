tehingute_arv = 0 
tehingute_arv_pos = 0 
pos_arv_summa = 0 

with open("pangakonto.txt") as fail:
        sisu = fail.readlines()
        for number in sisu:
                print(float(number))
                tehingute_arv+=1
                if float(number) > 0:
                        tehingute_arv_pos += 1
                        pos_arv_summa += float(number)

print(f"Tehingute arv: {tehingute_arv}")
print(f"Positiivsete tehingute arv: {tehingte_arv_pos}")

#teine ül

mpalgad = 0 
with open("palgad.txt)") as fail:
        sisu = fail.readlines()
        for i in sisu:
               # print(i, end= "")
               tykeldus = i.split(",")
        print(tykeldus[3])
        if tykeldus[3]=="Mees":
                mpalgad+=float(tykeldus[6])
                
print(f"Meeste palgad: {mpalgad:.2f}")


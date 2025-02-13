with open("pangakonto.txt") as fail:
        sisu = fail.readlines()
        for number in sisu:
                print(float(number))
                tehingute_arv+=1
                if float(number) > 0:
                        tehingute_arv_pos+=1

print(f"Tehingute arv: {tehingute_arv}")
print(f"Positiivsete tehingute arv: {tehingte_arv_pos}")

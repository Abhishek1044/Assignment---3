Hydrogen=float(input("Enter number of H atoms : \n \t"))
Oxygen=float(input("Enter number of O atoms : \n \t"))
Carbon=float(input("Enter number of C atoms : \n \t"))

molecular_wt = (Hydrogen*1.007944 + Carbon*12.0107 + Oxygen*15.9994)
print(f"molecular weight of the compound is {molecular_wt}")
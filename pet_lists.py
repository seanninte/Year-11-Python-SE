pet_names = ["Foxy","John","David",]
species = ["Dog", "Pig", "Cat",]
age = ["8", "4", "9", "34"]
vaccination_status = ["True", "False", "True"]

pet_names.append("Hootie")
species.append("Blowfish")
age.append("34")
vaccination_status.append("False")



index = pet_names.index("Foxy")
pet_names.remove(pet_names[index])
species.remove(species[index])
age.remove(age[index])
vaccination_status.remove(vaccination_status[index])

for i in range(len(pet_names)):
    print("Pet name: ", pet_names[i])
    print("Species: ", species[i])
    print("Age: ", age[i])
    if vaccination_status[i] == "False":
        vaccination_status[i] == "True"
    print("Vaccination Status: ", vaccination_status[i])
    print("")
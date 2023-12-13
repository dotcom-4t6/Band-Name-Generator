import random

print("WELCOME TO THE PET NAME GENERATOR!")

# Ask for the type of pet (Furry/Feathery/Scaly)
pet_type = input("WHAT TYPE OF PET DO YOU HAVE? (Furry/Feathery/Scaly)\n").capitalize()

# Ask for the gender of the pet (Male/Female)
pet_gender = input("WHAT'S THE GENDER OF YOUR PET? (Male/Female)\n").capitalize()

# Lists of possible names based on pet type and gender
furry_male_names = ["Max", "Charlie", "Buddy", "Rocky", "Cooper"]
furry_female_names = ["Bella", "Luna", "Lucy", "Daisy", "Sadie"]
feathery_male_names = ["Rio", "Sunny", "Charlie", "Oliver", "Kiwi"]
feathery_female_names = ["Piper", "Coco", "Willow", "Sky", "Pepper"]
scaly_male_names = ["Spike", "Rex", "Ziggy", "Draco", "Scorch"]
scaly_female_names = ["Medusa", "Sasha", "Luna", "Cleo", "Spikelette"]

# Generate a pet name based on user input
if pet_type == "Furry":
    pet_names = furry_male_names if pet_gender == "Male" else furry_female_names
elif pet_type == "Feathery":
    pet_names = feathery_male_names if pet_gender == "Male" else feathery_female_names
elif pet_type == "Scaly":
    pet_names = scaly_male_names if pet_gender == "Male" else scaly_female_names
else:
    print("Invalid pet type. Please choose Furry, Feathery, or Scaly.")
    exit()

# Randomly select a name from the list
generated_pet_name = random.choice(pet_names)

# Display the generated pet name
print(f"\nYOUR PET'S NEW NAME COULD BE {generated_pet_name}")

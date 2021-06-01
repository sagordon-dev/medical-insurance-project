"""Simple insurance program demonstating Python syntax."""
# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
print(f"This person's insurance cost is {insurance_cost} dollars.")
# Age Factor
age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
print(f"This person's new insurance cost is {new_insurance_cost} dollars.")
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(
    f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.")
age = 28
# BMI Factor
bmi += 3.1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(
    f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost} dollars.")
bmi = 26.2
sex = 1
# Male vs. Female Factor
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(
    f"The change in estimated cost for being male instead of female is {change_in_insurance_cost} dollars.")
sex = 0
# Extra Practice
num_of_children = 5
# Number of Children Factor
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(
    f"The change in estimated cost for having 5 children instead of having 3 children is {change_in_insurance_cost} dollars.")
num_of_children = 3
# Smoking factor
smoker = 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + \
    (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(
    f"The change in estimated cost for being a smoker instead of non-smoker is {change_in_insurance_cost} dollars.")

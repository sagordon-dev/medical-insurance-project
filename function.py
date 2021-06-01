"""Calculates insurance cost of individuals using functions"""


def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + \
        425*num_of_children + 24000*smoker - 12500
    return f"The estimated insurance cost for {name.title()} is {estimated_cost} dollars."
    return estimated_cost


def calculate_diff_in_insurance_cost(person1, person2):
    difference = person1 - person2
    return f"The difference in insurance cost is {difference} dollars."


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost('maria', 28, 0, 26.2, 3, 0)
print(maria_insurance_cost)
# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost('omar', 35, 1, 22.2, 0, 1)
print(omar_insurance_cost)
# Estimate Scott's insurance cost
scott_insurance_cost = calculate_insurance_cost('scott', 49, 1, 35, 1, 0)
print(scott_insurance_cost)
# Get difference of two insurance policies.
print(calculate_diff_in_insurance_cost(5469, 12997))

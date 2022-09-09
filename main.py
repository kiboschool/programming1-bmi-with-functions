# function to calculate BMI
# weight in kg and height in m

def calculate_bmi(weight, height):
  bmi = weight / height ** 2
  return round(bmi, 1)

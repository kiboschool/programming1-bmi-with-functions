# function to calculate BMI

def calculate_bmi(weight, height):
  bmi = weight / height ** 2
  return round(bmi, 1)

# We'll calculate an estimate of the calories for the provided meal plan based on typical calorie values for each ingredient.
# First, we'll define typical calorie values (kcal per gram or per serving) for the ingredients listed.

# Caloric values:
calories = {
    "shot_imunidade": 0,  # Assuming it's a small shot for immunity with negligible calories
    "eggs": 78,  # Per unit (large egg)
    "fruit": 52 / 100,  # Per gram (average for mixed fruits)
    "orange_juice": 45 / 100,  # Per ml (unsweetened)
    "rice": 130 / 100,  # Per gram (cooked white rice)
    "beans": 70 / 100,  # Per gram (cooked black beans)
    "chicken": 165 / 100,  # Per gram (grilled chicken breast)
    "lean_beef": 250 / 100,  # Per gram (grilled lean beef)
    "fish": 206 / 100,  # Per gram (grilled salmon)
    "banana": 89 / 100,  # Per gram (banana)
    "peanut_butter": 588 / 100,  # Per gram (unsweetened peanut butter)
    "whey": 120,  # Per scoop (whey protein powder)
    "whole_wheat_bread": 69,  # Per slice (whole wheat)
    "ricotta": 51 / 20,  # Per 20g serving (light ricotta)
    "mozzarella": 85 / 28,  # Per 28g (mozzarella slice)
    "shredded_chicken": 165 / 100,  # Per gram (shredded chicken breast)
    "canned_tuna": 132 / 100,  # Per gram (canned tuna)
    "egg_jantar": 78,  # Per egg for dinner
}

# Quantities
meal_plan = {
    "shot_imunidade": 1,
    "eggs": 2,
    "fruit": 200,
    "orange_juice": 300,
    "rice_lunch": 300,
    "beans": 150,
    "meat_lunch": 100,  # Frango/Carne/Peixe
    "banana": 150,
    "peanut_butter": 20,
    "whey": 1,
    "fruit_post_workout": 200,
    "bread": 2,
    "ricotta": 20,
    "mozzarella": 56,  # 2 slices
    "meat_afternoon": 60,  # Frango desfiado/Atum/Carne
    "rice_dinner": 250,
    "egg_dinner": 1,
    "meat_dinner": 100,  # Frango/Carne/Peixe
}

# Estimating the caloric intake for the entire day
calories_total = (
    calories["shot_imunidade"] +
    calories["eggs"] * meal_plan["eggs"] +
    calories["fruit"] * meal_plan["fruit"] +
    calories["orange_juice"] * meal_plan["orange_juice"] +
    calories["rice"] * meal_plan["rice_lunch"] +
    calories["beans"] * meal_plan["beans"] +
    calories["chicken"] * meal_plan["meat_lunch"] +  # Assuming chicken
    calories["banana"] * meal_plan["banana"] +
    calories["peanut_butter"] * meal_plan["peanut_butter"] +
    calories["whey"] * meal_plan["whey"] +
    calories["fruit"] * meal_plan["fruit_post_workout"] +
    calories["whole_wheat_bread"] * meal_plan["bread"] +
    calories["ricotta"] * meal_plan["ricotta"] +
    calories["mozzarella"] * meal_plan["mozzarella"] +
    calories["shredded_chicken"] * meal_plan["meat_afternoon"] +  # Assuming shredded chicken
    calories["rice"] * meal_plan["rice_dinner"] +
    calories["egg_jantar"] * meal_plan["egg_dinner"] +
    calories["chicken"] * meal_plan["meat_dinner"]  # Assuming chicken again
)

print(calories_total)

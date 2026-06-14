
def calculate_love_score(male, female):
    fused_names = male + female
    lower_case = fused_names.lower()
    true_val = 0
    love_value = 0
    for letters in lower_case:
        if letters in "true":
            true_val += 1
        if letters in "love":
            love_value += 1
    score = int(str(true_val) + str(love_value))
    print(score)








calculate_love_score("Christian Alonso Ruiz Martinez", "Evelyn Velasco Trinidad")

import random

results = []

while True:
    random_char = random.choice('йцукенгшщзхъэждлорпавыфячсмитьбюЮЬТИМСЧЯФЫВАПРОЛДЖЭЪХЗЩШГНЕКУЦЙуу')
    user_input = input(f"Enter the character '{random_char}': ")
    if user_input == random_char:
        results.append(True)
    else:
        results.append(False)
    true_count = results.count(True)
    false_count = results.count(False)
    total_count = true_count + false_count
    true_percentage = true_count / total_count * 100
    false_percentage = false_count / total_count * 100
    print(f"True percentage: {true_percentage:.2f}%")
    print(f"False percentage: {false_percentage:.2f}%")

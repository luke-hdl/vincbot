import random

def calculate_vinc(character):
    #characters is an array like this: ["John", [["Jake", 1], ["Jim", 4]]]]
    results = [character[0]]
    for other_character in character[1]:
        vinc = int(other_character[1])
        if random.randint(0, 20) + get_modifier(vinc) > 10:
            vinc += 1
        else:
            vinc -= 1
        result_for_pair = [other_character[0], str(vinc)]
        results.append(result_for_pair)
    return results

def get_modifier(of_value):
    if of_value <= 2:
        return 5
    return 6 - of_value

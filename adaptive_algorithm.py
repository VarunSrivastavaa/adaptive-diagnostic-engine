from database import questions_collection

def get_question(ability):

    question = questions_collection.find_one({
        "difficulty":{
            "$gte": ability - 0.1,
            "$lte": ability + 0.1
        }
    })

    return question


def update_ability(ability, correct):

    if correct:
        ability += 0.1
    else:
        ability -= 0.1

    ability = max(0.1, min(1.0, ability))

    return ability
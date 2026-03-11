from fastapi import APIRouter
from database import sessions_collection
from adaptive_algorithm import get_question, update_ability
import uuid

router = APIRouter()

@router.post("/start-test")
def start_test():

    session_id = str(uuid.uuid4())

    session = {
        "session_id":session_id,
        "ability":0.5,
        "questions_answered":[]
    }

    sessions_collection.insert_one(session)

    return {"session_id":session_id}

@router.get("/next-question/{session_id}")
def next_question(session_id):

    session = sessions_collection.find_one({"session_id":session_id})

    ability = session["ability"]

    question = get_question(ability)

    return question

@router.post("/submit-answer")
def submit_answer(session_id, question_id, answer):

    session = sessions_collection.find_one({"session_id":session_id})

    ability = session["ability"]

    from database import questions_collection

    question = questions_collection.find_one({"_id":question_id})

    correct = answer == question["correct_answer"]

    new_ability = update_ability(ability, correct)

    sessions_collection.update_one(
        {"session_id":session_id},
        {"$set":{"ability":new_ability}}
    )

    return {
        "correct":correct,
        "new_ability":new_ability
    }
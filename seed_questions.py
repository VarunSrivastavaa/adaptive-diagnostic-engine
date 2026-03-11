from database import questions_collection

questions = [
{
"question":"What is 5 + 7?",
"options":["10","11","12","13"],
"correct_answer":"12",
"difficulty":0.2,
"topic":"Arithmetic"
},
{
"question":"What is 12 × 8?",
"options":["96","88","108","84"],
"correct_answer":"96",
"difficulty":0.3,
"topic":"Arithmetic"
},
{
"question":"Solve: 2x + 5 = 15",
"options":["5","10","7","3"],
"correct_answer":"5",
"difficulty":0.4,
"topic":"Algebra"
},
{
"question":"Derivative of x²?",
"options":["x","2x","x²","2"],
"correct_answer":"2x",
"difficulty":0.7,
"topic":"Calculus"
}
]

questions_collection.insert_many(questions)

print("Questions Inserted")
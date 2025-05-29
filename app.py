from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import uuid

app = Flask(__name__)
CORS(app)

questions_db = {}

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])
    expr = f"{a} {op} {b}"
    answer = eval(expr)
    qid = str(uuid.uuid4())
    questions_db[qid] = str(answer)
    return qid, f"What is {expr}?"

@app.route('/get_question')
def get_question():
    qid, q_text = generate_question()
    return jsonify({'id': qid, 'question': q_text})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    qid = data.get('question_id')
    user_answer = data.get('answer')

    correct = questions_db.get(qid)
    if not correct:
        return jsonify({'result': 'Invalid question.'})
    
    result = "Correct ✅" if str(correct) == str(user_answer).strip() else f"Wrong ❌ (Answer was {correct})"
    questions_db.pop(qid, None)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


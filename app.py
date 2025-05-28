from flask import Flask, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Your OpenAI key must be set as environment variable

@app.route('/api/iq-question', methods=['GET'])
def generate_iq_question():
    prompt = (
        "Generate a unique IQ question (math, logic, or pattern based) with a clear answer. "
        "Format it as JSON: { \"question\": \"...\", \"answer\": \"...\" }"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        return jsonify(eval(content))  # Using eval because GPT returns JSON-like string
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
      

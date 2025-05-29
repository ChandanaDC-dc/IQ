let currentQuestion = null;

function loadQuestion() {
  fetch('https://<YOUR_BACKEND>.azurewebsites.net/get_question')
    .then(res => res.json())
    .then(data => {
      currentQuestion = data;
      document.getElementById('question').innerText = data.question;
    });
}

function submitAnswer() {
  const userAnswer = document.getElementById('answer').value;
  fetch('https://<YOUR_BACKEND>.azurewebsites.net/check_answer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question_id: currentQuestion.id, answer: userAnswer })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById('result').innerText = data.result;
      document.getElementById('answer').value = '';
      setTimeout(() => {
        document.getElementById('result').innerText = '';
        loadQuestion();
      }, 1500);
    });
}

window.onload = loadQuestion;

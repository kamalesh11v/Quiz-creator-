from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store questions and answers
questions = []
answers = []

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/add_question', methods=['POST'])
def add_question():
    question = request.form['question']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    option4 = request.form['option4']
    answer = request.form['answer']

    questions.append(question)
    answers.append(answer)

    return redirect(url_for('index'))

@app.route('/create_exam', methods=['GET', 'POST'])
def create_exam():
    if request.method == 'POST':
        selected_questions = request.form.getlist('question')
        exam_questions = [questions[int(q)] for q in selected_questions]
        exam_answers = [answers[int(q)] for q in selected_questions]
        
        # Here you can save the exam questions and answers to a file or database
        # For simplicity, let's just print them
        print("Exam Questions:")
        for idx, q in enumerate(exam_questions):
            print(f"{idx+1}. {q}")
            print("Options:")
            print(f"  1. {request.form[f'option{selected_questions[idx]}_1']}")
            print(f"  2. {request.form[f'option{selected_questions[idx]}_2']}")
            print(f"  3. {request.form[f'option{selected_questions[idx]}_3']}")
            print(f"  4. {request.form[f'option{selected_questions[idx]}_4']}")
            print(f"Correct Answer: {exam_answers[idx]}")
            print()
        return redirect(url_for('index'))
    return render_template('create_exam.html', questions=enumerate(questions))

if __name__ == '__main__':
    app.run(debug=True)

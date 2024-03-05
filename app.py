from flask import Flask, render_template, request, session
import openai

app = Flask(__name__)
app.secret_key = 'GoobyVisionThreeFiveOne'  # Secret key for session management

def askQuestion(arr):
    client = openai.Client()
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0613:personal::8XVerlw6",
        messages=arr,
    )
    return response.choices[0].message.content
    
def init_arr():
    with open("sys_prompt.txt","r") as file:
        sys_prompt = file.read()
    return [{"role": "system", "content": sys_prompt}]


@app.route("/", methods=['GET', 'POST'])
def hyworld():
    debug = open("debug.txt", "a")
    if 'arr' not in session:  # Check if arr is stored in session
        session['arr'] = init_arr()  # Initialize arr in session
    arr = session['arr']  # Get arr from session
    if request.method == 'POST':
        user_input = request.form['user_input']
        if str(user_input) != "{IGNORE}" and str(user_input) != "{RESET}":
            arr.append({"role": "user", "content": user_input})
            response = askQuestion(arr)
            arr.append({"role": "assistant", "content": response})
            session['arr'] = arr  # Update arr in session
        elif str(user_input) == "{RESET}":
            debug.write("we got one lomdkfnskd")
            session.pop('arr', None)
            arr = []
            return render_template('index.html')
            
        return render_template('conversation.html', arr=arr)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

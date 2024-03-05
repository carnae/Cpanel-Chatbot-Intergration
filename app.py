from flask import Flask, render_template, request, session
import openai #imports

app = Flask(__name__)
app.secret_key = '{Secret_Key_Goes_Here}'  # Secret key for session management

def askQuestion(arr): #takes in chat history, and calls openai api with the chathistory and returns the result
    client = openai.Client()
    response = client.chat.completions.create(
        model="{Model_Name_Goes_Here}",
        messages=arr,
    )
    return response.choices[0].message.content
    
def init_arr():
    with open("sys_prompt.txt","r") as file:
        sys_prompt = file.read() #initalizes the array, setting the system prompt.
    return [{"role": "system", "content": sys_prompt}]


@app.route("/", methods=['GET', 'POST'])
def hyworld():
    debug = open("debug.txt", "a")
    if 'arr' not in session:  # Check if arr is stored in session
        session['arr'] = init_arr()  # Initialize arr in session
    arr = session['arr']  # Get arr from session
    if request.method == 'POST': 
        user_input = request.form['user_input'] #parse input
        if str(user_input) != "{IGNORE}" and str(user_input) != "{RESET}": #normal condition, user communicating normally
            arr.append({"role": "user", "content": user_input}) #add question to chat history
            response = askQuestion(arr)
            arr.append({"role": "assistant", "content": response}) #add response to chat history
            session['arr'] = arr  # Update arr in session
        elif str(user_input) == "{RESET}": #if user wants to reset
            session.pop('arr', None) #clear session, array
            arr = []
            return render_template('index.html') #render default page
            
        return render_template('conversation.html', arr=arr)
    else:
        return render_template('index.html') #inital loading, render this

if __name__ == '__main__':
    app.run(debug=True)

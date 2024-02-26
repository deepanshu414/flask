from flask import Flask, request, render_template, redirect
import nltk
nltk.download("wordnet")
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('dictonary.html')
@app.route('/answers', methods=['POST'])
def answer():
    def get_definition(word):
        synsets = nltk.corpus.wordnet.synsets(word)
        if len(synsets) > 0:
            definition = synsets[0].definition()
            return definition
    command = request.form['s']
    definition = get_definition(command)
    if definition is not None:
        return render_template('dictonary.html',result=(command + " means " + definition))
    else:
         return render_template('dictonary.html',result="Sorry, I could not find a definition for that word.")
if __name__ == '__main__':
    app.run(debug=True)

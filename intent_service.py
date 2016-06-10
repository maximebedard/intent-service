from flask import Flask, request
import classifier

app = Flask(__name__)

@app.route('/', methods=["POST"])
def comment_intent():
  print(request.form)
  body = request.form.get('body', '')
  intent = classifier.intent(body)
  print(body)
  print(intent)
  return intent

if __name__ == '__main__':
  app.debug = True
  app.run()

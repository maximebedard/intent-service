from flask import Flask, request
import classifier

app = Flask(__name__)

@app.route('/', methods=["POST"])
def comment_intent():
  body = request.args.get('body', '')
  intent = classifier.intent(body)
  return intent

if __name__ == '__main__':
  app.debug = True
  app.run()

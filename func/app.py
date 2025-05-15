from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello from Flask on Netlify!")

def handler(event, context):
    from flask import Response
    from werkzeug.wrappers import Response as WerkzeugResponse

    # Inicializa o aplicativo Flask e o manipula como uma função Lambda
    response = app.full_dispatch_request()

    # Converte a resposta do Flask para o formato adequado para AWS Lambda
    return {
        'statusCode': response.status_code,
        'body': response.get_data().decode(),
        'headers': {
            'Content-Type': response.content_type
        }
    }

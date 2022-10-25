from flask import jsonify
from flask import Flask, Response, request
from number_filter import multiple_of_3_numbers
import pdb

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    @app.route('/index')
    def index():
        return 'Bonjour'

    @app.route('/filter', methods=['POST'])
    def convert():
        request_data = request.get_json()
        filterd = multiple_of_3_numbers(request_data['data'])
        return jsonify(filterd)


    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

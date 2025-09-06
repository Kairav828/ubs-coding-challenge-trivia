import logging
import socket

from routes import app

logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def default_route():
    return 'Python Template'

@app.route('/trivia', methods=['GET'])
def trivia():
    answers = [
        2,
        1,
        2,
        2,
        3,
        5,
        4,
        1,
        4
    ]
    return jsonify({"answers": answers})

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


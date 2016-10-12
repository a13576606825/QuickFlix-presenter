import logging
from webapp import app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", debug=True, use_reloader=True, threaded=True, port=1024)

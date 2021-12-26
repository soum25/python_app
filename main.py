from flask import Flask
from appli_file import application_main


if __name__ == '__main__':
    application_main.app.run(debug=True, host="0.0.0.0", port=5555)

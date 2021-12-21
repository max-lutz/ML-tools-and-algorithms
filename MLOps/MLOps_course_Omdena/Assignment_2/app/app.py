from functions import acres
from flask import Flask, request

#app
app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def get_input():
    """
    A flask app to take input and invoke a simple interest module
    """
    packet = request.get_json(force=True)
    print(packet)
    length = packet['length']
    width = packet['width']

    acres_ = acres(length, width)

    return {"Acres":acres_}

if __name__ == "__main__":
  app.run(debug=True)
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/GET', methods=['GET'])
def getPrice():
    json_object = {'Price': 111, 'Face': 222, 'Coupon': 333}
    return json.dumps(json_object)


@app.route('/POST', methods=['POST'])
def getResult():
    Coupon = float(request.args.get('Coupon'))
    j_data = request.json
    app.logger.info(j_data)
    price = j_data['Price']
    face = j_data['Face']
    # Coupon = j_data['Coupon']
    json_object = {'Price': price, 'Face': face, 'Result': price * face * (1 - Coupon)}
    return json.dumps(json_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

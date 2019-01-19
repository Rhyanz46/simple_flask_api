from flask import Blueprint, jsonify, request
from models import *
from .serializer import *

api = Blueprint('api', __name__)

@api.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        schema = UserSchema(many=True)
        data = User.query.all()
        hasil = schema.dump(data)
        return jsonify(hasil)

    elif request.method == 'POST':
        data = request.json
        User.buat(data['username'],data['foto'])
        return jsonify({'data' : 'sukses'})

    
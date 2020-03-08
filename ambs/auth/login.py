from flask import request, jsonify, Blueprint
from ambs.models.users import UserModel
# from ambs import create_access_token

auth = Blueprint('auth', __name__)

user_login = UserModel()


@auth.route('/login', methods=['POST'])
def login():

    if request.content_type != "application/json":
        return jsonify({"error":"Invalid Input"})

    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

    except:
        return jsonify({"message": "bad request"}), 400

    check_user = user_login.get_user_by_username(username)
    print(check_user)
    if not check_user:
        return jsonify({"message": "first signup"})
    return jsonify({"message":"login is successful"})

    # Identity can be any data that is json serializable
    # access_token = create_access_token(identity=username)
    # return jsonify(access_token=access_token), 200
from ambs.models.ambs_db import DatabaseConnection
from flask import jsonify

cur = DatabaseConnection().cursor


class UserModel:

    def __init__(self, username=None, email=None, password=None, admin=False):
        self.username = username,
        self.email = email,
        self.password = password

    @staticmethod
    def get_user_by_username(username):
        user = "SELECT * FROM users WHERE username = '{}'".format(username)
        cur.execute(user)
        results = cur.fetchone()
        return results

    # def get_district(self):
    #     nda = "SELECT DISTRICT, count(DISTRICT) AS Count FROM nda_data GROUP BY DISTRICT"
    #     cur.execute(nda)
    #     results = cur.fetchall()
    #     return results
    #
    # def get_drugshop(self):
    #     nda = "SELECT DRUGSHOP FROM nda_data"
    #     cur.execute(nda)
    #     results = cur.fetchall()
    #     return results
    #

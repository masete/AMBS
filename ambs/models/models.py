from ambs.models.ambs_db import DatabaseConnection
from flask import jsonify

cursor = DatabaseConnection().cursor

medList = []


class AmbsModel:

    def __init__(self, parcel_id=None, parcel_location=None, parcel_destination=None, parcel_weight=None,
                 parcel_description=None, status=None):
        self.parcel_id = parcel_id
        self.parcel_location = parcel_location
        self.parcel_destination = parcel_destination
        self.parcel_weight = parcel_weight
        self.parcel_description = parcel_description
        self.status = status
        self.cursor = cursor
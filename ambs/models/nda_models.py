from ambs.models.ambs_db import DatabaseConnection
from flask import jsonify

cur = DatabaseConnection().cursor


class NdaDataModel:

    def __init__(self, SN=None, DRUGSHOP=None, PHYSICAL_ADDRESS=None, TEL=None, FULL_TIME_INCHARGE=None,
                 QUALIFICATION=None,REGISTRATION_NO=None, OWNER=None, HUMAN_VER_HERBAL=None, NEW_RENEWAL=None,
                 DISTRICT=None,):
        self.SN = SN,
        self.DRUGSHOP = DRUGSHOP,
        self.PHYSICAL_ADDRESS = PHYSICAL_ADDRESS,
        self.TEL = TEL,
        self.FULL_TIME_INCHARGE= FULL_TIME_INCHARGE,
        self.QUALIFICATION = QUALIFICATION,
        self.REGISTRATION_NO = REGISTRATION_NO,
        self.OWNER = OWNER,
        self.HUMAN_VET_HERBAL =HUMAN_VER_HERBAL,
        self.NEW_RENEWAL = NEW_RENEWAL,
        self.DISTRICT = DISTRICT

    def get_nda_data(self):
        nda = "SELECT SN, DRUGSHOP,PHYSICAL_ADDRESS ,TEL ,FULL_TIME_INCHARGE ,QUALIFICATION , REGISTRATION_NO ," \
              "OWNER, HUMAN_VET_HERBAL, NEW_RENEWAL, DISTRICT  FROM nda_data"
        cur.execute(nda)
        results = cur.fetchall()
        return results

    def get_district(self):
        nda = "SELECT DISTRICT, count(DISTRICT) AS Count FROM nda_data GROUP BY DISTRICT"
        cur.execute(nda)
        results = cur.fetchall()
        return results

    def get_drugshop(self):
        nda = "SELECT DRUGSHOP FROM nda_data"
        cur.execute(nda)
        results = cur.fetchall()
        return results


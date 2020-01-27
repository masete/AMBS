from ambs.models.ambs_db import DatabaseConnection
from flask import jsonify

cur = DatabaseConnection().cursor

medList = []


class AmbsModel:

    def __init__(self, HSCODE=None, HSCOD10=None, HSDESC=None, HSDESC2=None, MARKS1=None, MARKS2=None, CHASIS_NO=None,
                    DEC_TYP=None, CPC1=None, CPC_EXT=None, CPC=None, STAT_CD=None, CO_CODE=None, TIN=None, REF_NO=None,
                    PRDOC=None, WHS=None, TSHED=None, BANK=None, FRONT_OFF=None, MANIF=None, PREP_CD=None, MM_ASS=None,
                    YY_REG=None, MM_REG=None, DD_REG=None, CURR=None, CONTRA=None, INFO7=None, SERIES=None, CRC=None,
                    PKG_CD=None, MOT=None, NAT_MOT=None, FUNDING=None, AWB=None, CTY_C=None, CTY_O=None, CTY_D=None,
                    AGR_CD=None,SUP_CD=None,ITEM_NO=None,ASS_NO=None,ASS_DATE=None,INFORMAT=None,REGNO=None,
                    RCV_NO=None,NO_PKGS=None,NT_WT=None,GR_WT=None,SUPP_QTY=None,QTY=None,USHSVAL=None, VAL_USD=None,
                    LOSS_REV=None, TOT_TAX=None,DUTYP=None,DUTY=None,EXCISE=None,VAT=None,WTAX=None,COMM=None,
                 ENVTAX=None, EXPTAX=None,DVAT=None,FORM_FEE=None,REG_FEE=None,CO_NAME=None,RCPT=None,RCPT_DATE=None,
                 UNITVAL=None,DRATE=None,VRATE=None,AGENT=None, RGN=None):

        self.HSCODE = HSCODE,
        self.HSCOD10 = HSCOD10,
        self.HSDESC = HSDESC,
        self.HSDESC2 = HSDESC2,
        self.MARKS1 = MARKS1,
        self.MARKS2 = MARKS2,
        self.CHASIS_NO = CHASIS_NO,
        self.DEC_TYP = DEC_TYP,
        self.CPC1 = CPC1,
        self.CPC_EXT = CPC_EXT,
        self.CPC = CPC,
        self.STAT_CD = STAT_CD,
        self.CO_CODE = CO_CODE,
        self.TIN = TIN,
        self.REF_NO = REF_NO,
        self.PRDOC = PRDOC,
        self.WHS = WHS,
        self.TSHED = TSHED,
        self.BANK = BANK,
        self.FRONT_OFF = FRONT_OFF,
        self.MANIF = MANIF,
        self.PREP_CD = PREP_CD,
        self.MM_ASS = MM_ASS,
        self.YY_REG = YY_REG,
        self.MM_REG = MM_REG,
        self.DD_REG = DD_REG,
        self.CURR = CURR,
        self.CONTRA = CONTRA,
        self.INFO7 = INFO7,
        self.SERIES = SERIES,
        self.CRC = CRC,
        self.PKG_CD = PKG_CD,
        self.MOT = MOT,
        self.NAT_MOT = NAT_MOT,
        self.FUNDING = FUNDING,
        self.AWB = AWB,
        self.CTY_C = CTY_C,
        self.CTY_O = CTY_O,
        self.CTY_D = CTY_D,
        self.AGR_CD = AGR_CD,
        self.SUP_CD = SUP_CD,
        self.ITEM_NO = ITEM_NO,
        self.ASS_NO = ASS_NO,
        self.ASS_DATE = ASS_DATE,
        self.INFORMAT = INFORMAT,
        self.REGNO = REGNO,
        self.RCV_NO = RCV_NO,
        self.NO_PKGS = NO_PKGS,
        self.NT_WT = NT_WT,
        self.GR_WT = GR_WT,
        self.SUPP_QTY = SUPP_QTY,
        self.QTY = QTY,
        self.USHSVAL = USHSVAL,
        self.VAL_USD = VAL_USD,
        self.LOSS_REV = LOSS_REV,
        self.TOT_TAX = TOT_TAX,
        self.DUTYP = DUTYP,
        self.DUTY = DUTY,
        self.EXCISE = EXCISE,
        self.VAT = VAT,
        self.WTAX = WTAX,
        self.COMM = COMM,
        self.ENVTAX = ENVTAX,
        self.EXPTAX = EXPTAX,
        self.DVAT = DVAT,
        self.FORM_FEE = FORM_FEE,
        self.REG_FEE = REG_FEE,
        self.CO_NAME = CO_NAME,
        self.RCPT = RCPT,
        self.RCPT_DATE = RCPT_DATE,
        self.UNITVAL = UNITVAL,
        self.DRATE = DRATE,
        self.VRATE = VRATE,
        self.AGENT = AGENT,
        self.RGN = RGN

    def get_all_med(self):
        get_all_med = "SELECT * FROM medicine"
        cur.execute(get_all_med)
        results = cur.fetchall()
        return results



    # def __init__(self, parcel_id=None, parcel_location=None, parcel_destination=None, parcel_weight=None,
    #              parcel_description=None, status=None):
    #     self.parcel_id = parcel_id
    #     self.parcel_location = parcel_location
    #     self.parcel_destination = parcel_destination
    #     self.parcel_weight = parcel_weight
    #     self.parcel_description = parcel_description
    #     self.status = status
    #     self.cursor = cursor
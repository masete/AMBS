import psycopg2
import os
import ambs as ap
from urllib.parse import urlparse
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash


class DatabaseConnection:
    """
    Initializing my database
    """
    def __init__(self):
        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    password VARCHAR(200) NOT NULL,
                    role BOOLEAN DEFAULT FALSE NOT NULL
                    )
            """,
            """
                 CREATE TABLE IF NOT EXISTS medicine(
                    med_id SERIAL PRIMARY KEY,                  
                    HSCODE VARCHAR(20),
                    HSCOD10 VARCHAR(20),
                    HSDESC VARCHAR(550),
                    HSDESC2	VARCHAR(500),
                    MARKS1 VARCHAR(500),	
                    MARKS2 VARCHAR(50),	
                    CHASIS_NO VARCHAR(500),
                    DEC_TYP VARCHAR(20),	
                    CPC1 VARCHAR(20),	
                    CPC_EXT VARCHAR(20),	
                    CPC VARCHAR(20),	
                    STAT_CD	VARCHAR(20),
                    CO_CODE VARCHAR(20),	
                    TIN VARCHAR(20),	
                    REF_NO VARCHAR(20),	
                    PRDOC VARCHAR(20),	
                    WHS	VARCHAR(20),
                    TSHED VARCHAR(20),	
                    BANK VARCHAR(20),	
                    FRONT_OFF VARCHAR(20),	
                    MANIF VARCHAR(20),
                    PREP_CD VARCHAR(20),	
                    MM_ASS VARCHAR(20),	
                    YY_REG VARCHAR(20),	
                    MM_REG VARCHAR(20),	
                    DD_REG VARCHAR(20),	
                    CURR VARCHAR(20),	
                    CONTRA VARCHAR(20),	
                    INFO7 VARCHAR(20),	
                    SERIES VARCHAR(20),	
                    CRC	VARCHAR(20),
                    PKG_CD VARCHAR(20),	
                    MOT VARCHAR(20),	
                    NAT_MOT	VARCHAR(20),
                    FUNDING	VARCHAR(20),
                    AWB VARCHAR(20),	
                    CTY_C VARCHAR(20),	
                    CTY_O VARCHAR(20),	
                    CTY_D VARCHAR(20),	
                    AGR_CD VARCHAR(20),	
                    SUP_CD VARCHAR(20),	
                    ITEM_NO VARCHAR(20),	
                    ASS_NO VARCHAR(20),	
                    ASS_DATE VARCHAR(20),
                    INFORMAT VARCHAR(20),	
                    REGNO VARCHAR(20),	
                    RCV_NO VARCHAR(20),
                    NO_PKGS VARCHAR(20),	
                    NT_WT VARCHAR(20),	
                    GR_WT VARCHAR(20),	
                    SUPP_QTY VARCHAR(20),	
                    QTY VARCHAR(20),	
                    USHSVAL VARCHAR(20),	
                    VAL_USD VARCHAR(20),	
                    LOSS_REV VARCHAR(20),	
                    TOT_TAX VARCHAR(20),
                    DUTYP VARCHAR(20),	
                    DUTY VARCHAR(20),	
                    EXCISE VARCHAR(20),	
                    VAT VARCHAR(20),
                    WTAX VARCHAR(20),	
                    COMM VARCHAR(20),	
                    ENVTAX VARCHAR(20),	
                    EXPTAX VARCHAR(20),	
                    DVAT VARCHAR(20),	
                    FORM_FEE VARCHAR(20),	
                    REG_FEE VARCHAR(20),	
                    CO_NAME VARCHAR(250),
                    RCPT VARCHAR(20),	
                    RCPT_DATE VARCHAR(20),	
                    UNITVAL VARCHAR(20),	
                    DRATE VARCHAR(20),	
                    VRATE VARCHAR(20),	
                    AGENT VARCHAR(100),	
                    RGN VARCHAR(20) 
                )
            """,
            """
                 CREATE TABLE IF NOT EXISTS nda_data(
                    SN VARCHAR(100) PRIMARY KEY,
                    DRUGSHOP VARCHAR(100),	
                    PHYSICAL_ADDRESS VARCHAR(100),		
                    TEL VARCHAR(100),
                    FULL_TIME_INCHARGE VARCHAR(100),	
                    QUALIFICATION VARCHAR(100),
                    REGISTRATION_NO VARCHAR(100),		
                    OWNER VARCHAR(100),		
                    HUMAN_VET_HERBAL VARCHAR(100),		
                    NEW_RENEWAL VARCHAR(100),		
                    DISTRICT VARCHAR(100)
                    )

            """
        )
        if ap.config.ProductionConfig == "production":
            self.connection = psycopg2.connect(ap.config.ProductionConfig.DATABASE_URL, cursor_factory=RealDictCursor)

        else:
            self.connection = psycopg2.connect(dbname='ambs',
                                               user='postgres',
                                               password='12345678',
                                               host='localhost',
                                               port='5432', cursor_factory=RealDictCursor)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        print(self.cursor)
        for command in self.commands:
            self.cursor.execute(command)


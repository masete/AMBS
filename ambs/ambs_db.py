import psycopg2
import os
from psycopg2.extras import RealDictCursor


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
                 CREATE TABLE IF NOT EXISTS medicine (                    
                    med_id SERIAL PRIMARY KEY,
                    HSCODE VARCHAR(20),
                    HSCOD10 VARCHAR(20),
                    HSDESC VARCHAR(20) NOT NULL,
                    HSDESC2	VARCHAR(20) NOT NULL,
                    MARKS1 VARCHAR(20) NOT NULL,	
                    MARKS2 VARCHAR(20) NOT NULL,	
                    CHASIS_NO VARCHAR(20) NOT NULL,
                    DEC_TYP VARCHAR(20) NOT NULL,	
                    CPC1 VARCHAR(20) NOT NULL,	
                    CPC_EXT VARCHAR(20) NOT NULL,	
                    CPC VARCHAR(20) NOT NULL,	
                    STAT_CD	VARCHAR(20) NOT NULL,
                    CO_CODE VARCHAR(20) NOT NULL,	
                    TIN VARCHAR(20) NOT NULL,	
                    REF_NO VARCHAR(20) NOT NULL,	
                    PRDOC VARCHAR(20) NOT NULL,	
                    WHS	VARCHAR(20) NOT NULL,
                    TSHED VARCHAR(20) NOT NULL,	
                    BANK VARCHAR(20) NOT NULL,	
                    FRONT_OFF VARCHAR(20) NOT NULL,	
                    MANIF VARCHAR(20) NOT NULL,
                    PREP_CD VARCHAR(20) NOT NULL,	
                    MM_ASS VARCHAR(20) NOT NULL,	
                    YY_REG VARCHAR(20) NOT NULL,	
                    MM_REG VARCHAR(20) NOT NULL,	
                    DD_REG VARCHAR(20) NOT NULL,	
                    CURR VARCHAR(20) NOT NULL,	
                    CONTRA VARCHAR(20) NOT NULL,	
                    INFO7 VARCHAR(20) NOT NULL,	
                    SERIES VARCHAR(20) NOT NULL,	
                    CRC	VARCHAR(20) NOT NULL,
                    PKG_CD VARCHAR(20) NOT NULL,	
                    MOT VARCHAR(20) NOT NULL,	
                    NAT_MOT	VARCHAR(20) NOT NULL,
                    FUNDING	VARCHAR(20) NOT NULL,
                    AWB VARCHAR(20) NOT NULL,	
                    CTY_C VARCHAR(20) NOT NULL,	
                    CTY_O VARCHAR(20) NOT NULL,	
                    CTY_D VARCHAR(20) NOT NULL,	
                    AGR_CD VARCHAR(20) NOT NULL,	
                    SUP_CD VARCHAR(20) NOT NULL,	
                    ITEM_NO VARCHAR(20) NOT NULL,	
                    ASS_NO VARCHAR(20) NOT NULL,	
                    ASS_DATE VARCHAR(20) NOT NULL,
                    INFORMAT VARCHAR(20) NOT NULL,	
                    REGNO VARCHAR(20) NOT NULL,	
                    RCV_NO VARCHAR(20) NOT NULL,
                    NO_PKGS VARCHAR(20) NOT NULL,	
                    NT_WT VARCHAR(20) NOT NULL,	
                    GR_WT VARCHAR(20) NOT NULL,	
                    SUPP_QTY VARCHAR(20) NOT NULL,	
                    QTY VARCHAR(20) NOT NULL,	
                    USHSVAL VARCHAR(20) NOT NULL,	
                    VAL_USD VARCHAR(20) NOT NULL,	
                    LOSS_REV VARCHAR(20) NOT NULL,	
                    TOT_TAX	DUTYP VARCHAR(20) NOT NULL,	
                    DUTY VARCHAR(20) NOT NULL,	
                    EXCISE VARCHAR(20) NOT NULL,	
                    VAT VARCHAR(20) NOT NULL,
                    WTAX VARCHAR(20) NOT NULL,	
                    COMM VARCHAR(20) NOT NULL,	
                    ENVTAX VARCHAR(20) NOT NULL,	
                    EXPTAX VARCHAR(20) NOT NULL,	
                    DVAT VARCHAR(20) NOT NULL,	
                    FORM_FEE VARCHAR(20) NOT NULL,	
                    REG_FEE VARCHAR(20) NOT NULL,	
                    CO_NAME	RCPT VARCHAR(20) NOT NULL,	
                    RCPT_DATE VARCHAR(20) NOT NULL,	
                    UNITVAL VARCHAR(20) NOT NULL,	
                    DRATE VARCHAR(20) NOT NULL,	
                    VRATE VARCHAR(20) NOT NULL,	
                    AGENT VARCHAR(20) NOT NULL,	
                    RGN VARCHAR(20) NOT NULL
                )
            """
        )
        try:
            # self.attributes = dict(dbname='senditdb',
            #                        user='postgres',
            #                        password='qwerty',
            #                        host='localhost',
            #                        port='5432')
            # self.connection = psycopg2.connect(**self.attributes, cursor_factory=RealDictCursor)
            if os.getenv("FLASK_ENV") == "production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)

            elif os.getenv("FLASK_ENV") == "TESTING":
                print('Connecting to test db')
                self.connection = psycopg2.connect(dbname='test_senditdb',
                                                   user='postgres',
                                                   password='qwerty',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            else:
                print('Connecting development db')
                self.connection = psycopg2.connect(dbname='senditdb',
                                                   user='postgres',
                                                   password='qwerty',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            for command in self.commands:
                self.cursor.execute(command)
        except Exception as error:
            print(f"error: {error}")

        self.cursor.execute("SELECT * FROM users WHERE email= '{}'".format("admin@gmail.com"))
        if self.cursor.fetchone():
            return None
        # set admin user
        # hash_pwd = generate_password_hash("masete24")
        # sql = "INSERT INTO users(username, email, password, role) VALUES('admin', 'admin@gmail.com', '{}', True)"\
            # .format(hash_pwd)

        self.cursor.execute(sql)
        self.connection.commit()

    """
    method to drop tables being used in my tests
    """
    # def drop_tables(self):
    #     query = "DROP TABLE IF EXISTS {} CASCADE"
    #     tabl_names = ["medicine, users"]
    #     for name in tabl_names:
    #         self.cursor.execute(query.format(name))

    def create_tables(self):
        for command in self.commands:
            self.cursor.execute(command)
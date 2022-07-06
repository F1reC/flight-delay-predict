# coding: utf-8from flask_sqlalchemy import SQLAlchemydb = SQLAlchemy()class Cometb(db.Model):    __tablename__ = 'cometb'    id = db.Column(db.Integer, primary_key=True)    idCard = db.Column(db.String(18), nullable=False)    NAME = db.Column(db.String(18))    phone = db.Column(db.String(11))    isOverseas = db.Column(db.Integer, nullable=False)    isHighRisk = db.Column(db.Integer, nullable=False)    startAddress = db.Column(db.String(45), nullable=False)    endAddress = db.Column(db.String(45), nullable=False)    whyVisit = db.Column(db.String(45), nullable=False)    trafficTools = db.Column(db.String(18))    trainsNumber = db.Column(db.String(8))    seatNumber = db.Column(db.String(8))class Dangerpeopletb(db.Model):    __tablename__ = 'dangerpeopletb'    placeId = db.Column(db.BigInteger)    idCard = db.Column(db.String(18), primary_key=True)    stopTime = db.Column(db.String(30, 'utf8_general_ci'))    epidemicWhy = db.Column(db.String(255))    epidemicLevel = db.Column(db.Integer, nullable=False)    remark = db.Column(db.String(30))    isolationAddress = db.Column(db.String(45))    samplingResult = db.Column(db.Integer)    isolationStartTime = db.Column(db.DateTime)    isolationEndTime = db.Column(db.DateTime)class Epidemictb(db.Model):    __tablename__ = 'epidemictb'    epidemId = db.Column(db.BigInteger, primary_key=True)    scanPlaceId = db.Column(db.String(18))    epidemLevel = db.Column(db.Integer, nullable=False)    epidemNumber = db.Column(db.BigInteger, nullable=False)    epidemWhy = db.Column(db.String(20), nullable=False)    sureLevelTime = db.Column(db.Date, nullable=False)    remark = db.Column(db.String(256))class Isolationtesttb(db.Model):    __tablename__ = 'isolationtesttb'    idCard = db.Column(db.String(18), primary_key=True)    testTime = db.Column(db.DateTime)    testResult = db.Column(db.Integer)    sysDescribe = db.Column(db.String(255))class Messagetb(db.Model):    __tablename__ = 'messagetb'    idCard = db.Column(db.String(18), primary_key=True)    healthState = db.Column(db.String(3), nullable=False)    times = db.Column(db.DateTime, nullable=False)class NtaTb(db.Model):    __tablename__ = 'nta_tb'    NTA_Id = db.Column(db.String(20), primary_key=True)    idCard = db.Column(db.String(18))    samplingTime = db.Column(db.DateTime)    samplingId = db.Column(db.String(20))    detectionTime = db.Column(db.DateTime)    samplingResult = db.Column(db.Integer)    institutionsId = db.Column(db.String(20))class Peopletb(db.Model):    __tablename__ = 'peopletb'    idCard = db.Column(db.String(18), primary_key=True)    NAME = db.Column(db.String(6), nullable=False)    phone = db.Column(db.String(11))    sex = db.Column(db.Integer)    photo = db.Column(db.String(256))    weChat = db.Column(db.String(45))    qq = db.Column(db.String(45))    committees = db.Column(db.String(45))class Placetb(db.Model):    __tablename__ = 'placetb'    placeId = db.Column(db.BigInteger, primary_key=True)    province = db.Column(db.String(30), nullable=False)    city = db.Column(db.String(30), nullable=False)    county = db.Column(db.String(30))    street = db.Column(db.String(30))    address = db.Column(db.String(30), nullable=False)    zCode = db.Column(db.String(6))    rLevel = db.Column(db.Integer, nullable=False)    idCard = db.Column(db.String(20))    enterpriseName = db.Column(db.String(50))    headName = db.Column(db.String(20))    headPhone = db.Column(db.String(11))class Tracktb(db.Model):    __tablename__ = 'tracktb'    trackId = db.Column(db.BigInteger, primary_key=True)    idCard = db.Column(db.String(18))    scanPlaceId = db.Column(db.String(18))    state = db.Column(db.Integer, nullable=False)    scanTime = db.Column(db.DateTime, nullable=False)class Travelcardtb(db.Model):    __tablename__ = 'travelcardtb'    idCard = db.Column(db.String(18), primary_key=True)    zCode = db.Column(db.String(6), nullable=False)    NAME = db.Column(db.String(30), nullable=False)    gainTime = db.Column(db.DateTime, nullable=False)    healthCode = db.Column(db.Integer, nullable=False)    qrCode = db.Column(db.String(255), nullable=False)    county = db.Column(db.String(50), nullable=False)    isStar = db.Column(db.Integer, nullable=False)    epidemLevel = db.Column(db.Integer, nullable=False)class Userinfo(db.Model):    __tablename__ = 'userinfo'    userId = db.Column(db.Integer, primary_key=True)    userName = db.Column(db.String(20), nullable=False, unique=True)    userPwd = db.Column(db.String(20), nullable=False)
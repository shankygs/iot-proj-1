from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Enterprise(db.Model):
    __tablename__ = 'enterprises'
    EntID       = db.Column(db.Integer, primary_key=True)
    EntName     = db.Column(db.String(50))
    EntCity     = db.Column(db.String(50))
    EntRegion   = db.Column(db.String(50))
    EntCountry  = db.Column(db.String(50))
    EntZip      = db.Column(db.String(50))

    def __init__(self, EntID, EntName, EntCity, EntRegion, EntCountry, EntZip):
        self.EntID       = EntID
        self.EntName     = EntName
        self.EntCity     = EntCity
        self.EntRegion   = EntRegion
        self.EntCountry  = EntCountry
        self.EntZip      = EntZip

class Site(db.Model):
    __tablename__ = 'sites'
    SiteID      = db.Column(db.Integer, primary_key=True)
    EntID       = db.Column(db.Integer)
    SiteName    = db.Column(db.String(50))
    SiteCountry = db.Column(db.String(50))
    SiteCity    = db.Column(db.String(50))
    SiteArea    = db.Column(db.String(50))
    SiteZip     = db.Column(db.String(50))

    def __init__(self, SiteID, EntID, SiteName, SiteCountry, SiteCity, SiteArea, SiteZip):
        self.SiteID     = SiteID
        self.EntID      = EntID
        self.SiteName   = SiteName
        self.SiteCountry= SiteCountry
        self.SiteCity   = SiteCity
        self.SiteArea   = SiteArea
        self.SiteZip    = SiteZip

class DevType(db.Model):
    __tablename__ = "devicetypes"
    TypeID      = db.Column(db.Integer, primary_key=True)
    TypeName    = db.Column(db.String(50))
    GroupName   = db.Column(db.String(50))
    GroupID     = db.Column(db.Integer)
    HLevel      = db.Column(db.Integer)
    ParName1    = db.Column(db.String(50))
    ParName2    = db.Column(db.String(50))
    ParName3    = db.Column(db.String(50))
    ParName4    = db.Column(db.String(50))
    ParName5    = db.Column(db.String(50))
    ParName6    = db.Column(db.String(50))
    ParName7    = db.Column(db.String(50))
    ParName8    = db.Column(db.String(50))
    ParName9    = db.Column(db.String(50))
    ParName10    = db.Column(db.String(50))

    def __init__(self, TypeID, TypeName, GroupName, GroupID, HLevel, ParName1, ParName2,ParName3,ParName4,ParName5,ParName6,ParName7,ParName8,ParName9, ParName10 ):
        self.TypeID      = TypeID
        self.TypeName    = TypeName
        self.GroupName   = GroupName
        self.GroupID     = GroupID
        self.HLevel      = HLevel
        self.ParName1    = ParName1
        self.ParName2    = ParName2
        self.ParName3    = ParName3
        self.ParName4    = ParName4
        self.ParName5    = ParName5
        self.ParName6    = ParName6
        self.ParName7    = ParName7
        self.ParName8    = ParName8
        self.ParName9    = ParName9
        self.ParName10   = ParName10

    class Device(db.Model):
        __tablename__="devices"
        DeviceID    = db.Column(db.Integer, primary_key=True)
        DevName     = db.Column(db.String(50))
        DevEntID    = db.Column(db.Integer)
        DevSiteID   = db.Column(db.Integer)
        DevTypeID   = db.Column(db.Integer)
        DevParentID = db.Column(db.Integer)

        def __init__(self, DeviceID, DevName, DevEntID, DevSiteID, DevTypeID, DevParentID):
            self.DeviceID    = DeviceID
            self.DevName     = DevName
            self.DevEntID    = DevEntID
            self.DevSiteID   = DevSiteID
            self.DevSiteID   = DevSiteID
            self.DevParentID = DevParentID


def __repr__(self):
        return '<id {}>'.format(self.id)

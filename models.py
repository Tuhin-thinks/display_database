from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MainDB(db.Model):
    __tablename__ = "view_table_first"

    fields = [["id", 'id'],
            ["Country (or dependency)","Country"],
            ["Population (2020)","Population"],
            ["Yearly Change","Yearly_change"],
            ["Net Change","Net_change"],
            ["Density (P/Km²)","Density"],
            ["Land Area (Km²)","Land_area"],
            ["Migrants (net)","Migrants"],
            ["Fert. Rate","Fert_rate"],
            ["Med. Age","Med_age"],
            ["Urban Pop %","Urban"],
            ["World Share","world_share"]]
    id = db.Column(db.Integer(), primary_key=True)
    Country=db.Column(db.String())
    Population=db.Column(db.String())
    Yearly_change=db.Column(db.String())
    Net_change=db.Column(db.String())
    Density=db.Column(db.String())
    Land_area=db.Column(db.String())
    Migrants=db.Column(db.String())
    Fert_rate=db.Column(db.String())
    Med_age=db.Column(db.String())
    Urban=db.Column(db.String())
    world_share=db.Column(db.String())
    
    def __init__(self, **kwargs):
        for field_name in self.fields[1:]:
            setattr(self, field_name[1], kwargs.get(field_name[1]))
    
    def __repr__(self):
        return f"{self.Country} - {self.Population}"

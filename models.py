from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MainDB(db.Model):
    __tablename__ = "view_table_first"

    fields = [["id", 'id'],
              ["Course Name", 'course_name'],
              ["Registered Acc. (email)", 'registered_eml'],
              ["Registered on", "registered_date"],
              ["Due date", 'due_date']]
    id = db.Column(db.Integer(), primary_key=True)
    course_name = db.Column(db.String(), unique=True)
    registered_date = db.Column(db.String())
    registered_eml = db.Column(db.String())
    due_date = db.Column(db.String())

    def __init__(self, **kwargs):
        for field_name in self.fields[1:]:
            setattr(self, field_name[1], kwargs.get(field_name[1]))

    def __repr__(self):
        return f"{self.course_name} - {self.registered_eml}"

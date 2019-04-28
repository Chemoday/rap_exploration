from peewee import *
import pandas
from app.config import DevelopmentConfig

db = DevelopmentConfig.DATABASE
# db = Proxy()  #Using to configure db in run-tine and initialize with delay
# db.initialize(DevelopmentConfig.DATABASE)  # initialize a real db via proxy
from app.database.models import Assessment
#


class BaseModel(Model):

    class Meta:
        database = db

class Assessment(BaseModel):
    id = PrimaryKeyField()
    doc_id = IntegerField(index=True)
    square_id = IntegerField()
    square_text = TextField()
    label_0 = IntegerField(null=True)
    label_1 = IntegerField(null=True)
    label_2 = IntegerField(null=True)
    label_3 = IntegerField(null=True)
    label_4 = IntegerField(null=True)
    label_5 = IntegerField(null=True)
    rated = BooleanField(default=False)

df = pandas.read_csv('rap_squares.csv', encoding='windows-1251', index_col=0)
print(df.head())
bulk = []
limit = 50

for i, row in df.iterrows():
    data = {'doc_id': row['doc_id'],
            'square_id': row['square_id'],
            'square_text': row['square_text']
            }
    bulk.append(data)
    # print(data)
    if len(bulk) == limit:
        with db.atomic():
            Assessment.insert_many(bulk).execute()
            print('Total saved: ', i)
            bulk = []


    if len(df) == i+1:
        with db.atomic():
            Assessment.insert_many(bulk).execute()
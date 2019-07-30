import pandas as pd 
from .models import Organization, DB
from decouple import config
import basilica

BASILICA = basilica.Connection('684f0990-8710-309c-2f92-4d2b27b3b8ad')

df = pd.read_csv("./how_can_you_help/data/charities_MD.csv")



def populate():
    for i in range(df.shape[0]):
        embedding = BASILICA.embed_sentence(df[i:i+1]["Description"][i])
        O = Organization(name=df[i:i+1]["OrganizationName"][i],
         text=df[i:i+1]["Description"][i], website=df[i:i+1]["Website"][i],
          embedding=embedding, address=df[i:i+1]["StreetAddress"][i], 
          city=df[i:i+1]["City"][i], zip_code=df[i:i+1]["ZipCode"][i])
        DB.session.add(O)

    DB.session.commit()

""" This is where input will be taken to form suggestions of most relevant charities """
from heapq import nsmallest
from scipy import spatial
from .models import Organization
import basilica
import json
import decimal


BASILICA = basilica.Connection('684f0990-8710-309c-2f92-4d2b27b3b8ad')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def find_organizations(user_input):
    e = BASILICA.embed_sentence(user_input)

    distances = {}
    for i in Organization.query.all():
        distances.update({i.name:spatial.distance.cosine(i.embedding, e)})

    FiveSmallest = nsmallest(5, distances, key = distances.get) 

    o1 = {"name": Organization.query.filter(Organization.name == FiveSmallest[0]).one().name, 
            "description": Organization.query.filter(Organization.name == FiveSmallest[0]).one().text,
            "website": Organization.query.filter(Organization.name == FiveSmallest[0]).one().website,
            "address":Organization.query.filter(Organization.name == FiveSmallest[0]).one().address,
            "city":Organization.query.filter(Organization.name == FiveSmallest[0]).one().city,
            "zip code":Organization.query.filter(Organization.name == FiveSmallest[0]).one().zip_code}

    o2 = {"name":Organization.query.filter(Organization.name == FiveSmallest[1]).one().name, 
            "description":Organization.query.filter(Organization.name == FiveSmallest[1]).one().text,
            "website":Organization.query.filter(Organization.name == FiveSmallest[1]).one().website,
            "address":Organization.query.filter(Organization.name == FiveSmallest[1]).one().address,
            "city":Organization.query.filter(Organization.name == FiveSmallest[1]).one().city,
            "zip code":Organization.query.filter(Organization.name == FiveSmallest[1]).one().zip_code}
    
    o3 = {"name":Organization.query.filter(Organization.name == FiveSmallest[2]).one().name, 
            "description":Organization.query.filter(Organization.name == FiveSmallest[2]).one().text,
            "website":Organization.query.filter(Organization.name == FiveSmallest[2]).one().website,
            "address":Organization.query.filter(Organization.name == FiveSmallest[2]).one().address,
            "city":Organization.query.filter(Organization.name == FiveSmallest[2]).one().city,
            "zip code":Organization.query.filter(Organization.name == FiveSmallest[2]).one().zip_code}

    o4 = {"name":Organization.query.filter(Organization.name == FiveSmallest[3]).one().name, 
            "description":Organization.query.filter(Organization.name == FiveSmallest[3]).one().text,
            "website":Organization.query.filter(Organization.name == FiveSmallest[3]).one().website,
            "address":Organization.query.filter(Organization.name == FiveSmallest[3]).one().address,
            "city":Organization.query.filter(Organization.name == FiveSmallest[3]).one().city,
            "zip code":Organization.query.filter(Organization.name == FiveSmallest[3]).one().zip_code}

    o5 = {"name":Organization.query.filter(Organization.name == FiveSmallest[4]).one().name, 
            "description":Organization.query.filter(Organization.name == FiveSmallest[4]).one().text,
            "website":Organization.query.filter(Organization.name == FiveSmallest[4]).one().website,
            "address":Organization.query.filter(Organization.name == FiveSmallest[4]).one().address,
            "city":Organization.query.filter(Organization.name == FiveSmallest[4]).one().city,
            "zip code":Organization.query.filter(Organization.name == FiveSmallest[4]).one().zip_code}

    l = {1:o1, 2:o2, 3:o3, 4:o4, 5:o5}


    return json.dumps(l, cls=DecimalEncoder)

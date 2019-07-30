""" This is where input will be taken to form suggestions of most relevant charities """
from heapq import nsmallest
from scipy import spatial
from .models import Organization
import basilica


BASILICA = basilica.Connection('684f0990-8710-309c-2f92-4d2b27b3b8ad')

def find_organizations(user_input):
    e = BASILICA.embed_sentence(user_input)

    distances = {}
    for i in Organization.query.all():
        distances.update({i.name:spatial.distance.cosine(i.embedding, e)})

    ThreeSmallest = nsmallest(5, distances, key = distances.get) 
    return ThreeSmallest

API_KEY = '*********************'
API_SECRET = '********************'

#initialisation
import time
from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

#importing API class
from facepp import API
api = API(API_KEY, API_SECRET)

#assigning image with URL
#not necessary in this program
PERSONS = [
    ('image1', '<URL1>'),
    ('image2', '<URL2>'),
]

#assigning face ids

result = api.detection.detect(url = '<URL1>', mode = 'oneface')
face_idone = result['face'][0]['face_id']
print(face_idone)

result2 = api.detection.detect(url = '<URL2>', mode = 'oneface')
face_idtwo = result2['face'][0]['face_id']
print(face_idtwo)


#computing the similarity
sim = api.recognition.compare(face_id1 = face_idone, face_id2 = face_idtwo)
similarity = sim['similarity']
print(similarity)



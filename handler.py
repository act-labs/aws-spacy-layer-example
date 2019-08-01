import json
import spacy

nlp = spacy.load('/opt/en_core_web_sm-2.1.0')

def nouns(event, context):
    text = event["body"]
    doc = nlp(text)
    nouns = [token.lemma_ for token in doc if  token.pos_ == 'NOUN']

    response = {
        "statusCode": 200,
        "body": json.dumps(nouns)
    }

    return response



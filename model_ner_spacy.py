from pydantic import BaseModel
from pathlib import Path
import spacy
from utils import get_text_from_pracuj_pl

model_dir = Path(r'ner4')
ner_model = spacy.load(model_dir)


class NERspaCyLinkQueryModel(BaseModel):
    text : str

class NERspaCyTextQueryModel(BaseModel):
    text : str

class NERspaCyLinkModel:
    def get_entities(self, URL):
        text = get_text_from_pracuj_pl(URL)
        doc = ner_model(text)
        results = [{'text': ent.text, 'label': ent.label_, 'start_char': ent.start_char, 'end_char': ent.end_char} for ent in doc.ents]
        return {'text': text, 'entities': results}

class NERspaCyTextModel:
    def get_entities(self, text):
        doc = ner_model(text)
        results = [{'text': ent.text, 'label': ent.label_, 'start_char': ent.start_char, 'end_char': ent.end_char} for ent in doc.ents]
        return {'text': text, 'entities': results}

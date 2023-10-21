import spacy

class Searcher:
    def __init__(self, model_name="pt_core_news_lg"):
        self.nlp = spacy.load(model_name)

    def advanced_search(self, query, document, max_paragraphs=50):
        doc = self.nlp(document)
        query_doc = self.nlp(query)

        scores = {}
        for sent in doc.sents:
            scores[sent.text] = query_doc.similarity(sent)

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        extracted_paragraphs = [item[0] for item in sorted_scores][:max_paragraphs]

        return extracted_paragraphs

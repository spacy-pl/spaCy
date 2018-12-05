# coding: utf8
from collections import OrderedDict
from ...pipeline import Tagger


class PolishTagger(Tagger):
    def __init__(self, vocab, model=False, **cfg):
        self.vocab = vocab
        self.model = model
        self.cfg = OrderedDict(sorted(cfg.items()))
        self.cfg.setdefault('cnn_maxout_pieces', 2)

    def __call__(self, doc):
        self.set_annotations([doc], [[1] * len(doc)])
        return doc

# coding: utf8
from __future__ import unicode_literals

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_INFIXES
from .lemmatizer import LEMMA_RULES, LEMMA_INDEX, LEMMA_EXC
from .lemmatizer.lemmatizer import PolishLemmatizer
from .tagger import PolishTagger

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups
from ...symbols import POS, PUNCT


class PolishDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: 'pl'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM], BASE_NORMS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    infixes = tuple(TOKENIZER_INFIXES)
    stop_words = STOP_WORDS
    tag_map = {"*": {POS: PUNCT, "PunctType": "peri"}}

    @classmethod
    def create_lemmatizer(cls, nlp=None):
        lemma_rules = LEMMA_RULES
        lemma_index = LEMMA_INDEX
        lemma_exc = LEMMA_EXC
        return PolishLemmatizer(index=lemma_index, exceptions=lemma_exc,
                                rules=lemma_rules)


class Polish(Language):
    lang = 'pl'
    Defaults = PolishDefaults


__all__ = ['Polish']

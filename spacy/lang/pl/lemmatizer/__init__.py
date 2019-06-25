# coding: utf8
from __future__ import unicode_literals

from ....util import load_resource


ADJECTIVES = load_resource('./', 'adj')
ADVERBS = load_resource('./', 'adv')
NOUNS = load_resource('./', 'noun')
PARTICIPLES = load_resource('./', 'part')
VERBS = load_resource('./', 'verb')
OTHER = load_resource('./', 'other')

ADJECTIVE_RULES = load_resource('./', 'adj_rules')
ADVERB_RULES = load_resource('./', 'adv_rules')
NOUN_RULES = load_resource('./', 'noun_rules')
PARTICIPLE_RULES = load_resource('./', 'part_rules')
VERB_RULES = load_resource('./', 'verb_rules')
# from ._other_rules import OTHER_RULES


LEMMA_INDEX = {'adj': ADJECTIVES, 'adv': ADVERBS, 'noun': NOUNS,
               'part': PARTICIPLES, 'verb': VERBS, 'other': OTHER}

LEMMA_EXC = {}

LEMMA_RULES = {'adj': ADJECTIVE_RULES, 'adv': ADVERB_RULES, 'noun': NOUN_RULES,
               'part': PARTICIPLE_RULES, 'verb': VERB_RULES}

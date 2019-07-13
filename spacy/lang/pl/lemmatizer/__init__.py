# coding: utf8
from __future__ import unicode_literals

from ....util import load_resource


ADJECTIVES = set(load_resource('./', 'adjectives'))
ADVERBS = set(load_resource('./', 'adverbs'))
NOUNS = set(load_resource('./', 'nouns'))
PARTICIPLES = set(load_resource('./', 'pariciples'))
VERBS = set(load_resource('./', 'verbs'))
OTHER = set(load_resource('./', 'other'))

ADJECTIVE_RULES = list(load_resource('./', 'adj_rules'))
ADVERB_RULES = list(load_resource('./', 'adv_rules'))
NOUN_RULES = list(load_resource('./', 'noun_rules'))
PARTICIPLE_RULES = list(load_resource('./', 'part_rules'))
VERB_RULES = list(load_resource('./', 'verb_rules'))


LEMMA_INDEX = {'adj': ADJECTIVES, 'adv': ADVERBS, 'noun': NOUNS,
               'part': PARTICIPLES, 'verb': VERBS, 'other': OTHER}

LEMMA_EXC = {}

LEMMA_RULES = {'adj': ADJECTIVE_RULES, 'adv': ADVERB_RULES, 'noun': NOUN_RULES,
               'part': PARTICIPLE_RULES, 'verb': VERB_RULES}

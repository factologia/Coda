 # -*- coding: utf-8 -*-
import ctypes, os, unittest, time
import tokenizer, disambiguator, common

syntax_parser_lib = common.load_library('syntax-parser')

class SyntaxNode(disambiguator.DisambiguatedData):
    def __init__(self):
        self.index = -1
        self.parent_index = -1

    def get_info_from_morphology(self, disambiguated):
        self.get_info_from_token(disambiguated)
        self.lemma = disambiguated.lemma
        self.label = disambiguated.label
        self.weight = disambiguated.weight
        self.lemma_id = disambiguated.lemma_id

class SyntaxTree(object):
    def __init__(self):
        self.root_index = -1
        self.nodes = []
        self.sentence = u''

class SyntaxParser(object):
    def __init__(self, language):
        syntax_parser_lib.CreateSyntaxParser(language)
        self.language = language

class SyntaxParserTest(unittest.TestCase):
    def test_time_creation(self):
        parser = SyntaxParser("RU")
        start_time = time.time()
        parser = SyntaxParser("RU")
        spent_time = time.time() - start_time
        self.assertLess(spent_time, 1e-3)

if __name__ == '__main__':
    unittest.main()

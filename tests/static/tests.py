import os
import shutil
import monkey.corpus as corpus
import monkey.helpers.cell_helper as cell_helper 
import monkey.helpers.static_helper as static_helper
from glimpse.glab.api import *

class TestStatic():
    
    def setup(self):
        Reset()
        path = "monkey/test_static"
        self.sample_corpus = corpus.Corpus(path, 2)
        SetCorpus(self.sample_corpus.get_corpus())
        ImprintS2Prototypes(5)
        self.sample_prototype = GetPrototype()
        self.sample_cell_helper = cell_helper.CellHelper(path, 5)
        self.sample_static_helper = static_helper.StaticHelper(path, None, 5)
        self.sample_corpus.get_next_images()
       
    def teardown(self):
        try:
            shutil.rmtree("monkey/test_static")
        except Exception:
            pass
    
    def test_cell_helper(self):
        assert not self.sample_cell_helper.imprint() is None

    def test_static_helper(self):
        init_prototype = GetPrototype()
        StoreExperiment("test_experiment")
        prototype, results = self.sample_static_helper.imprint()
        LoadExperiment("test_experiment")
        assert prototype != init_prototype


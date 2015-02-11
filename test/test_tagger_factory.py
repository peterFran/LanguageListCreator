__author__ = 'peter'

from langtools.classify.tagger import TaggerFactory


def test_tagger_creates():
    a = TaggerFactory.factory("cess")
    assert isinstance(a, object)


def test_tagger_fails():
    a = TaggerFactory.factory("cep")
    assert a is None
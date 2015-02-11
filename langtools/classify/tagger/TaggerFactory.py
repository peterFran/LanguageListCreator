__author__ = 'peter'
import pickle
import pkgutil


def factory(name):
    if name == "cess":
        return pickle.loads(pkgutil.get_data('langtools', 'classify/tagger/class.pickle'))
    return None


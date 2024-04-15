import re
import xml.etree.ElementTree as et


class Statements():

    def __init__(self, file_path):
        self.dictionary = {}
        with open(file_path) as f:
            self.root = et.parse(f).getroot()
        stmts = self.root.findall("statement")
        for stmt in stmts:
            self.dictionary[stmt.find("name").text] = stmt.find("value").text

    def get(self, name, param=None):
        stmt = self.dictionary.get(name)
        if type(param) is dict:
            return stmt.format(**param)
        if type(param) is list:
            stmt = re.sub(r'\{[^{}]*}', '{}', stmt)
            return stmt.format(*param)
        return stmt

    def all(self):
        return self.dictionary.keys()

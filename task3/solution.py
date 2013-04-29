class Person:
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        if father:
            self.add_parent(father)
        if mother:
            self.add_parent(mother)
        self.kids = []

    def add_parent(self, parent):
        if parent.gender == 'F':
            self.mother = parent
        else:
            self.father = parent
        parent.kids.append(self)

    def children(self, gender='both'):
        if not gender == 'both':
            return list(filter(lambda person: person.gender == gender,
                               self.kids))
        else:
            return self.kids

    def get_siblings(self, gender):
        if hasattr(self, "mother"):
            if hasattr(self, "father"):
                siblings = list(set(self.mother.children(gender) +
                                    self.father.children(gender)))
            else:
                siblings = self.mother.children(gender)
        elif hasattr(self, "father"):
            siblings = self.father.children(gender)
        else:
            siblings = []

        return list(set(siblings) - {self})

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def is_direct_successor(self, other_person):
        return other_person in self.children()

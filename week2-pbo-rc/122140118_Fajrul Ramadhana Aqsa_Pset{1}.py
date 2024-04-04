import random


class Parent:

    def __init__(self, blood_type):
        self.blood_type = blood_type

    def get_allele(self):
        if self.blood_type == 'A':
            return "A"
        elif self.blood_type == 'B':
            return "B"
        elif self.blood_type == 'O':
            return "O"
        elif self.blood_type == "AA":
            return "A"
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "AO":
            return ["A", "O"]
        elif self.blood_type == "BA":
            return ["B", "A"]
        elif self.blood_type == "BB":
            return "B"
        elif self.blood_type == "BO":
            return ["B", "O"]
        elif self.blood_type == "OA":
            return ["O", "A"]
        elif self.blood_type == "OB":
            return ["O", "B"]
        elif self.blood_type == "OO":
            return ["O", "O"]


class Child:

    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.allele = []

    def get_allele(self):
        allele_father = self.father.get_allele()
        allele_mother = self.mother.get_allele()

        self.allele.append(random.choice(allele_father))
        self.allele.append(random.choice(allele_mother))
        return "".join(self.allele)

    def get_blood_type(self):
        allele = self.get_allele()
        if allele == "AA":
            return "A"
        elif allele == "AB" or allele == "BA":
            return "AB"
        elif allele == "BB":
            return "B"
        elif allele == "OO":
            return "O"
        elif "O" in allele and ("A" in allele or "B" in allele):
            return "A" if "A" in allele else "B"
        else:
            return "Invalid blood type"


father_blood = input("Enter the father's allele: ").upper()
mother_blood = input("Enter the mother's allele: ").upper()

father = Parent(father_blood)
mother = Parent(mother_blood)

child = Child(father, mother)

print(f"Child's allele: {child.get_allele()}")
print(f"Child's blood type: {child.get_blood_type()}")

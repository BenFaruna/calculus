from decimal import Decimal

superscript = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


class Term:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def __repr__(self):
        if type(self.coefficient) == float:
            numerator, denominator  = Decimal(self.coefficient).as_integer_ratio()
            return f"{numerator}/{denominator}x" + f"{self.power}".translate(superscript)
        return f"{self.coefficient}x" + f"{self.power}".translate(superscript)

    def __add__(self, other):
        if self.power == other.power:
            new_coefficient = self.coefficient + other.coefficient

            return Term(new_coefficient, self.power)
        else:
            return self, other

    def __sub__(self, other):
        if self.power == other.power:
            new_coefficient = self.coefficient - other.coefficient

            return Term(new_coefficient, self.power)
        else:
            return self, other

    def __mul__(self, other):
        new_coefficient = self.coefficient * other.coefficient
        new_power = self.power + other.power

        return Term(new_coefficient, new_power)

    def __divmod__(self, other):
        new_coefficient = self.coefficient / other.coefficient
        new_power = self.power - other.power

        return Term(new_coefficient, new_power)


class Equation:
    def __init__(self):
        self.equation = []

    def __repr__(self):
        equation = ""
        for term in self.equation:
            if term.coefficient < 0:
                equation += f"{term.coefficient}x" + f"{term.power}".translate(superscript)
            else:
                equation += f"+{term.coefficient}x" + f"{term.power}".translate(superscript)

        return equation

    def add_term(self, term):
        self.equation.append(term)


# term1 = Term(-5, 10)
# term2 = Term(10, 3)
# term3 = Term(10, 10)
# term4 = Term(-20, 3)
#
# new_term = term2 + term1
# print(new_term)
#
# print(term1, term3)
# new_term2 = term1 + term3
# print(new_term2)
#
# new_term3 = term1 - term3
# print(new_term3)
#
# print(term2, term4)
# new_term4 = term2 + term4
# print(new_term4)
#
# new_term4 = term2 - term4
# print(new_term4)
#
# new_term5 = term4 - term2
# print(new_term5)

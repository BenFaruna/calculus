superscript = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


class Term:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def __repr__(self):
        if type(self.coefficient) == float:
            numerator, denominator = self.coefficient.as_integer_ratio()
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

    def derivative(self):
        new_coefficient = self.power * self.coefficient
        new_power = self.power - 1
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

        return "y = " + equation

    def add_term(self, new_term):
        index = 0
        for term in self.equation:
            if term.power == new_term.power:
                self.equation[index] = term + new_term
                return

            index += 1

        self.equation.append(new_term)

    def derivative(self):
        result = Equation()
        for term in self.equation:
            result.equation.append(term.derivative())

        return result

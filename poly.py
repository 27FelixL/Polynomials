"""
Student information for this assignment:

On my honor, Felix Li, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: fl7449
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """Class for the assignment"""
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """Insert"""
        if coeff == 0:  # Ignore zero coefficient terms
            return
        new_node = Node(coeff, exp)
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
            return
        prev, current = None, self.head
        while current and current.exp > exp:
            prev, current = current, current.next
        if current and current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0:  # Remove zero coefficient terms
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            return
        new_node.next = current
        if prev:
            prev.next = new_node
        else:
            self.head = new_node

    def add(self, p):
        """adding"""
        result = LinkedList()
        t1, t2 = self.head, p.head
        while t1 or t2:
            if t1 and (not t2 or t1.exp > t2.exp):
                result.insert_term(t1.coeff, t1.exp)
                t1 = t1.next
            elif t2 and (not t1 or t2.exp > t1.exp):
                result.insert_term(t2.coeff, t2.exp)
                t2 = t2.next
            else:
                result.insert_term(t1.coeff + t2.coeff, t1.exp)
                t1, t2 = t1.next, t2.next
        return result

    def mult(self, p):
        """Multiplying"""
        result = LinkedList()
        t1 = self.head
        temp_dict = {}
        while t1:
            t2 = p.head
            while t2:
                new_exp = t1.exp + t2.exp
                new_coeff = t1.coeff * t2.coeff
                if new_exp in temp_dict:
                    temp_dict[new_exp] += new_coeff
                else:
                    temp_dict[new_exp] = new_coeff
                t2 = t2.next
            t1 = t1.next
        for exp in sorted(temp_dict.keys(), reverse=True):
            result.insert_term(temp_dict[exp], exp)
        return result

    def __str__(self):
        """String return"""
        if not self.head:
            return ""
        terms = []
        current = self.head
        while current:
            terms.append(f"({current.coeff}, {current.exp})")
            current = current.next
        return " + ".join(terms)


def main():
    """Main"""
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product

if __name__ == "__main__":
    main()

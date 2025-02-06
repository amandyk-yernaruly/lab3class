# Task 1
class A:
    def init(self):
        self.a = ""
    
    def b(self):
        self.a = input("Enter a string: ")
    
    def c(self):
        print(self.a.upper())

# Task 2
class D:
    def e(self):
        return 0

class F(D):
    def init(self, a):
        self.a = a
    
    def e(self):
        return self.a ** 2

# Task 3
class G(D):
    def init(self, a, b):
        self.a = a
        self.b = b
    
    def e(self):
        return self.a * self.b

# Task 4
import math
class H:
    def init(self, a, b):
        self.a = a
        self.b = b
    
    def i(self):
        print(f"Point({self.a}, {self.b})")
    
    def j(self, c, d):
        self.a = c
        self.b = d
    
    def k(self, l):
        return math.sqrt((self.a - l.a)**2 + (self.b - l.b)**2)

# Task 5
class M:
    def init(self, a, b=0):
        self.a = a
        self.b = b
    
    def n(self, c):
        self.b += c
        print(f"Deposited {c}. New balance: {self.b}")
    
    def o(self, c):
        if c > self.b:
            print("Insufficient funds!")
        else:
            self.b -= c
            print(f"Withdrawn {c}. New balance: {self.b}")

# Task 6
p = list(range(1, 21))
q = lambda a: a > 1 and all(a % b != 0 for b in range(2, int(math.sqrt(a)) + 1))
r = list(filter(q, p))
print("Prime numbers:", r)
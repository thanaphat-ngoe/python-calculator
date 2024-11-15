class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if (b < 0):
            for i in range(-b):
                result = self.add(result, -a)

        for i in range(b):
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0

        if (a == 0):
            return result
        
        if (a < 0 and b < 0):
            a = -a
            b = -b

        if (a < 0):
            b = -b
            while True:
                result += 1
                if(self.multiply(result, b) == a):
                    result = self.multiply(result, -1)
                    return result
                
        if (b < 0):
            a = -a
            while True:
                result += 1
                if(self.multiply(result, b) == a):
                    result = self.multiply(result, -1)
                    return result
        
        while True:
            result += 1
            if(self.multiply(result, b) == a):
                break
        
        return result
    
    def modulo(self, a, b):
        negResult = (a < 0) ^ (b < 0)
        if (a < 0):
            a = -a
        if (b < 0):
            b = -b
        while a >= b:
            a = a-b
        if (negResult):
            return -a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
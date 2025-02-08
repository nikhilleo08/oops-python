from abc import ABC, abstractmethod

# Step 1: Define the Expression Interface
class Expression(ABC):
    """Abstract Expression Interface"""
    
    @abstractmethod
    def interpret(self):
        pass


# Step 2: Define Terminal Expression (Numbers)
class NumberExpression(Expression):
    """Terminal Expression: Represents numbers"""
    
    def __init__(self, number):
        self.number = number
    
    def interpret(self):
        return self.number


# Step 3: Define Non-Terminal Expressions (Operators)
class AddExpression(Expression):
    """Non-Terminal Expression: Represents addition"""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class SubtractExpression(Expression):
    """Non-Terminal Expression: Represents subtraction"""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class MultiplyExpression(Expression):
    """Non-Terminal Expression: Represents multiplication"""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


# Step 4: Client Code
if __name__ == "__main__":
    # (5 + 3) - (10 - 2)
    expression = SubtractExpression(
        AddExpression(NumberExpression(15), NumberExpression(3)),
        SubtractExpression(NumberExpression(10), NumberExpression(2))
    )

    print(f"Result: {expression.interpret()}")  # Output: 6

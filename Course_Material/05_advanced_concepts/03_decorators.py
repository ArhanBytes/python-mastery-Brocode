"""
Topic: Docarators
Section: Advanced Concept
Description:
- Decorator =   A function that extends the behavior of another function
                w/o modifying the base function
                Pass the base function as an argument to the decorator
"""

# decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs): # i create this wrapper so when i apply decorators this add_sprinles function will cal but since our main content is inside the wrapper so the main content won't be shown but it return in a function
        print("You add Sprinkles .....")
        func(*args, **kwargs)
    return wrapper

# decorator
def add_fudge(func):
    def wrapper(*args, **kwargs): # args and kwargs always pass this if your base function has arguments
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour): # base function
    print(f"Here is your {flavour} ice cream :).")
    
get_ice_cream("chocolato")
"""
Topic: Keyword Arguments
Section: Function
Description:
keyword arguments = an argument preceded by an identifier
                    helps with readability
                    order of arguments doesn't matter
                    1. positional 2. default 3. KEYWORD 4. arbitrary
"""

# ------ GREETING FUNCTION ------
def hello(greeting, title, first, last):
    print(f"{greeting}! {title}{first} {last}")

hello("Hello", title="Mr.", last="Imran", first="Arhan")

# keyword argument -> write the same parameter variable as a prefix followed by = to the corresponding argument
# positional arguemnt should comes first otherwise there will be error

# ------ PRINTING NUMBERS FUNCTION ------
for x in range(1, 11):
    print(x, end=" ") # end is an keyword argument of print function

# --- sepratae argument in print function ------
print("1", "2","3", "4", "5", "6", sep="-")

# alot of built-in function has keyword argument yuo can use


# ---------- EXERCISE 01: GENERATE A PHONE NUMBER FUNCTION ----------
# country code | area code | first 3 digit | last 2 digit

def get_phone_num(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num = get_phone_num(country_code=5, area_code=123, first_digits=453, last_digits=9421)
print(f"Phone Number: {phone_num}")
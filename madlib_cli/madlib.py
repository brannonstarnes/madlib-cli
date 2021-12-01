import re 

welcome = "Welcome to Python Madlibs"
instructions = "Enter words, get laughs."
stormy_template = 'assets/dark_and_stormy_night_template.txt'

def show_instructions():
    print(instructions)

def welcome_user():
    print(welcome)

def read_template(template):
    
    try:
        with open(template, 'r') as file:
            content = file.read()
            parse_template(content)
            return content
    except:
        raise FileNotFoundError("Invalid File Path/File Not Found")
    pass

def parse_template(template_string):
    bracketed_words = re.findall(r"{(.*?)}", template_string)
    stripped = re.sub(r"{(.*?)}", "{}", template_string)
    return stripped , tuple(bracketed_words)

    pass

def merge(empty_template, user_words):
    complete_lib = empty_template.format(*user_words)
    return complete_lib
    pass

# Call functions
welcome_user()
show_instructions()
read_template(stormy_template)
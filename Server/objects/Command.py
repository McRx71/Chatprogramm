class Command:
    def __init__(self, name, syntax, arguments, description):
        self.name = str(name).lower()
        self.syntax = syntax
        self.arguments = arguments
        self.description = description
class Foo:
    def __init__(self):
        print("Hello word from foo")

class Bar(Foo):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return 5

    def __my_new_special_method__(self):
        """
        Never create methods like this. (__method_name__)
        This format belongs to special methods and the name you gave
        can be used in the feature python versions
        """
        pass

my_var = Bar()

# Bad!
print(my_var.__len__())

# Good!
print(len(my_var))

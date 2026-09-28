def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

    def safe_number(text):
        try:
            return int(text)
        except ValueError:
            return "Not a valid number"

        def get_filed(learner, key):
            try:
                return learner[key]
            except KeyError:
                return "field not found"

            # Testing the functions
            print(safe_divide(10, 2))
            print(safe_divide(10, 0))
            print(safe_number("42"))
            print(safe_number("abc"))
            learner = {"name": "kubi", "score": 82}
            print(get_field(learner, ""))
            print(get_field(learner, "email"))
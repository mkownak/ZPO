import re

class Form:
    def __init__(self, email: str, username: str, age: int) -> None:
        self.email = email
        self.username = username
        self.age = age


def formvalidator(func):
    def wrapper(form: Form):
        errors = []

        if not re.match(r"[^@]+@[^@]+\.[^@]+", form.email):
            errors.append("Nieprawidłowy email")

        if not form.username.strip():
            errors.append("Nazwa użytkownika nie może być pusta")

        if not isinstance(form.age, int) or form.age <= 0:
            errors.append("Wiek musi być liczbą większą niż 0")

        if errors:
            return f"Błędy w formularzu: {', '.join(errors)}"

        return func(form)
    return wrapper


@formvalidator
def submit_form(form: Form):
    return "Formularz przeszedł walidację pomyślnie"

form1 = Form("kownak@gmail.com", "cognac", 23)

form2 = Form("majl", "eniu", 1)

print(submit_form(form1))
print(submit_form(form2))

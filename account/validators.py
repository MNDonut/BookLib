from django.core.exceptions import ValidationError

# password should contain at least 1 letter and 1 digit

class CustomTooCommonPasswordValidator():
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password) or \
            not any(char.isalpha() for char in password):
            raise ValidationError('Пароль повинен містити літери та цифри')
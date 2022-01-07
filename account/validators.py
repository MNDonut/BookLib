from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
from difflib import SequenceMatcher
from django.core.exceptions import FieldDoesNotExist
import re

# password should contain at least 1 letter and 1 digit
class CustomTooCommonPasswordValidator():
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password) or \
            not any(char.isalpha() for char in password):
            raise ValidationError('Пароль повинен містити літери та цифри')


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
            if not user:
                return

            for attribute_name in self.user_attributes:
                value = getattr(user, attribute_name, None)
                if not value or not isinstance(value, str):
                    continue
                value_parts = re.split(r'\W+', value) + [value]
                for value_part in value_parts:
                    if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                        try:
                            verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                        except FieldDoesNotExist:
                            verbose_name = attribute_name
                        raise ValidationError(
                            "Пароль занадто схожий до %(verbose_name)s",
                            code='password_too_similar',
                            params={'verbose_name': verbose_name.lower()},
                        )
from django.db import models

class DropdownField(models.Field):
    "Implements lists of options for use in dropdown menus"

    def __init__(self, options=[], *args, **kwargs):
        str_options = ""

        for option in options:
            if len(str_options) > 0:
                str_options += ','
            str_options += str(option)

        self.options = str_options

        super.__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwarg if it's not the default
        if self.options != "":
            kwargs['options'] = self.options.split(',')
        return name, path, args, kwargs

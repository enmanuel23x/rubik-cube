class Row:
    def __init__(self, color):
        self.first_color = color
        self._middle_color = color
        self.last_color = color

    def __str__(self):
        row = str(self.first_color.value) + " | " + \
            str(self.middle_color.value) + " | " + str(self.last_color.value)
        return row

    def __eq__(self, row):
        self.first_color = row.first_color
        self._middle_color = row.middle_color
        self.last_color = row.last_color

    def __iter__(self):
        yield self.first_color
        yield self._middle_color
        yield self.last_color

    @property
    def middle_color(self):
        return self._middle_color

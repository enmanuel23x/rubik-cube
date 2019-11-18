from Row import Row


class Face(object):
    def __init__(self, main_color):
        self._main_color = main_color
        self.first_row = Row(main_color)
        self._middle_row = Row(main_color)
        self.last_row = Row(main_color)

    def __eq__(self, face):
        self.first_row = face.first_row
        self._middle_row = face.middle_row
        self.last_row = face.last_row

    def __str__(self):
        face = str(self.first_row) + "\n" + \
            str(self.middle_row) + "\n" + str(self.last_row)
        return face

    def __iter__(self):
        yield self.first_row
        yield self._middle_row
        yield self.last_row

    @property
    def main_color(self):
        return self._main_color

    @property
    def middle_row(self):
        return self._middle_row

    @property
    def first_column(self):
        column = Row(self._middle_row.first_color)
        column.first_color = self.first_row.first_color
        column.last_color = self.last_row.first_color
        return column

    @first_column.setter
    def first_column(self, column):
        self.first_row.first_color = column.first_color
        self._middle_row.first_color = column.middle_color
        self.last_row.first_color = column.last_color

    @property
    def middle_column(self):
        column = Row(self._middle_row.middle_color)
        column.first_color = self.first_row.middle_color
        column.last_color = self.last_row.middle_color
        return column

    @property
    def last_column(self):
        column = Row(self._middle_row.last_color)
        column.first_color = self.first_row.last_color
        column.last_color = self.last_row.last_color
        return column

    @last_column.setter
    def last_column(self, column):
        self.first_row.last_color = column.first_color
        self._middle_row.last_color = column.middle_color
        self.last_row.last_color = column.last_color

    def rotate_clockwise(self):
        first_column = self.first_column
        middle_column = self.middle_column
        last_column = self.last_column
        self.first_row = first_column
        self._middle_row = middle_column
        self.last_row = last_column

    def rotate_counter_clockwise(self):
        first_column = self.first_column
        middle_column = self.middle_column
        last_column = self.last_column
        self.first_row = last_column
        self._middle_row = middle_column
        self.last_row = first_column

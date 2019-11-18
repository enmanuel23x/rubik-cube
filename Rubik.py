from Color import Color
from Row import Row
from Face import Face


class Rubik:
    def __init__(self):
        self.front_face = Face(Color.red)
        self.back_face = Face(Color.orange)
        self.left_face = Face(Color.green)
        self.right_face = Face(Color.blue)
        self.top_face = Face(Color.white)
        self.bottom_face = Face(Color.yellow)

    def __str__(self):
        rubik = "Front face:\n" + str(self.front_face) + "\n\n"
        rubik += "Back face:\n" + str(self.back_face) + "\n\n"
        rubik += "Left face:\n" + str(self.left_face) + "\n\n"
        rubik += "Right face:\n" + str(self.right_face) + "\n\n"
        rubik += "Top face:\n" + str(self.top_face) + "\n\n"
        rubik += "Bottom face:\n" + str(self.bottom_face) + "\n\n"
        return rubik

    def rotate_cube_clockwise(self):
        temp = self.top_face
        self.top_face = self.left_face
        self.left_face = self.bottom_face
        self.bottom_face = self.right_face
        self.right_face = temp
        self.front_face.rotate_clockwise()
        self.back_face.rotate_counter_clockwise()

    def rotate_cube_counter_clockwise(self):
        temp = self.top_face
        self.top_face = self.right_face
        self.right_face = self.bottom_face
        self.bottom_face = self.left_face
        self.left_face = temp
        self.front_face.rotate_counter_clockwise()
        self.back_face.rotate_clockwise()

    def rotate_cube_upward(self):
        temp = self.top_face
        self.top_face = self.front_face
        self.front_face = self.bottom_face
        self.bottom_face = self.back_face
        self.back_face = temp
        self.right_face.rotate_clockwise()
        self.left_face.rotate_counter_clockwise()

    def rotate_cube_downward(self):
        temp = self.top_face
        self.top_face = self.back_face
        self.back_face = self.bottom_face
        self.bottom_face = self.front_face
        self.front_face = temp
        self.right_face.rotate_counter_clockwise()
        self.left_face.rotate_clockwise()

    def rotate_cube_right(self):
        temp = self.front_face
        self.front_face = self.left_face
        self.left_face = self.back_face
        self.back_face = self.right_face
        self.right_face = temp
        self.top_face.rotate_counter_clockwise()
        self.bottom_face.rotate_clockwise()

    def rotate_cube_left(self):
        temp = self.front_face
        self.front_face = self.right_face
        self.right_face = self.back_face
        self.back_face = self.left_face
        self.left_face = temp
        self.top_face.rotate_clockwise()
        self.bottom_face.rotate_counter_clockwise()

    def rotate_front_face_clockwise(self):
        self.front_face.rotate_clockwise()
        temp = self.right_face.first_column
        self.right_face.first_column = self.top_face.last_row
        self.top_face.last_row = self.left_face.last_column
        self.left_face.last_column = self.bottom_face.first_row
        self.bottom_face.first_row = temp

    def rotate_front_face_counter_clockwise(self):
        self.front_face.rotate_counter_clockwise()
        temp = self.right_face.first_column
        self.right_face.first_column = self.bottom_face.first_row
        self.bottom_face.first_row = self.left_face.last_column
        self.left_face.last_column = self.top_face.last_row
        self.top_face.last_row = temp

    def rotate_right_face_upward(self):
        temp = self.front_face.last_column
        self.front_face.last_column = self.bottom_face.last_column
        self.bottom_face.last_column = self.back_face.last_column
        self.back_face.last_column = self.top_face.last_column
        self.top_face.last_column = temp
        self.right_face.rotate_clockwise()

    def rotate_right_face_downward(self):
        temp = self.front_face.last_column
        self.front_face.last_column = self.top_face.last_column
        self.top_face.last_column = self.back_face.last_column
        self.back_face.last_column = self.bottom_face.last_column
        self.bottom_face.last_column = temp
        self.right_face.rotate_counter_clockwise()

    def rotate_left_face_upward(self):
        temp = self.front_face.first_column
        self.front_face.first_column = self.bottom_face.first_column
        self.bottom_face.first_column = self.back_face.first_column
        self.back_face.first_column = self.top_face.first_column
        self.top_face.first_column = temp
        self.left_face.rotate_counter_clockwise()

    def rotate_left_face_downward(self):
        temp = self.front_face.first_column
        self.front_face.first_column = self.top_face.first_column
        self.top_face.first_column = self.back_face.first_column
        self.back_face.first_column = self.bottom_face.first_column
        self.bottom_face.first_column = temp
        self.left_face.rotate_clockwise()

    def rotate_top_face_left(self):
        temp = self.front_face.first_row
        self.front_face.first_row = self.right_face.first_row
        self.right_face.first_row = self.back_face.first_row
        self.back_face.first_row = self.left_face.first_row
        self.left_face.first_row = temp
        self.top_face.rotate_clockwise()

    def rotate_top_face_right(self):
        temp = self.front_face.first_row
        self.front_face.first_row = self.left_face.first_row
        self.left_face.first_row = self.back_face.first_row
        self.back_face.first_row = self.right_face.first_row
        self.right_face.first_row = temp
        self.top_face.rotate_counter_clockwise()

    def rotate_bottom_face_left(self):
        temp = self.front_face.last_row
        self.front_face.last_row = self.right_face.last_row
        self.right_face.last_row = self.back_face.last_row
        self.back_face.last_row = self.left_face.last_row
        self.left_face.last_row = temp
        self.bottom_face.rotate_counter_clockwise()

    def rotate_bottom_face_right(self):
        temp = self.front_face.last_row
        self.front_face.last_row = self.left_face.last_row
        self.left_face.last_row = self.back_face.last_row
        self.back_face.last_row = self.right_face.last_row
        self.right_face.last_row = temp
        self.bottom_face.rotate_clockwise()

    def shuffle_cube(self, amount_of_rotations=100):
        pass


def main():
    rubik = Rubik()
    print(rubik)

    print("Rotate cube clockwise\n")
    rubik.rotate_cube_clockwise()
    print(rubik)

    print("Rotate cube counter clockwise\n")
    rubik.rotate_cube_counter_clockwise()
    print(rubik)

    print("Rotate cube upward\n")
    rubik.rotate_cube_upward()
    print(rubik)

    print("Rotate cube downward\n")
    rubik.rotate_cube_downward()
    print(rubik)

    print("Rotate cube right\n")
    rubik.rotate_cube_right()
    print(rubik)

    print("Rotate cube left\n")
    rubik.rotate_cube_left()
    print(rubik)

    print("Rotate front face clockwise\n")
    rubik.rotate_front_face_clockwise()
    print(rubik)

    print("Rotate front face couter clockwise\n")
    rubik.rotate_front_face_counter_clockwise()
    print(rubik)

    print("Rotate front face counter clockwise\n")
    rubik.rotate_front_face_counter_clockwise()
    print(rubik)

    print("Rotate front face clockwise\n")
    rubik.rotate_front_face_clockwise()
    print(rubik)


if __name__ == '__main__':
    main()

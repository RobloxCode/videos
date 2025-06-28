from manim import *

class VariableAssignmentExampleUsage(Scene):
    def construct(self):
        box = Rectangle(width=2, height=1)
        self.play(Create(box))
        self.wait(2)
        var_name = Text("age").next_to(box, UP)
        self.play(Write(var_name))
        self.wait(3)
        number = Text("19").next_to(box, RIGHT, buff=1)
        self.play(Write(number))
        self.wait(2)
        self.play(number.animate.move_to(box.get_center()), run_time=1.5)

class VariableVideo(Scene):
    def scaleAndShrink(self, mobject, scale, run_time):
        self.play(mobject.animate.scale(scale), run_time=run_time)
        self.play(mobject.animate.scale(1 / scale), run_time=run_time)
        self.wait(1)
    
    def changeColorAndShrink(self, mobject, original_color, new_color, scale, run_time):
        mobject.set_color(new_color)
        self.scaleAndShrink(mobject, scale=scale, run_time=run_time)
        mobject.set_color(original_color)

    def variableAssigment(self, mobject_to_transform, name, value, time_to_fadeout):
        box = Rectangle(width=2, height=1)
        self.play(Transform(mobject_to_transform, box))
        self.add(box)
        var_name = Text(name).next_to(box, UP)
        self.play(Write(var_name))
        number = Text(value).next_to(box, RIGHT, buff=1)
        self.play(Write(number))
        self.play(number.animate.move_to(box.get_center()), run_time=1)
        self.wait(time_to_fadeout)
        self.play(FadeOut(var_name))
        self.play(FadeOut(number))
        self.play(FadeOut(box))
    
    def appearAndScale(self, mobject, scale, run_time):
        self.add(mobject)
        self.scaleAndShrink(mobject=mobject, scale=scale, run_time=run_time)

    def construct(self):
        self.wait(1.5)
        # display text
        var_definition = Text("variables in programming languages are containers\nof data values in the program's memmory", font_size=30)
        self.play(Write(var_definition))
        self.wait(4)
        self.play(FadeOut(var_definition))
        self.wait(1)

        rectange = Rectangle(WHITE, 1.5, 4)
        self.play(Create(rectange))
        self.wait(0.3)

        var_name = Text("name").next_to(rectange, UP)
        self.play(Write(var_name))
        self.wait(1)

        var_value = Text("some value").next_to(rectange, RIGHT*1.5)
        self.play(Write(var_value))
        self.wait(1)

        self.play(var_value.animate.move_to(rectange.get_center()))

        self.play(FadeOut(rectange))
        self.play(FadeOut(var_name))
        self.play(FadeOut(var_value))
        self.wait(3)

        # creating variable
        var_name.move_to(ORIGIN).shift(LEFT*2)
        assignmnet = Text("=").next_to(var_name, RIGHT*2)
        var_value.move_to(ORIGIN).shift(RIGHT*1.7)
        var_value.shift(UP*0.1)
        self.appearAndScale(var_name, 1.2, 0.3)
        self.wait(1)
        self.appearAndScale(assignmnet, 1.2, 0.3)
        self.wait(1)
        self.appearAndScale(var_value, 1.2, 0.3)
        self.play(FadeOut(var_name, run_time=0.7))
        self.play(FadeOut(assignmnet, run_time=0.7))
        self.play(FadeOut(var_value, run_time=0.7))
        self.wait(1)

        # examples
        example1_name = Text("age").shift(LEFT*2)
        assignmnet_ex1 = Text("=").next_to(example1_name, RIGHT*2)
        example1_value = Text("25").next_to(assignmnet_ex1, RIGHT*2)
        self.play(Write(example1_name))
        self.play(Write(assignmnet_ex1))
        self.play(Write(example1_value))
        self.wait(1)

        self.changeColorAndShrink(assignmnet_ex1, WHITE, BLUE, 1.2, 0.3)
        self.changeColorAndShrink(example1_value, WHITE, BLUE, 1.2, 0.5)
        self.changeColorAndShrink(example1_name, WHITE, BLUE, 1.2, 0.6)
        self.wait(1)
        self.play(FadeOut(example1_value))
        self.play(FadeOut(assignmnet_ex1))
        self.variableAssigment(example1_name, "age", "25", 1)
        self.play(FadeOut(example1_name))
        self.wait(4)

        data_type_definition = Text("A datatype tells the computer\n what kind of data you're using", font_size=30)
        self.play(Write(data_type_definition))
        self.wait(2)
        self.play(FadeOut(data_type_definition))
        self.wait(2)

        #example of datatypes
        int_example = Text("45")
        float_example = Text("3.99").next_to(int_example, UP*2.5)
        string_example = Text('"SUBSCRIBE"').next_to(int_example, DOWN*2)
        bool_example = Text("True/False").next_to(int_example, RIGHT*3)

        float_example.shift(LEFT*2)
        string_example.shift(LEFT*4)
        bool_example.shift(DOWN*1.4)

        self.wait(2)
        self.play(Write(int_example))
        self.play(Write(float_example))
        self.play(Write(string_example))
        self.play(Write(bool_example))

        self.wait(2)
        self.play(FadeOut(int_example, run_time=0.7))
        self.play(FadeOut(float_example, run_time=0.7))
        self.play(FadeOut(string_example, run_time=0.7))
        self.play(FadeOut(bool_example, run_time=0.7))
        self.wait(1)

        text = Text("More examples:").shift(UP*3)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))
        self.wait(3)

        print_txt = Text("print")
        print_txt.shift(LEFT*3)
        open_parenthesis = Text("(").next_to(print_txt, RIGHT*1.5)
        closing_parenthesis = Text(")").next_to(open_parenthesis, RIGHT*22)
        var_name_txt = Text("varaible_name").next_to(open_parenthesis, RIGHT*2)

        self.play(Write(print_txt))
        self.wait(1)
        self.play(Write(open_parenthesis))
        self.play(Write(closing_parenthesis))
        self.wait(1)
        self.play(Write(var_name_txt))
        self.wait(2)

        self.play(FadeOut(closing_parenthesis, run_time=0.7))
        self.play(FadeOut(var_name_txt, run_time=0.7))
        self.play(FadeOut(open_parenthesis, run_time=0.7))
        self.play(FadeOut(print_txt, run_time=0.7))
        self.wait(4)

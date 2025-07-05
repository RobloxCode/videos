from manim import *

# in this scene we only show one iteration as example explained
class ForLoopExplanation(Scene):
    def scale_and_color_text(self, mobj: Mobject, scale_factor=1.5, new_color=BLUE, duration=0.5):
        self.play(
            mobj.animate.scale(scale_factor).set_color(new_color),
            run_time=duration
        )
        self.play(
            mobj.animate.scale(1/scale_factor).set_color(WHITE),
            run_time=duration
        )

    def construct(self):
        line1For = Text("for", 
            font="Courier new",
            font_size=30
        ).shift(LEFT*2.2)
        line1Openp = Text("(", 
            font="Courier new",
            font_size=30
        ).next_to(line1For, RIGHT).shift(LEFT*0.17)
        line1Index= Text("int i = 0;", 
            font="Courier new",
            font_size=30
        ).next_to(line1Openp, RIGHT)
        line1Condition = Text("i <= 5;", 
            font="Courier new",
            font_size=30
        ).next_to(line1Index, RIGHT).shift(RIGHT*0.2)
        line1Increment = Text("i++", 
            font="Courier new",
            font_size=30
        ).next_to(line1Condition, RIGHT).shift(RIGHT*.2)
        line1CloseP = Text(")", 
            font="Courier new",
            font_size=30
        ).next_to(line1Increment, RIGHT)
        line1OpenBrace = Text("{", 
            font="Courier new",
            font_size=30
        ).next_to(line1CloseP, RIGHT)
        #    0   1      2         3     4   5  6
        # [ for, (, int i = 0, i <= 5, i++, ) ,{ ]
        line1 = VGroup(
            line1For,
            line1Openp,
            line1Index,
            line1Condition,
            line1Increment,
            line1CloseP,
            line1OpenBrace
        )
        line2 = Text('printf("%d ", i);', 
            font="Courier new",
            font_size=30
        )
        line3 = Text("}", 
            font="Courier new",
            font_size=30
        )
        line4 = Text("// rest of the code", 
            font="Courier new",
            font_size=30
        )        
        rectRed = Rectangle(
            height=0.5,
            width=2,
            fill_color=RED,
            fill_opacity=0.4,
            stroke_opacity=0
        ).shift(UP*0.6).shift(RIGHT*1.1)
        rectGreen = Rectangle(
            height=0.5,
            width=2,
            fill_color=GREEN,
            fill_opacity=0.4,
            stroke_opacity=0
        ).shift(UP*0.6).shift(RIGHT*1.1)

        line1.next_to(line2, UP)
        line3.next_to(line2, DOWN)
        line4.next_to(line3, DOWN)

        line2.shift(LEFT*0.7)
        line3.shift(LEFT*3.4)
        line4.shift(LEFT*1.18)

        forLoopGroup = VGroup(
            line1,
            line2,
            line3,
            line4
        )

        # display line 1
        for subLn in line1:
            self.play(Write(subLn), run_time=1.5)
        
        # display the rest of the for loop
        for line in forLoopGroup[1::]:
            self.play(Write(line), run_time=1.5)
        self.wait(10)

        self.scale_and_color_text(line1[3], 1.2)
        self.wait(1)
        self.scale_and_color_text(line1[2], 1.18)
        self.wait(2)
        self.scale_and_color_text(line1[4], 1.2)
        self.wait(2)

        self.play(Create(rectRed))
        self.wait(2)

        self.play(FadeOut(rectRed))
        self.wait(2)
        self.play(Create(rectGreen))
        self.scale_and_color_text(forLoopGroup[1], 1.1)
        self.play(FadeOut(rectGreen))


# this will be a full example
class ForLoop(Scene):
    def moveCurLineExecuting(self, curLineExecuting, direction, lines=1):
        if lines == 1:
            self.play(curLineExecuting.animate.shift(direction*0.58), run_time=0.5)
        else:
            self.play(curLineExecuting.animate.shift(direction*0.58*lines), run_time=0.5)

    def updateConsoleOutput(self, consoleTxt, curOutput, newOutpu):
        self.play(Transform(curOutput, Text(f"{newOutpu}", font="Courier new", font_size=30).next_to(consoleTxt, DOWN)))

    def updateCurCondition(self, curCondition, valueOfIVGroup, iVal):
        self.play(
            Transform(
                curCondition, 
                Text(
                    f"current condition:\n      {iVal} <= 5", 
                    font="Courier new", 
                    font_size=30
                ).next_to(valueOfIVGroup, DOWN*1.5)
            )
        )

    def ScaleUpAndDown(self, text_mobject, scale_factor=1.2, duration=0.5):
        original_scale = text_mobject.get_scale()
        
        self.play(
            text_mobject.animate.scale(scale_factor),
            run_time=duration
        )
        self.play(
            text_mobject.animate.scale(1 / scale_factor),
            run_time=duration
        )

    
    def updateIValue(self, curIVal, iVar, newVal):
        self.play(Transform(curIVal, Text(f"{newVal}", font="Courier new").next_to(iVar, RIGHT)))

    def construct(self):
        line1 = Text("for(int i = 0; i <= 5; i++){", 
            font="Courier new",
            font_size=30
        )
        line2 = Text('printf("%d ", i);', 
            font="Courier new",
            font_size=30
        )
        line3 = Text("}", 
            font="Courier new",
            font_size=30
        )
        line4 = Text("// rest of the code", 
            font="Courier new",
            font_size=30
        )
        valueOfIBox = Rectangle(stroke_width=1.2)
        valueTxt = Text("values of i", font="Courier new", font_size=30).next_to(valueOfIBox, UP)
        iVar = Text("i=", font="Courier new").shift(LEFT*0.2)
        iValue = Text("0", font="Courier new").next_to(iVar, RIGHT)
        valueOfIVGroup = VGroup(
            valueTxt,
            valueOfIBox,
            iValue,
            iVar
        ).to_edge(RIGHT)
        curLineExecuting = Rectangle(
            height=0.4, 
            width=7.5,
            fill_color=GRAY,
            fill_opacity=0.5,
            stroke_color=GRAY,
            stroke_opacity=0
        ).shift(LEFT*2.9).shift(UP*0.58).shift(UP*0.58)
        consoleTxt = Text(
            "console: ",
            font="Courier new",
            font_size=30
        )
        forLoopDisplay = Text(
            "nothing yet...",
            font="Courier new",
            font_size=30
        ).next_to(consoleTxt, DOWN)
        consoleDisplayVGroup = VGroup(
            consoleTxt,
            forLoopDisplay
        ).to_corner(DL)

        line1.next_to(line2, UP)
        line3.next_to(line2, DOWN)
        line4.next_to(line3, DOWN)

        line2.shift(LEFT*0.7)
        line3.shift(LEFT*3.4)
        line4.shift(LEFT*1.18)

        forLoopGroup= VGroup(
            line1,
            line2,
            line3,
            line4
        )

        for line in forLoopGroup:
            self.play(Write(line))
        self.wait(4)

        self.play(forLoopGroup.animate.to_edge(LEFT))
        
        for thing in valueOfIVGroup:
            self.play(Create(thing))

        self.play(Create(curLineExecuting))

        curCondition = Text("current condition:\n      0 <= 5", 
            font="Courier new", 
            font_size=30
        ).next_to(valueOfIVGroup, DOWN*1.5)
        conditionResults = [
            # 0 FALSE
            # 1 TRUE
            Text(
                "false",
                font="Courier new",
                font_size=30,
                color=RED
            ).next_to(curCondition, DOWN),
            Text(
                "true",
                font="Courier new",
                font_size=30,
                color=GREEN
            ).next_to(curCondition, DOWN),
        ]

        self.wait(1)

        for displayConsole in consoleDisplayVGroup:
            self.play(Write(displayConsole))

        # FOR LOOP STARTS
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.play(Write(curCondition))
        self.play(Write(conditionResults[1]))
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)

        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0")
        self.updateIValue(iValue, iVar, 1)
        self.wait(0.5)
       
        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 1)
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1")
        self.updateIValue(iValue, iVar, 2)
        self.wait(0.5)

        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 2)
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1 2")
        self.updateIValue(iValue, iVar, 3)
        self.wait(0.5)

        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 3)
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1 2 3")
        self.updateIValue(iValue, iVar, 4)
        self.wait(0.5)

        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 4)
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1 2 3 4")
        self.updateIValue(iValue, iVar, 5)
        self.wait(0.5)

        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 5)
        self.ScaleUpAndDown(conditionResults[1])
        self.moveCurLineExecuting(curLineExecuting, DOWN)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1 2 3 4 5")
        self.updateIValue(iValue, iVar, 6)
        self.wait(0.5)

        self.moveCurLineExecuting(curLineExecuting, UP)
        self.wait(1)
        self.updateCurCondition(curCondition, valueOfIVGroup, 6)
        self.play(Transform(conditionResults[1], conditionResults[0]))
        self.wait(1)
        # self.ScaleUpAndDown(conditionResults[0])
        self.moveCurLineExecuting(curLineExecuting, DOWN, 3)
        self.updateConsoleOutput(consoleTxt, forLoopDisplay, "0 1 2 3 4 5")

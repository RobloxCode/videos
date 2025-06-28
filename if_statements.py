from manim import *

class IfStatements(Scene):
    def construct(self):
        ifKeyWord = Text(
            "if" ,
            font="Courier new",
            font_size=30
        )
        ifCondition = Text(
            "some_condition" ,
            font="Courier new",
            font_size=30
        )
        semicolon= Text(
            ":" ,
            font="Courier new",
            font_size=30
        )
        someCodeTxt = Text(
            "# some code",
            font="Courier new",
            font_size=30
        )
        conditionResults = [
            # 0 FALSE
            # 1 TRUE
            Text(
                "false",
                font="Courier new",
                font_size=30,
                color=RED
            ).next_to(ifCondition, DOWN*1.5).shift(RIGHT*2.5),
            Text(
                "true",
                font="Courier new",
                font_size=30,
                color=GREEN
            ).next_to(ifCondition, DOWN*1.5).shift(LEFT*2.5)
        ]
        trueConditionEx1 = Text(
            "if 1 < 3:",
            font="Courier new",
            font_size=30
        )
        trueConditionEx2 = Text(
            'if "hello" != "hi":',
            font="Courier new",
            font_size=30
        )
        trueConditionEx3 = Text(
            'if 10 == 10:',
            font="Courier new",
            font_size=30
        )
        falseConditionEx1 = Text(
            "if 3 < 1:",
            font="Courier new",
            font_size=30
        )
        falseConditionEx2 = Text(
            'if 2 == 1:',
            font="Courier new",
            font_size=30
        )
        falseConditionEx3 = Text(
            'if "python" == "C":',
            font="Courier new",
            font_size=30
        )
        trueCoditionsExamplesVGroup = VGroup(
            trueConditionEx1,
            trueConditionEx2,
            trueConditionEx3
        )
        falseConditionsExamplesVGroup = VGroup(
            falseConditionEx1,
            falseConditionEx2,
            falseConditionEx3
        )
        equalsOperator = Text(
            "==",
            font="Courier new",
            font_size=35
        ).shift(UP*1.5)
        differentThan = Text(
            "!=",
            font="Courier new",
            font_size=35
        ).next_to(equalsOperator, DOWN)
        lessThan = Text(
            "<",
            font="Courier new",
            font_size=35
        ).next_to(differentThan, DOWN)
        GreaterThan= Text(
            ">",
            font="Courier new",
            font_size=35
        ).next_to(lessThan, DOWN)
        lessEqualTo = Text(
            "<=",
            font="Courier new",
            font_size=35
        ).next_to(GreaterThan, DOWN)
        greaterEqualTo = Text(
            ">=",
            font="Courier new",
            font_size=35
        ).next_to(lessEqualTo, DOWN)
        conditionOperators = VGroup(
            equalsOperator,
            differentThan,
            lessThan,
            GreaterThan,
            lessEqualTo,
            greaterEqualTo
        )
        codeExLine1 = Text(
            "age = 13",
            font="Courier new",
            font_size=35
        )
        codeExLine2 = Text(
            "if age >= 18:",
            font="Courier new",
            font_size=35
        )
        codeExLine3 = Text(
            'print("You are an adult now")',
            font="Courier new",
            font_size=35
        )
        codeExLine4 = Text(
            "else:",
            font="Courier new",
            font_size=35
        )
        codeExLine5 = Text(
            'print("You are not an adult yet")',
            font="Courier new",
            font_size=35
        )
        codeExLine1.shift(UP*2)
        codeExLine2.next_to(codeExLine1, DOWN)
        codeExLine3.next_to(codeExLine2, DOWN)
        codeExLine4.next_to(codeExLine3, DOWN)
        codeExLine5.next_to(codeExLine4, DOWN)

        codeExLine2.shift(RIGHT*0.7)
        codeExLine3.shift(RIGHT*4)
        codeExLine4.shift(LEFT*0.5)
        codeExLine5.shift(RIGHT*4.6)
        
        codeExLineVGroup = VGroup(
            codeExLine1,
            codeExLine2,
            codeExLine3,
            codeExLine4,
            codeExLine5
        ).to_edge(LEFT)

        ifKeyWord.next_to(ifCondition, LEFT)
        semicolon.next_to(ifCondition, RIGHT)
        someCodeTxt.next_to(ifCondition, DOWN)

        ifKeyWord.shift(LEFT*0.1)
        semicolon.shift(LEFT*0.09)
        someCodeTxt.shift(LEFT*0.5)

        ifStatementVGroup = VGroup(
            ifKeyWord,
            ifCondition,
            semicolon,
            someCodeTxt
        )

        self.wait(8)

        for ifStPart in ifStatementVGroup:
            self.play(Write(ifStPart))
            self.wait(2)
        
        self.wait(2)

        self.play(FadeOut(ifStatementVGroup[0]))
        self.play(FadeOut(ifStatementVGroup[2]))
        self.play(FadeOut(ifStatementVGroup[3]))
        self.play(ifStatementVGroup[1].animate.scale(1.3))

        self.wait(2)

        self.play(Write(conditionResults[1]))
        self.play(Write(conditionResults[0]))

        self.wait(2)
        self.play(FadeOut(ifStatementVGroup[1]))
        self.play(FadeOut(conditionResults[0]))

        self.play(conditionResults[1].animate.move_to(ORIGIN).shift(UP*1.2))

        for trueConditionEx in trueCoditionsExamplesVGroup:
            self.play(Write(trueConditionEx))
            self.wait(4)
            self.play(FadeOut(trueConditionEx))

        self.wait(3)
        
        conditionResults[0].move_to(ORIGIN).shift(UP*1.2)
        self.play(Transform(conditionResults[1], conditionResults[0]))

        for falseConditionEx in falseConditionsExamplesVGroup:
            self.play(Write(falseConditionEx))
            self.wait(4)
            self.play(FadeOut(falseConditionEx))
        
        self.play(FadeOut(conditionResults[1]))
        
        self.wait(2)
        
        for conditionOperator in conditionOperators:
            self.play(Write(conditionOperator))
            self.wait(1)

        for conditionOperator in conditionOperators:
            self.play(FadeOut(conditionOperator))

        self.wait(2)

        self.play(Write(codeExLineVGroup[0]))
        self.play(Write(codeExLineVGroup[1]))
        self.play(Write(codeExLineVGroup[2]))
        self.wait(25)
        self.play(Write(codeExLineVGroup[3]))
        self.play(Write(codeExLineVGroup[4]))
        self.wait(8)

        for line in codeExLineVGroup:
            self.play(FadeOut(line))

        self.wait(4)

        txtPythonLO =  Text(
            "Python" ,
            font="Courier new",
            font_size=30
        )
        andOperatorPython = Text(
            "and" ,
            font="Courier new",
            font_size=30
        ).next_to(txtPythonLO, DOWN)
        orOperatorPython = Text(
            "or" ,
            font="Courier new",
            font_size=30
        ).next_to(andOperatorPython, DOWN)
        notOperatorPython = Text(
            "not" ,
            font="Courier new",
            font_size=30
        ).next_to(orOperatorPython, DOWN)
        txtOtherPLLO =  Text(
            "Other languages" ,
            font="Courier new",
            font_size=30
        )
        andOperatorOtheL = Text(
            "&&" ,
            font="Courier new",
            font_size=30
        ).next_to(txtOtherPLLO, DOWN)
        orOperatorOtherL = Text(
            "||" ,
            font="Courier new",
            font_size=30
        ).next_to(andOperatorOtheL, DOWN)
        notOperatorOtherL = Text(
            "!" ,
            font="Courier new",
            font_size=30
        ).next_to(orOperatorOtherL, DOWN)

        logicalOperatorsPythonVGroup = VGroup(
            txtPythonLO,
            andOperatorPython, 
            orOperatorPython, 
            notOperatorPython
        ).to_edge(LEFT).shift(RIGHT*2)

        logicalOperatorsOtherLVGroup = VGroup(
            txtOtherPLLO,
            andOperatorOtheL, 
            orOperatorOtherL, 
            notOperatorOtherL
        ).to_edge(RIGHT).shift(LEFT*2)

        for logicalOpPython in logicalOperatorsPythonVGroup:
            self.play(Write(logicalOpPython))

        self.wait(3)

        for logicalOpOtherL in logicalOperatorsOtherLVGroup:
            self.play(Write(logicalOpOtherL))
        self.wait(2)
        for logicalOpOtherL in logicalOperatorsOtherLVGroup:
            self.play(FadeOut(logicalOpOtherL), run_time=0.5)

        self.play(logicalOperatorsPythonVGroup.animate.move_to(ORIGIN))
        self.play(FadeOut(logicalOperatorsPythonVGroup[0]))
        self.play(FadeOut(logicalOperatorsPythonVGroup[2]))
        self.play(FadeOut(logicalOperatorsPythonVGroup[3]))

        self.play(logicalOperatorsPythonVGroup[1].animate.move_to(ORIGIN).shift(UP*2))

        andExampleLine1 = Text(
            "if condition_1 and condition_2:",
            font="Courier new",
            font_size=30
        )
        andExampleLine2 = Text(
            "# some code",
            font="Courier new",
            font_size=30
        ).next_to(andExampleLine1, DOWN).shift(LEFT*1.6)
        rect = Rectangle(
            height=0.6, width=3,
            stroke_color=GREEN,
            fill_opacity=0
        ).shift(LEFT*1.7).shift(UP*0.3)
        rect2 = Rectangle(
            height=0.6, width=3,
            stroke_color=GREEN,
            fill_opacity=0
        ).shift(LEFT*1.7).shift(UP*0.3)

        orExampleLine1 = Text(
            "if condition_1 or condition_2:",
            font="Courier new",
            font_size=30
        )
        orExampleLine2 = Text(
            "# some code",
            font="Courier new",
            font_size=30
        ).next_to(orExampleLine1, DOWN).shift(LEFT*1.6)

        notExampleLine1 = Text(
            "if not False:",
            font="Courier new",
            font_size=30
        )
        notExampleLine2 = Text(
            "# some code",
            font="Courier new",
            font_size=30
        ).next_to(notExampleLine1, DOWN)

        andLogicalOpCode = VGroup(
            andExampleLine1,
            andExampleLine2
        ).next_to(logicalOperatorsPythonVGroup[1], DOWN).shift(DOWN*1.2)

        orLogicalOpCode = VGroup(
            orExampleLine1,
            orExampleLine2
        ).next_to(logicalOperatorsPythonVGroup[1], DOWN).shift(DOWN*1.2)

        notLogicalOpCode = VGroup(
            notExampleLine1,
            notExampleLine2
        ).next_to(logicalOperatorsPythonVGroup[1], DOWN).shift(DOWN*1.2)

        self.wait(2)
        for line in andLogicalOpCode:
            self.play(Write(line))

        self.wait(2)
        self.play(Create(rect))
        self.play(Create(rect2))
        self.play(rect2.animate.shift(RIGHT*4))
        self.play(rect2.animate.set_color(RED))
        self.wait(3)
        self.play(rect.animate.set_color(RED))
        self.wait(2)

        # updating now to the or operator
        logicalOperatorsPythonVGroup[2].shift(UP*2)
        self.play(FadeOut(rect))
        self.play(FadeOut(rect2))
        for line in andLogicalOpCode:
            self.play(FadeOut(line))

        self.wait(2)
        self.play(Transform(logicalOperatorsPythonVGroup[1], logicalOperatorsPythonVGroup[2]))

        for line in orLogicalOpCode:
            self.play(Write(line))
        
        self.wait(2)

        rect.shift(RIGHT*0.09)
        rect.set_color(GREEN)
        self.wait(2)
        self.play(Create(rect))
        self.play(Create(rect2))
        self.wait(3)
        self.play(rect2.animate.set_color(GREEN))
        self.wait(2)

        # not logical operator
        logicalOperatorsPythonVGroup[3].move_to(ORIGIN).shift(UP*2)
        self.play(FadeOut(rect))
        self.play(FadeOut(rect2))
        for line in orLogicalOpCode:
            self.play(FadeOut(line))

        self.wait(2)
        # self.play(FadeOut(logicalOperatorsPythonVGroup[1]))
        self.play(Transform(logicalOperatorsPythonVGroup[1], logicalOperatorsPythonVGroup[3]))

        for line in notLogicalOpCode:
            self.play(Write(line))

        self.wait(3)
        self.play(Transform(notLogicalOpCode[0], Text(
            "if True:",
            font="Courier new",
            font_size=30
        ).shift(UP*0.2)))

        self.wait(2)
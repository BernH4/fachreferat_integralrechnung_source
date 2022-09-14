from manim import *
from manim_editor import PresentationSectionType

# config.background_color = WHITE
# config["background_color"] = WHITE

def fade_out_all(self):
        self.play(*[FadeOut(mob)for mob in self.mobjects])


class intro(Scene):
    def construct(self):
        riemann = Text("Herleitung des Hauptsatzes der Differential- und Integralrechnung", font_size=85).scale(0.3).shift(UP)
        riemann2 = Text("zur Ermittlung der Maßzahl krummlinig begrenzter", font_size=85).scale(0.3)
        riemann3 = Text("Flächen mit Hilfe des bestimmten Integrals", font_size=85).scale(0.3)
        riemann2.next_to(riemann, DOWN)
        riemann3.next_to(riemann2, DOWN)
        self.next_section("Intro", PresentationSectionType.NORMAL)
        self.play(FadeIn(VGroup(riemann, riemann2, riemann3)))
        self.wait(0.2) #slide

class inhaltsverzeichnis(Scene):
    def construct(self):
        fs=30
        inhalt = VGroup(Text("Inhaltsverzeichnis:", font_size=60),
            Text("1. Themeneinführung", font_size=fs),
            Text("2. Bestimmung einfacher Flächeninhaltsfunktionen", font_size=fs),
            Text("3. Bestimmung der Flächeninhaltsfunktion einer \n\tquadratischen Randfunktion", font_size=fs),
            Text("4. Zusammenhang von Randfunktion und \n\tFlächeninhaltsfunktion ", font_size=fs),
            Text("5. Fläche über einem Intervall", font_size=fs),
            Text("6. Schreibweise und Begriffsdefinitionen", font_size=fs),
            Text("7. Lösen des Ausgangsproblems", font_size=fs),
            )
        inhalt.arrange(DOWN, center=False, aligned_edge=LEFT,buff=0.4).to_edge(LEFT).to_edge(UP)

        # image= ImageMobject("inhaltsverzeichnis.png")
        # image.scale(0.45)
        # # image.to_edge(RIGHT, buff=1)

        self.next_section("Inhaltsverzeichnis", PresentationSectionType.NORMAL)
        for punkt in inhalt:
            self.add(punkt)
            self.next_section("",PresentationSectionType.SUB_NORMAL)
            self.wait(0.1)

class praxisbeispiel(Scene):
    def construct(self):

        title = Tex(r"1. Themeneinführung", font_size=40).to_edge(UP)

        ax = Axes(
            x_range=[-1, 5],
            x_length=7,
            y_range=[-1, 8],
            y_length=7,

        ).next_to(title,DOWN).to_edge(LEFT).add_coordinates().scale(0.7)
        labels = ax.get_axis_labels(
            x_label=Tex("$t$ in $s$"), y_label=Tex("$v$ in $m/s$")
        )

        question = VGroup(Text("Wie viel Meter hat der Fahrer"), Text("zwischen Sekunde 2 und 4 zurückgelegt?"), Text(r"Die Geschwindigkeit verläuft nach der Funktion:", font_size = 40) ,MathTex("f(t) = 0,5t^3-3t^2+4t+4", font_size=70)).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.43).next_to(ax, RIGHT).shift(0.5*UP)
        curve = ax.plot(
                # lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
                # lambda x: -x*x+4*x,
                lambda x: 0.5*x**3-3*x**2+4*x+4,
                x_range=[0, 4.5],
                color=GREEN
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(4, curve), color=YELLOW)
        area = ax.get_area(
            curve,
            x_range=(2,4),
            color=(YELLOW_B, YELLOW_D),
            opacity=0.5,
        )

        # ax_o.set_color(BLACK)
        # ax_u.set_color(BLACK)
        # labels_o.set_color(BLACK)

        #FLÄCHE hervorheben
        # line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, quadratic), color=YELLOW)
        # line_2 = ax.get_vertical_line(ax.input_to_graph_point(6, quadratic), color=YELLOW)
        # area = ax.get_area(quadratic, [2, 6], color=YELLOW, opacity=0.5)

        # self.play(FadeIn(question))
        # self.wait(1)
        # self.play(question.animate.to_edge(UP, buff=1))
        self.next_section("1.0",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(ax), FadeIn(curve), FadeIn(labels))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(question), FadeIn(line_1), FadeIn(line_2))
        # self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(area))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        # fade_out_all(self)
        # self.wait(10)#slide
        # fade_out_all(self)

class konstante_funk (Scene):
    def construct(self):

        k = ValueTracker(0)
        title = Text("2.1 Konstante Funktion", font_size=30).to_edge(UP)#.shift(3*UP)

        ax = Axes(
            x_range=[-1, 4],
            x_length=6,
            y_range=[-1, 4],
            y_length=6,

        ).to_edge(LEFT).add_coordinates()#.scale(0.7)
        labels = ax.get_axis_labels(
            x_label="x", y_label="y"
        )
        func_lab = (
            # MathTex("f(x)=\\frac{1}{3} {x}^{3}")
            MathTex("f(x)=2")
            .set(width=2.5)
            .next_to(ax, UP, buff=0.2)
            .set_color(GREEN)
            .shift(0.5*RIGHT)
            .shift(1.5*DOWN)
        )

        # question = VGroup(Text("Fläche im Intervall "), Text("zwischen Sekunde 2 und 4 zurückgelegt?")).scale(0.43).next_to(ax, RIGHT).shift(UP).arrange(DOWN, center=False)
        question = Tex(r"Fläche im Intervall $[0;x]$?", font_size=40).next_to(ax, RIGHT).shift(UP)
        answer = Tex(r"$A(x) = 2x$", font_size=60).set_color(RED_C)#.next_to(question, 2*DOWN)
        VGroup(question, answer).arrange(DOWN,buff=0.5).next_to(ax,RIGHT, buff=1)

        curve = ax.plot(
                # lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
                # lambda x: -x*x+4*x,
                lambda x: 2,
                x_range=[0, 3.5],
                color=GREEN
        )

        line_1 = ax.get_vertical_line(ax.i2gp(0, curve), color=YELLOW)

        moving_line_2 = always_redraw(
                lambda: ax.get_vertical_line(ax.input_to_graph_point(k.get_value(), curve), color=YELLOW)
                )

        moving_area = always_redraw(
                lambda: ax.get_area( curve, x_range=(0,k.get_value()), color=(YELLOW_B, YELLOW_D), opacity=0.5)
                )




        #FLÄCHE hervorheben
        # line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, quadratic), color=YELLOW)
        # line_2 = ax.get_vertical_line(ax.input_to_graph_point(6, quadratic), color=YELLOW)
        # area = ax.get_area(quadratic, [2, 6], color=YELLOW, opacity=0.5)

        self.next_section("2.1",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(ax), FadeIn(curve), FadeIn(labels), FadeIn(func_lab))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(question))#, FadeIn(line_1), FadeIn(line_2))
        # self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(line_1), FadeIn(moving_line_2), FadeIn(moving_area))
        self.play(k.animate.set_value(3), run_time=2)
        self.play(k.animate.set_value(1.3), run_time=2)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(answer))
        self.wait(10)
        # fade_out_all(self)
        # self.wait(10)#slide
        # fade_out_all(self)

class lineare_funk_m_versch(Scene):
    def construct(self):

        k = ValueTracker(0)
        title = Text("2.2 Lineare Funktion m. Verschiebung in y-Richtung", font_size=20).to_edge(RIGHT).to_edge(UP)#.shift(3*UP)

        ax = Axes(
            x_range=[-1, 6],
            x_length=8,
            y_range=[-1, 5],
            y_length=6

        ).to_edge(LEFT).shift(0.5 * DOWN).add_coordinates()#.set_color(BLACK)
        labels = ax.get_axis_labels(
            x_label="x", y_label="y"
        )

        # rect = Rectangle(width=4, height=2).move_to(ax.coords_to_point(0,0), aligned_edge = LEFT*UP)
        func_lab = (
            # MathTex("f(x)=\\frac{1}{3} {x}^{3}")
            MathTex("f(x)=0.6x+2")
            .set(width=3.5)
            .next_to(ax, UP)
            .set_color(GREEN)
            .shift(0.2 * RIGHT)
            .shift(0.2 * DOWN)
        )


        curve = ax.plot(
                lambda x: 0.6*x+2,
                x_range=[0, 4.5],
                color=GREEN
        )
        konst = ax.plot(
                lambda x: 2,
                x_range=[0, 4.5],
                color=GREEN
        )

        rect_area = ax.get_area(konst, x_range=(0,3.7), color=(YELLOW_B, YELLOW_D), opacity=0.5)
        triangle_area = ax.get_area(curve, x_range=(0,3.7),bounded_graph=konst, color=(BLUE_B, BLUE_D), opacity=0.5)

        # question = VGroup(Text("Fläche im Intervall "), Text("zwischen Sekunde 2 und 4 zurückgelegt?")).scale(0.43).next_to(ax, RIGHT).shift(UP).arrange(DOWN, center=False)
        # Arect = Tex(r" sdf$A_r(x) = 2x", font_size=40).next_to(rect_area, RIGHT)
        # Atriangle = Tex(r" sdf $A_d(x) = \\frac{1}{2}\cdot g \cdot h = 2x$", font_size=40).next_to(triangle_area, RIGHT)
        # answer = Tex(r"$A(x) = 2x$", font_size=60).set_color(RED_C).next_to(question, 2*DOWN)

        #FLÄCHE hervorheben
        # line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, quadratic), color=YELLOW)
        # line_2 = ax.get_vertical_line(ax.input_to_graph_point(6, quadratic), color=YELLOW)
        # area = ax.get_area(quadratic, [2, 6], color=YELLOW, opacity=0.5)

        self.next_section("2.2",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(ax), FadeIn(curve), FadeIn(labels), FadeIn(func_lab))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        # self.play(FadeIn(question))#, FadeIn(line_1), FadeIn(line_2))
        # self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(rect_area), FadeIn(triangle_area))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        Arect = MathTex("A_r(x) = 2x", font_size=30).next_to(rect_area, RIGHT)
        self.play(FadeIn(Arect))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        all_in_ax = VGroup(ax, curve, labels, rect_area, triangle_area, Arect)
        func_lab.generate_target()
        func_lab.target.shift(0.5*DOWN)
        self.play(all_in_ax.animate.scale(0.7).to_edge(LEFT),MoveToTarget(func_lab),  runtime= 1)

        ATriangle1 = MathTex("A_d(x) = \\frac{1}{2}\cdot g \cdot h", font_size=30)
        ATriangle2 = MathTex("= \\frac{1}{2}\cdot x \cdot f(x) -2", font_size=30)
        ATriangle3 = MathTex("= \\frac{1}{2}\cdot x \cdot 0,6x + 2 -2", font_size=30)
        ATriangle4 = MathTex("= 0,3x^2", font_size=30)
        ATriangle= VGroup(ATriangle1, ATriangle2, ATriangle3, ATriangle4).arrange(RIGHT).next_to(triangle_area, RIGHT)
        self.play(FadeIn(ATriangle1))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(ATriangle2))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(ATriangle3))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(ATriangle4))
        answer = Tex(r"$A(x) = A_r + A_d = 0,3x^2 + 2x$", font_size=50).set_color(RED_C).next_to(Arect, RIGHT, buff= 0.4).shift(0.3*UP).shift(0.5*RIGHT)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(answer))
        # self.wait(10)
        # fade_out_all(self)

class quadratische_funktion(Scene):
    def construct(self):
        title = Text("3.1 Approximation des Flächeninhalts mit wenigen Rechtecken", font_size=20).to_edge(UP)
        ax_o = Axes(
            x_range=[-1, 2.5],
            x_length=2*4,
            y_range=[-1, 5],
            y_length=1.2*5,

        ).align_to(title, UP).to_edge(RIGHT).shift(DOWN).add_coordinates()
        labels_o = ax_o.get_axis_labels(
            x_label="x", y_label="y"
        )
        ax_u = Axes(
            x_range=[-1, 2.5],
            x_length=2*4,
            y_range=[-1, 5],
            y_length=1.2*5,

        ).align_to(title, UP).to_edge(RIGHT).shift(DOWN).add_coordinates()
        labels_u = ax_u.get_axis_labels(
            x_label="x", y_label="y"
        )

        question = Tex(r"Fläche im Intervall $[0;2]$?", font_size=40)
        question.next_to(ax_o, LEFT).shift(UP).shift(RIGHT)


        quadratic_o = ax_o.plot(
                lambda x: x**2,
                x_range=[-0.3, 2.1],
                color=GREEN
        )
        quadratic_u = ax_u.plot(
                lambda x: x**2,
                x_range=[-0.3, 2.1],
                color=GREEN
        )

        # rects = VGroup()
        # the rectangles are constructed from their top right corner.
        # passing an iterable to `color` produces a gradient
        # for dx in np.arange(0.2, 0.05, -0.05):

        all_obersumme = VGroup(ax_o, labels_o, quadratic_o)
        all_untersumme = VGroup(ax_u, labels_u, quadratic_u).shift(UP).scale(0.5)

        # self.play(LaggedStart(
        self.next_section("3.1",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(all_obersumme), FadeIn(question))
        self.next_section("",PresentationSectionType.SUB_NORMAL)

        four_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/4,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )
        four_rects_u = ax_u.get_riemann_rectangles(
            quadratic_u,
            x_range=[0, 2],
            dx=2/4,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="left",
        )
        # Riemann Rechtecke einblenden
        self.play(
            # DrawBorderThenFill(
            FadeIn(
                    four_rects_o,
                    run_time=1,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(question))
        self.play(VGroup(all_obersumme, four_rects_o).animate.scale(0.5).to_edge(LEFT).shift(UP), runtime= 2)

        title_obersumme = Tex("Obersumme $O_n$").next_to(all_obersumme, UP).set(width=2.5).set_color(GREEN)
        title_untersumme = Tex("Untersumme $U_n$").next_to(all_untersumme, UP).set(width=2.5).set_color(GREEN)

        #für screenshots (weißer Hintergrund)
        # ax_o.set_color(BLACK)
        # ax_u.set_color(BLACK)
        # labels_o.set_color(BLACK)
        # labels_u.set_color(BLACK)
        # title_untersumme.set_color(BLACK)
        # title_obersumme.set_color(BLACK)

        self.play(FadeIn(all_untersumme),  FadeIn(title_obersumme),  FadeIn(title_untersumme))
        # Riemann Rechtecke einblenden
        self.play(FadeIn(four_rects_u, run_time=1, rate_func=smooth, lag_ratio=0.5))
            # run_time=0.1, lag_ratio=0.1)

        math_obersumme1 = MathTex("O_4 = 0,5 \cdot f(0,5) + 0,5 \cdot f(1) + 0,5 \cdot f(1,5)+ 0,5 \cdot f(2)", font_size=50).next_to(all_obersumme, DOWN).to_edge(LEFT)
        math_obersumme2 = MathTex("O_4 = 0,5 \cdot (0,5^2 + 1^2 + 1,5^1 + 2^2)", font_size=50).next_to(math_obersumme1, DOWN).to_edge(LEFT)
        math_obersumme3 = MathTex("= 3,75 \,FE", font_size=50).next_to(math_obersumme2, RIGHT)
        math_untersumme1 = MathTex("U_4 = 0,5 \cdot f(0) + 0,5 \cdot f(0.5) + 0,5 \cdot f(1)+ 0,5 \cdot f(1,5)", font_size=50).next_to(all_untersumme, DOWN).to_edge(LEFT)
        math_untersumme2 = MathTex("U_4 = 0,5 \cdot (0^2 + 0,5^2 + 1^1 + 1,5^2)", font_size=50).next_to(math_untersumme1, DOWN).to_edge(LEFT)
        math_untersumme3 = MathTex("= 1,75 \,FE", font_size=50).next_to(math_untersumme2, RIGHT)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math_obersumme1))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math_obersumme2))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math_obersumme3))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(Transform(VGroup(math_obersumme1,math_obersumme2,math_obersumme3), VGroup(math_untersumme1,math_untersumme2,math_untersumme3)))

        sixteen_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/16,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )
        sixteen_rects_u = ax_u.get_riemann_rectangles(
            quadratic_u,
            x_range=[0, 2],
            dx=2/16,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="left",
        )
        thirtytwo_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/32,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )
        thirtytwo_rects_u = ax_u.get_riemann_rectangles(
            quadratic_u,
            x_range=[0, 2],
            dx=2/32,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="left",
        )
        sixtyfour_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/64,
            stroke_width=1,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )
        sixtyfour_rechts_u = ax_u.get_riemann_rectangles(
            quadratic_u,
            x_range=[0, 2],
            dx=2/64,
            stroke_width=1,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="left",
        )

        asixtyfour_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/256,
            stroke_width=0,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )
        asixtyfour_rechts_u = ax_u.get_riemann_rectangles(
            quadratic_u,
            x_range=[0, 2],
            dx=2/256,
            stroke_width=0,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="left",
        )
        # self.play(FadeOut(math_obersumme1))
        solution_o = MathTex("O_4 = 3,75 \,FE", font_size=50).next_to(all_obersumme, DOWN)
        solution_u = MathTex("U_4 = 1,75 \,FE", font_size=50).next_to(all_untersumme, DOWN)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(math_obersumme1),FadeOut(math_obersumme2),FadeOut(math_obersumme3))
        self.play(FadeIn(solution_o), FadeIn(solution_u))
        # self.play(Transform(VGroup(math_untersumme1, math_untersumme2, math_untersumme3), MathTex("U_4 = 1,75 \,FE", font_size=50).next_to(all_untersumme,DOWN)))

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        solution_16_o = MathTex("O_{16} = 2,92 \,FE", font_size=50).next_to(solution_o, DOWN).align_to(solution_o, RIGHT)
        solution_16_u = MathTex("U_{16} = 2,42 \,FE", font_size=50).next_to(solution_u, DOWN).align_to(solution_u, RIGHT)
        self.play(ReplacementTransform( four_rects_o, sixteen_rects_o, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_16_o))
        self.play(ReplacementTransform( four_rects_u, sixteen_rects_u, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_16_u))

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        solution_32_o = MathTex("O_{32} = 2,79 \,FE", font_size=50).next_to(solution_16_o, DOWN).align_to(solution_o, RIGHT)
        solution_32_u = MathTex("U_{32} = 2,54 \,FE", font_size=50).next_to(solution_16_u, DOWN).align_to(solution_u, RIGHT)
        self.play(ReplacementTransform(sixteen_rects_o, thirtytwo_rects_o, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_32_o))
        self.play(ReplacementTransform(sixteen_rects_u, thirtytwo_rects_u, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_32_u))

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        solution_64_o = MathTex("O_{64} = 2,73 \,FE", font_size=50).next_to(solution_32_o, DOWN).align_to(solution_o, RIGHT)
        solution_64_u = MathTex("U_{64} = 2,60 \,FE", font_size=50).next_to(solution_32_u, DOWN).align_to(solution_u, RIGHT)
        self.play(ReplacementTransform( thirtytwo_rects_o, sixtyfour_rects_o, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_64_o))
        self.play(ReplacementTransform( thirtytwo_rects_u, sixtyfour_rechts_u, run_time=2, rate_func=smooth, lag_ratio=0.5), FadeIn(solution_64_u))

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(sixtyfour_rects_o, asixtyfour_rects_o, run_time=2, rate_func=smooth, lag_ratio=0.5), ReplacementTransform(sixtyfour_rechts_u, asixtyfour_rechts_u, run_time=2, rate_func=smooth, lag_ratio=0.5))


        # self.next_section("",PresentationSectionType.SUB_NORMAL)
        # area_o = ax_o.get_area( quadratic_o, x_range=(0,2), color=(YELLOW_B, YELLOW_D), opacity=0.5)
        # area_u = ax_u.get_area( quadratic_u, x_range=(0,2), color=(YELLOW_B, YELLOW_D), opacity=0.5)

        # self.play(Transform(sixteen_rects_o, area_o, run_time = 5), FadeOut(four_rects_o))
        # self.play(Transform(sixteen_rects_u, area_u, run_time = 5), FadeOut(four_rects_u))



        # Anzahl erhöhen
        # for rect in rects[1:]:
        #     self.play(
        #         Transform(
        #             rects[0], rect,
        #             run_time=2,
        #             rate_func=smooth,
        #             lag_ratio=0.5,
        #         ),
        #     )


class quadratische_funktion_n_rechtecke(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathtools}")
        title = Text("3.2 Ober- und Untersumme unter dem Graphen mit unendlich vielen Rechtecken", font_size=20).to_edge(UP)
        ax_o= Axes(
            x_range=[-1, 2.5],
            x_length=2*4,
            y_range=[-1, 5],
            y_length=1.2*5,

        ).align_to(title, UP).to_edge(RIGHT).shift(DOWN).shift(RIGHT).add_coordinates()
        labels_o = ax_o.get_axis_labels(
            x_label="x", y_label="y"
        )

        quadratic_o = ax_o.plot(
                lambda x: x**2,
                x_range=[-0.3, 2.1],
                color=GREEN
        )
        four_rects_o = ax_o.get_riemann_rectangles(
            quadratic_o,
            x_range=[0, 2],
            dx=2/4,
            stroke_width=2,
            # color=(TEAL, RED_B, RED),
            fill_opacity = 0.6,
            input_sample_type="right",
        )

        graph = VGroup(ax_o,labels_o, quadratic_o, four_rects_o).scale(0.6)
        brace_s = BraceBetweenPoints(ax_o.c2p(1,0),ax_o.c2p(1.5,0))
        bracelabel = brace_s.get_tex("\\Delta x = \\frac{x}{n}")
        brace = VGroup(brace_s, bracelabel).shift(0.2*DOWN)


        # bracelabel = BraceLabel(brace, "hi")
        fs = 35
        math1 = MathTex(r'O_n &= \frac{x}{n} \cdot f(1 \cdot \frac{x}{n}) + \frac{x}{n} \cdot f(2 \cdot \frac{x}{n}) + ... + \frac{x}{n} \cdot f(n \cdot \frac{x}{n})', font_size=fs)
        math2 = MathTex(r'= \frac{x}{n} \cdot \bigg[f(1 \cdot \frac{x}{n}) + f(2 \cdot \frac{x}{n}) + ... + f(n \cdot \frac{x}{n})\bigg]', font_size=fs)
        math3 = MathTex(r'= \frac{x}{n} \cdot \bigg[1^2 \cdot \frac{x^2}{n^2} + 2^2 \cdot \frac{x^2}{n^2} + ... + n^2 \cdot \frac{x^2}{n^2}\bigg]', font_size=fs)
        math4 = MathTex(r'= \frac{x^3}{n^3} \cdot \bigg[1^2  + 2^2 + ... + n^2 \bigg]', font_size=fs)
        math5 = MathTex(r'= \frac{x^3}{n^3} \cdot \bigg[\frac{1}{6}n(n+1)(2n+1)\bigg]', font_size=fs)
        left_math = VGroup(math1, math2, math3, math4,math5).arrange(DOWN, aligned_edge=LEFT).next_to(title,DOWN,buff=0.5).to_edge(LEFT)
        left_math[1:].shift(0.55*RIGHT)
        math5.generate_target()
        math5.target.next_to(title,DOWN,buff=0.5).to_edge(LEFT)

        math6 = MathTex(r'= \frac{x^3}{6n^2} \cdot \bigg[(n+1)(2n+1)\bigg]', font_size=fs)
        math7 = MathTex(r'= \frac{x^3}{6n^2} \cdot \bigg[2n^2+3n+1\bigg]', font_size=fs)
        math8 = MathTex(r'= \frac{2x^3n^2}{6n^2} + \frac{3x^3n}{6n^2} + \frac{x^3}{6n^3}', font_size=fs)
        math9 = MathTex(r'= \frac{x^3}{3} + \frac{x^3}{3n} + \frac{x^3}{6n^3}', font_size=fs)
        math10 = MathTex(r'\implies \lim\limits_{n \rightarrow \infty}{O_n} = \lim\limits_{n \rightarrow \infty}{\bigg(\frac{x^3}{3} + \frac{x^3}{3n} + \frac{x^3}{6n^3}\bigg)}', tex_template=myTemplate, font_size=fs)
        right_math = VGroup(math6, math7, math8, math9,math10).arrange(DOWN,aligned_edge=LEFT).next_to(math5.target,DOWN).to_edge(LEFT)
        math11 = MathTex(r' = \frac{x^3}{3} = \frac{1}{3}\cdot x^3', tex_template=myTemplate, font_size=fs).next_to(math10,RIGHT)

        self.next_section("3.2",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(graph), FadeIn(brace))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math1))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math2))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math3))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math4))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math5))
        self.wait(1)
        # self.play(left_math.animate.scale(0.6).to_edge(LEFT), run_time=1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(left_math[:-1]), MoveToTarget(math5))#,  runtime= 1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math6))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math7))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math8))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math9))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math10))
        self.wait(1)
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(math11))
        self.wait(1)


        herleitung = VGroup(math1,math2, math3, math4, math5, math6, math7, math8, math9, math10)
        A = MathTex(r'A(x) = \frac{1}{3}\cdot x^3', font_size=50).set_color(RED_C).next_to(graph, LEFT).shift(LEFT).shift(UP)
        A2 = MathTex(r'A(2) = \frac{1}{3}\cdot 2^3 = \frac{8}{3} \,FE', font_size=31).next_to(A, DOWN)

        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(VGroup(right_math,math5, math11)), FadeIn(A))
        self.next_section("",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(A2))
        self.next_section("",PresentationSectionType.SUB_NORMAL)


class zusammenhang(Scene):
    def construct(self):
        title = Text("4.0 Zusammenhang von Randfunktion und Flächeninhaltsfunktion", font_size=25).to_edge(UP)
        table = r"""
        \begin{center}
        \setlength{\tabcolsep}{18pt} %Breite der Spalten
        \renewcommand{\arraystretch}{1.5}
        \begin{tabular}{ |c|c|c| }
        \hline
        Randfunktion & Flächeninhaltsfunktion \\
        \hline
        \hline
        $f(x) = 2$ & $A(x) = 2x$\\
        \hline
        $f(x) = 0,6x + 2$ & $A(x) = 0,3x^2 + 2x$\\
        \hline
        $f(x) = x^2$ & $A(x) = \frac{1}{3} \cdot x^3$\\
        \hline
        \end{tabular}
        \end{center}
        """
        self.next_section("4",PresentationSectionType.NORMAL)
        tex_table = Tex(table).next_to(title,DOWN,buff=1.5)
        self.play(FadeIn(title),FadeIn(tex_table))

class flaeche_beliebiges_intervall(Scene):
    def construct(self):
        lower_limit = ValueTracker(0)
        higher_limit = ValueTracker(2)
        title = Tex(r"5. Fläche über einem Intervall $[a;b]$", font_size=40).to_edge(UP)

        ax = Axes(
            x_range=[-1, 3.5],
            x_length=2*4,
            y_range=[-1, 11,2.5],
            y_length=1.2*5,

        ).align_to(title, UP).shift(DOWN).add_coordinates().scale(0.8)
        labels = ax.get_axis_labels(
            x_label="x", y_label="y"
        )

        # question = Tex(r"Fläche im Intervall $[0;2]$?", font_size=40)
        # question.next_to(ax_o, LEFT).shift(UP).shift(RIGHT)


        quadratic = ax.plot(
                lambda x: x**2,
                x_range=[-0.3, 3.1],
                color=GREEN
        )


        graph = VGroup(ax, labels, quadratic)


        self.next_section("5.0",PresentationSectionType.NORMAL)
        self.play(FadeIn(title), FadeIn(graph))#, FadeIn(question))
        # self.next_section(" ",PresentationSectionType.SUB_NORMAL)


        # title_obersumme = Tex("Obersumme $O_n$").next_to(all_obersumme, UP).set(width=2.5).set_color(GREEN)
        # title_untersumme = Tex("Untersumme $U_n$").next_to(all_untersumme, UP).set(width=2.5).set_color(GREEN)

        # self.play(FadeIn(all_untersumme),  FadeIn(title_obersumme),  FadeIn(title_untersumme))
        # # Riemann Rechtecke einblenden
        # self.play(FadeIn(four_rects_u, run_time=1, rate_func=smooth, lag_ratio=0.5))
        #     # run_time=0.1, lag_ratio=0.1)

        # solution = MathTex("O_4 = 3,75 \,FE", font_size=50).next_to(all_obersumme, DOWN)
        # solution_u = MathTex("U_4 = 1,75 \,FE", font_size=50).next_to(all_untersumme, DOWN)
        area = always_redraw(
                lambda: ax.get_area(quadratic, x_range=(lower_limit.get_value(),higher_limit.get_value()), color=(YELLOW_B, YELLOW_D), opacity=0.5)
                )
        self.play(FadeIn(area))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(lower_limit.animate.set_value(1), run_time=2)
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(graph.animate.scale(0.9).to_edge(RIGHT).shift(UP), run_time=1)

        # f = MathTex(r"f(x) = x^2", font_size=40).next_to(graph, LEFT, buff= 2).shift(UP)
        # F = MathTex(r"F(x) = \frac{1}{3} \cdot x^3 + C", font_size=40).next_to(f,DOWN)
        f = MathTex(r"f(x) = x^2", font_size=40).next_to(graph, LEFT, buff= 2).next_to(graph, LEFT, buff= 3)
        F = MathTex(r"F(x) = \frac{1}{3} \cdot x^3 + C", font_size=40)
        functions = VGroup(f,F).arrange(DOWN, center=False, aligned_edge=LEFT)
        # A1 = MathTex(r"A = F(2) - F(1)", font_size=40).to_edge(DOWN)
        # A2 = MathTex(r"= \frac{8}{3} + C - (\frac{1}{3} + C)", font_size=40).next_to(A1,RIGHT)
        # A3 = MathTex(r"= \frac{7}{3} FE", font_size=40).next_to(A2,RIGHT)
        A1 = MathTex(r"A = F(2) - F(1)", font_size=40)
        A2 = MathTex(r"= \frac{8}{3} + C - (\frac{1}{3} + C)", font_size=40)
        A3 = MathTex(r"= \frac{7}{3} FE", font_size=40)
        answer = VGroup(A1,A2,A3).arrange(RIGHT).to_edge(DOWN)
        A2_new = MathTex(r"= \frac{8}{3} + C -\frac{1}{3} - C", font_size=40).next_to(A1,RIGHT)

        self.play(FadeIn(f))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(F))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(A1))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(A2))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeTransformPieces(A2,A2_new))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(A3))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        # self.play(k.animate.set_value(1), run_time=5)

class bergriffsdefinitionen(Scene):
    def construct(self):
        title = Tex(r"6. Schreibweise und Begriffsdefinitionen", font_size=40).to_edge(UP)
        unb = Text("Unbestimmtes Integral:", font_size = 33).next_to(title, DOWN, buff = 1).to_edge(LEFT, buff=1)
        unb_math = MathTex(r"\int f(x) \,dx  = F(x) + C", font_size = 30).next_to(unb, DOWN)

        best = Text("Bestimmtes Integral:", font_size = 33).next_to(title, DOWN, buff = 1).to_edge(RIGHT, buff=1)
        best_math = MathTex(r"\int_{a}^{b} f(x) \,dx", font_size = 30).next_to(best, DOWN)
        # unb_math = Tex(r"\int_{a}^{b} f(x) \,dx = \left[F(x)\right]_a^b = F(b) - F(a) = w, w \in \mathbb{R}")

        berechnung = Text("Flächenberechnung mit bestimmten Integral:", font_size = 33).next_to(unb_math,DOWN, buff=1).align_to(unb, LEFT)
        berechnung_math = MathTex(r"\int_{a}^{b} f(x) \,dx = F(b) - F(a)", font_size = 30).next_to(berechnung, DOWN).align_to(unb_math, LEFT)
        berechnung_math2 = MathTex(r"= \left[F(x)\right]_a^b", font_size = 30).next_to(berechnung_math, RIGHT)
        berechnung_math3 = MathTex(r"= w, w \in \mathbb{R}", font_size = 30).next_to(berechnung_math2, RIGHT)


        self.next_section("6.0",PresentationSectionType.NORMAL)
        self.play(FadeIn(title),FadeIn(unb),FadeIn(best))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(unb_math))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(best_math))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung_math))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung_math2))#, FadeIn(question))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung_math3))#, FadeIn(question))

class loesen_praxisbeispiel(Scene):
    def construct(self):
        title = Tex(r"7. Lösen des Ausgangsproblems", font_size=40).to_edge(UP)

        ax = Axes(
            x_range=[-1, 5],
            x_length=7,
            y_range=[-1, 8],
            y_length=7,

        ).next_to(title,DOWN).to_edge(LEFT).add_coordinates().scale(0.7)
        labels = ax.get_axis_labels(
            x_label=Tex("$t$ in $s$"), y_label=Tex("$v$ in $m/s$")
        )

        question = VGroup(Text("Wie viel Meter hat der Fahrer"), Text("zwischen Sekunde 2 und 4 zurückgelegt?"), Text(r"Die Geschwindigkeit verläuft nach der Funktion:", font_size = 40) ,MathTex("f(t) = 0,5t^3-3t^2+4t+4", font_size=70)).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.43).next_to(ax, RIGHT).shift(0.5*UP)
        curve = ax.plot(
                # lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
                # lambda x: -x*x+4*x,
                lambda x: 0.5*x**3-3*x**2+4*x+4,
                x_range=[0, 4.5],
                color=GREEN
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(4, curve), color=YELLOW)
        area = ax.get_area(
            curve,
            x_range=(2,4),
            color=(YELLOW_B, YELLOW_D),
            opacity=0.5,
        )

        problem = VGroup(ax, curve, labels, question)
        area_lines = VGroup(area, line_1, line_2)


        #FLÄCHE hervorheben
        # line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, quadratic), color=YELLOW)
        # line_2 = ax.get_vertical_line(ax.input_to_graph_point(6, quadratic), color=YELLOW)
        # area = ax.get_area(quadratic, [2, 6], color=YELLOW, opacity=0.5)

        # self.play(FadeIn(question))
        # self.wait(1)
        # self.play(question.animate.to_edge(UP, buff=1))
        self.next_section("7.0",PresentationSectionType.NORMAL)
        self.play( FadeIn(title), FadeIn(problem))
        self.play(FadeIn(area_lines))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        problem += area_lines
        self.play(problem.animate.scale(0.8).next_to(title,DOWN))

        berechnung1 = MathTex(r"\int_{2}^{4} (0,5t^3-3t^2+4t+4) \,dt", font_size = 30)
        berechnung2 = MathTex(r"= \left[\frac{0,5}{4}t^4-t^3+2t^2+4t\right]_2^4 ", font_size = 30)
        berechnung3 = MathTex(r"= 16 - 10 = 6\,m", font_size = 30)
        berechnung = VGroup(berechnung1,berechnung2,berechnung3).arrange(RIGHT).next_to(problem, DOWN)#.to_edge(DOWN)
        self.play(FadeIn(berechnung1))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung2))
        self.next_section(" ",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(berechnung3))
        # fade_out_all(self)

class quellen(Scene):
    def construct(self):
        image= ImageMobject("quellen.png")
        image.scale(0.5)

        self.next_section("Quellen", PresentationSectionType.NORMAL)
        self.add(image)
        self.wait(0.2) #slide

# class old_quadratische_funktion_n_rechtecke(Scene):
#     def construct(self):
#         title = Text("3.1 Approximation des Flächeninhalts mit wenigen Rechtecken", font_size=20).to_edge(UP)
#         ax = Axes(
#             x_range=[-1, 2.5],
#             x_length=2*4,
#             y_range=[-1, 5],
#             y_length=1.2*5,

#         ).align_to(title, UP).to_edge(RIGHT, buff=1).shift(DOWN)
#         question = Tex(r"Fläche im Intervall $[0;2]$?", font_size=40)
#         question.next_to(ax, LEFT).shift(UP)

#         quadratic = ax.plot(
#                 lambda x: x**2,
#                 x_range=[-1.3, 2.1],
#                 color=GREEN
#         )

#         rects = VGroup()
#         # the rectangles are constructed from their top right corner.
#         # passing an iterable to `color` produces a gradient
#         for dx in np.arange(0.2, 0.05, -0.05):
#             rect = ax.get_riemann_rectangles(
#                 quadratic,
#                             x_range=[2, 8],
#                 dx=dx,
#                 stroke_width=4*dx,
#                 # color=(TEAL, RED_B, RED),
#                 input_sample_type="left",
#             )
#             rects.add(rect)


#         self.play(LaggedStart(
#             FadeIn(ax), FadeIn(title), FadeIn(quadratic), FadeIn(question),
#             run_time=3, lag_ratio=1.0)
#             # run_time=0.1, lag_ratio=0.1)
#         )
#         self.wait(3)
#         # Riemann Rechtecke einblenden
#         self.play(
#             DrawBorderThenFill(
#                     rects[0],
#                     run_time=2,
#                     rate_func=smooth,
#                     lag_ratio=0.5,
#                 ),
#             )
#         self.wait()

#         # Anzahl erhöhen
#         for rect in rects[1:]:
#             self.play(
#                 Transform(
#                     rects[0], rect,
#                     run_time=2,
#                     rate_func=smooth,
#                     lag_ratio=0.5,
#                 ),
#             )



# class whats_riemann(Scene):
#     def construct(self):
#         ax = Axes(
#             x_range=[-2, 10],
#             x_length=10,
#             y_range=[-2, 10],
#             y_length=5,

#         )
#         question = Tex(r"Fläche im Intervall $[1;8]$", font_size=40)
#         question_sign = Text("?", font_size=60)
#                 # rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
#         question.next_to(ax, UP)
#         question_sign.next_to(question, RIGHT, buff=0.5)
#         quadratic = ax.plot(
#                 lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
#                 x_range=[-0.3, 10],
#                 color=GREEN
#         )

#         rects = VGroup()
#         # the rectangles are constructed from their top right corner.
#         # passing an iterable to `color` produces a gradient
#         for dx in np.arange(0.2, 0.05, -0.05):
#             rect = ax.get_riemann_rectangles(
#                 quadratic,
#                             x_range=[2, 8],
#                 dx=dx,
#                 stroke_width=4*dx,
#                 # color=(TEAL, RED_B, RED),
#                 input_sample_type="left",
#             )
#             rects.add(rect)


#         # ax.set_color(BLACK)
#         self.play(LaggedStart(
#             FadeIn(ax), FadeIn(quadratic), #FadeIn(question), FadeIn(question_sign),
#             run_time=3, lag_ratio=1.0)
#             # run_time=0.1, lag_ratio=0.1)
#         )
#         self.wait(3)
#         # Riemann Rechtecke einblenden
#         self.play(
#             DrawBorderThenFill(
#                     rects[0],
#                     run_time=2,
#                     rate_func=smooth,
#                     lag_ratio=0.5,
#                 ),
#             )
#         self.wait()

#         # Anzahl erhöhen
#         for rect in rects[1:]:
#             self.play(
#                 Transform(
#                     rects[0], rect,
#                     run_time=2,
#                     rate_func=smooth,
#                     lag_ratio=0.5,
#                 ),
#             )





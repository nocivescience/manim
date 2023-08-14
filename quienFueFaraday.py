from manim import *
class Faraday(Scene):
    def construct(self):
        FaradayHistory=(
            'Faraday fuel hijo de un habilidoso herrero '
            'quien paso de ser un pandillero a ser el director'
            'del prestigioo Royal Instituttion of London.'
        )
        title=Title('Faraday')
        MyTextFaraday=MarkupText(FaradayHistory,justify=True).set_width(config['frame_width'])
        self.play(Write(title),Write(MyTextFaraday), run_time=5)
        self.wait(6)
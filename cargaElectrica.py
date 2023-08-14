from manim import *
class MyCharge(Scene):
    def construct(self):
        mySentence1=Text("Primeras estimaciones")
        mySentence2=Text("De lo que se convertiría en nuetros días")
        mySentence3=Text('en el pilar de la civilización como la conocemos...')
        self.play(Write(mySentence1))
        self.wait(4)
        for myText in [mySentence2,mySentence3]:
            myText.set_width(config['frame_width'])
            self.play(Transform(mySentence1,myText))
            self.wait(6)
        self.wait()
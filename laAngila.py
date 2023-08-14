from manim import *
class LaAngila(Scene):
    def construct(self):
        texto=(
            'La llamada anguila eléctrica (Electrophorus electricus), ' 
            'también llamada temblón, temblador, gimnoto, pilaké o poraquê, ' 
            'es una especie de pez de la familia Gymnotidae. Puede emitir ' 
            'descargas eléctricas de hasta 850 voltios a partir de un grupo ' 
            'de células especializadas. Emplea las descargas eléctricas para ' 
            'cazar presas, para defenderse y para comunicarse.​ Es la especie '
            'tipo del género Electrophorus, el cual está integrado por otras 2 especies. '
            'fuente: Wikipedia'
        )
        myText=Text(texto)
        myText.set_width(config['frame_width'])
        self.play(Write(myText),run_time=5)
        self.wait(5)
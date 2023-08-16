from manim import *
class MyNumberRect(Scene):
    def construct(self):
        lin1=NumberLine(
            x_range=[0,10,1],
            length=config['frame_width']-1,
            include_tip=True,
            include_numbers=True,
        )
        texto1=MathTex('\\cdot 10^{+03}', font_size=30)
        texto1.next_to(lin1,RIGHT,buff=0.2)
        lin1.add(texto1)
        lin2=NumberLine(
            x_range=[0,10,1],
            length=config['frame_width']-1,
            include_tip=True,
            include_numbers=True,
        )
        lin3=NumberLine(
            x_range=[0,100,10],
            length=config['frame_width']-1,
            include_tip=True,
            include_numbers=True,
        )
        lin4=NumberLine(
            x_range=[0,160,16],
            length=config['frame_width']-1,
            include_tip=True,
            include_numbers=True,
        )
        texto2=MathTex('\\cdot 10^{+23}', font_size=30)
        texto2.next_to(lin2,RIGHT,buff=0.2)
        texto3= MathTex('\\cdot 10^{+02}', font_size=30)
        texto3.next_to(lin3,RIGHT,buff=0.2)
        texto4= MathTex('\\cdot 10^{+06}', font_size=30)
        texto4.next_to(lin4,RIGHT,buff=0.2)
        lin2.add(texto2)
        lin3.add(texto3)
        lin4.add(texto4)
        VGroup(lin1,lin2,lin3,lin4).set_color(RED).scale(.4)
        self.play(Create(VGroup(lin1,lin2,lin3,lin4).arrange(DOWN,buff=3).scale(0.6)))
        self.wait()
        x_value=ValueTracker(6)
        fx=lambda x:x.get_value()*1.6
        gx=lambda x:x.get_value()*1.2
        fx_value=ValueTracker(fx(x_value))
        gx_value=ValueTracker(gx(x_value))
        hx_value=ValueTracker(fx(x_value)+gx(x_value))
        decimal1=DecimalNumber(x_value.get_value(), font_size=30).add_updater(
            lambda t: t.set_value(x_value.get_value())
        )
        decimal2=DecimalNumber(fx_value.get_value(), font_size=30).add_updater(
            lambda t: t.set_value(fx_value.get_value())
        )
        decimal3=DecimalNumber(gx_value.get_value(), font_size=30).add_updater(
            lambda t: t.set_value(gx_value.get_value())
        )
        decimal4=DecimalNumber(hx_value.get_value(), font_size=30).add_updater(
            lambda t: t.set_value(hx_value.get_value())
        )
        decimal22=decimal2.copy()
        decimal11=decimal1.copy()
        decimal33=decimal3.copy()
        decimal44=decimal4.copy()
        my_tip=Arrow().rotate(3*PI/2).scale(0.6)
        my_tip.set_width(0.08)
        my_tip.set_height(0.8)
        my_tip2=my_tip.copy()
        my_tip3=my_tip.copy()
        my_tip4=my_tip.copy()
        my_tip.add_updater(lambda m: m.next_to(lin1.n2p(x_value.get_value()),UP,buff=0))
        my_tip2.add_updater(lambda m: m.next_to(lin2.n2p(fx_value.get_value()),UP,buff=0))
        my_tip3.add_updater(lambda m: m.next_to(lin3.n2p(gx_value.get_value()),UP,buff=0))
        my_tip4.add_updater(lambda m: m.next_to(lin4.n2p(hx_value.get_value()),UP,buff=0))
        decimal1.add_updater(lambda t: t.next_to(my_tip,UP,buff=0.2))
        decimal2.add_updater(lambda t: t.next_to(my_tip2,UP,buff=0.2))
        decimal3.add_updater(lambda t: t.next_to(my_tip3,UP,buff=0.2))
        decimal4.add_updater(lambda t: t.next_to(my_tip4,UP,buff=0.2)) 
        self.play(Create(my_tip),Create(decimal1))
        self.play(Create(my_tip2),Create(decimal2))
        self.play(Create(my_tip3),Create(decimal3))
        self.play(Create(my_tip4),Create(decimal4))
        self.wait()
        time=0
        FARADAY=VGroup(
            Text('Faraday:'),
            decimal11,
        ).arrange(RIGHT,buff=0.14)
        AVOGRADO=VGroup(
            Text('N° de electrones:'),
            decimal22
        ).arrange(RIGHT,buff=0.1)
        FUENTES=VGroup(
            Text('Fuentes:'),
            decimal33
        ).arrange(RIGHT,buff=0.1)
        AANI=VGroup(
            Text('Años:'),
            decimal44
        ).arrange(RIGHT,buff=0.1)
        myConstants=VGroup(FARADAY,AVOGRADO,FUENTES,AANI).arrange(RIGHT,buff=0.4).to_edge(DOWN,buff=0.14)
        FARADAY[0].scale(0.6)
        AVOGRADO[0].scale(0.6)
        FUENTES[0].scale(0.6)
        AANI[0].scale(0.6)
        myConstants.set_width(config['frame_width'])
        self.play(Write(myConstants))
        while time<10:
            my_time=.5
            time+=my_time
            random1=np.random.uniform(-1,1)
            random2=np.random.uniform(-1,1)
            random3=np.random.uniform(-1,1)
            random4=np.random.uniform(-1,1)
            self.play(
                x_value.animate.set_value(6+random1),
                decimal1.animate.set_value(6+random1),
                fx_value.animate.set_value(1.6+random2),
                decimal2.animate.set_value(1.6+random2),
                decimal11.animate.set_value(random1),
                gx_value.animate.set_value(1.2+random2),
                decimal22.animate.set_value(random2),
                decimal33.animate.set_value(random3),
                hx_value.animate.set_value(1.6+1.2+random2+random3),
                decimal4.animate.set_value(1.6+1.2+random2+random3),
                decimal44.animate.set_value(random2+random3),
            run_time=my_time,rate_functio=smooth)
        self.wait()
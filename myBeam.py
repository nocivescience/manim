from manim import *
import operator as op
class myBeam(Scene):
    def construct(self):
        myPoisson=self.getPoisson()
        myDot=self.getBeamAnim(myPoisson)
        myDot.add_updater(lambda t,dt: self.updateMoving(t,myPoisson,dt))
        self.add(myPoisson,myDot)
        self.wait(12)
    def getBeamAnim(self,rectangles):
        dot=Dot()
        dot.scale(0.5)
        dot.center=config['frame_width']/2*LEFT
        dot.velocity=15
        return dot
    def getPoisson(self):
        myRectangles=VGroup()
        for color in [RED,YELLOW,BLUE,GREEN,PURPLE]:
            myRectangle=Rectangle(color=color,fill_opacity=0.4,width=1,height=3).set_stroke(width=2)
            myRectangles.add(myRectangle)
        myRectangles.arrange(RIGHT,buff=0.3)
        return myRectangles
    def updateMoving(self,myFlash,myRectangles,dt):
        myFlash.center[0]+=myFlash.velocity*dt
        for i in range(len(myRectangles)):
            dist=abs(myFlash.get_center()[0]-myRectangles[i].get_center()[0])
            myFlash.proof=dist<0.5
            if myFlash.proof:
                myFlash.match_color(myRectangles[i])
            else:
                myFlash.set_color(WHITE)
        if abs(myFlash.center[0])+myFlash.radius>config['frame_width']/2:
            myFlash.center[0]=np.sign(myFlash.center[0])*(config['frame_width']/2)
            myFlash.velocity*=-1*op.mul(np.sign(myFlash.velocity),np.sign(myFlash.center[0]))
        myFlash.move_to(myFlash.center)
        return myFlash
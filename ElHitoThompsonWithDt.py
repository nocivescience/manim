from manim import *
class MyThompsonRay(Scene):
    def construct(self):
        myFlash=VMobject()
        myFlash.set_color(TEAL)
        myFlash.set_stroke(width=1)
        myFlash.center=config['frame_width']/2*LEFT
        myFlash.set_points_smoothly([config['frame_width']/2*LEFT,config['frame_width']/2*RIGHT/2+UP])
        myFlash.move_to(myFlash.center)
        myFlash.add_updater(self.updateRay)
        self.add(myFlash)
        self.wait(3)
    def updateRay(self,ray,dt):
        ray.center[0]+=8*dt
        if ray.center[0]>config['frame_width']/2:
            ray.center=config['frame_width']/2*LEFT
        ray.move_to(ray.center)
        return ray

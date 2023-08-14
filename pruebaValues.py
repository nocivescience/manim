class MoveAlongPathWithRotation(Scene):
    def get_pending(self,path,proportion,dx=0.01):
        if proportion < 1:
            coord_i = path.point_from_proportion(proportion)
            coord_f = path.point_from_proportion(proportion+dx)
        else:
            coord_i = path.point_from_proportion(proportion-dx)
            coord_f = path.point_from_proportion(proportion)
        line = Line(coord_i,coord_f)
        angle = line.get_angle()
        return angle

    def construct(self):
        # PATH
        path = Line(LEFT*5, RIGHT*5, stroke_opatity=0.5)
        path.points[1] += UP * 4
        path.points[2] += DOWN * 4
        start_angle = self.get_pending(path, 0)
        # TRIANGLE
        triangle = Triangle().set_height(0.5)
        triangle.move_to(path.get_start())
        triangle.rotate(- PI / 2)
        triangle.save_state()
        triangle.rotate(start_angle, about_point=triangle.get_center())

        def update_rotate_move(mob,alpha):
            triangle.restore()
            angle = self.get_pending(path,alpha)
            triangle.move_to(path.point_from_proportion(alpha))
            triangle.rotate(angle, about_point=triangle.get_center())

        self.add(triangle,path)
        self.play(
                UpdateFromAlphaFunc(triangle,update_rotate_move),
                run_time=4
            )
        self.wait()

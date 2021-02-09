from manimlib.imports import *

class Space(Scene):
    def construct(self):
        
        text1 = TextMobject(r"{\huge \textit{Orbit}}")
        EarthB=Dot(radius=2, stroke_width=2,color=BLUE)
        EarthA=Dot(radius=0.07, color=BLUE)
        Sun=Dot(radius=0.5, color=YELLOW)
        orbit=Circle(radius=2, colour=WHITE, stroke=0.5, opacity=0.1)
        
        self.wait(2)
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1,EarthB))
        self.wait(1)
        EarthP = np.array([2,0,0])
        self.play(Transform(text1,EarthA))
        self.play(text1.move_to, EarthP ,run_time=2) 
        self.play(FadeIn(Sun))
        
        self.play(GrowFromCenter(orbit))
        self.add(text1)
        for i in range(10):
            self.play(MoveAlongPath(text1, orbit), rate_func=linear, run_time=3)
            i=+1
        g = VGroup(Sun, text1, orbit)
        self.play(FadeOut(g))
        #self.play(FadeOut(EarthA))
        #self.play(FadeOut(EarthB))
        #self.play(FadeOut(text1))
        
        '''
        Stars appear to mimic space, want 72 in random spots
        '''
        
        
        
        # generate random star positions
        #stars = Dot(radius=0.02, color=WHITE)
        #starsP = np.zeros(2,72)
        #for i in range(0,starsP.shape[0]):
        #    for j in range(0,starsP.shape[0]):
        #        starsP[i,j] = [np.random.uniform(-8,8), np.random.uniform(-4,4)]
        
        
        '''
        Place stars in positions 
        > How to use one object multiple times
        > Appear at once?
        '''
        
        #for i in range(0,starsP.shape[0]):
        #       for j in range(0,starsP.shape[0]):
        #           stars.move
        
        #square = Square(side_length = 20)
        #square.set_color(ORANGE)
        #self.play(GrowFromCenter(square, run_time=3))
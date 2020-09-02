from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.core.window import Window

Window.clearcolor = (.6,) * 4

waveeffect = '''
/*These few lines of glsl are just some default fragment shader Kivy uses.*/
#ifdef GL_ES
    precision highp float;
#else
    precision mediump float;
#endif
/* Outputs from the vertex shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* uniform texture samplers */
uniform sampler2D texture0;
/*end defaults*/

/*My code*/
uniform float a; //a variable is fed from python code

void main(){
    float x = gl_FragCoord.x;
    float y = gl_FragCoord.y;
    /*A simple linear inequality here. Here the <= operator is used which makes the bottom area have the special effect. Change the operator to either "==" or ">=" to see different effect*/
    if (y <= 400.+40.*sin(radians(a+x*.75))){
        gl_FragColor = vec4(.2, .3, .7, 1.)*frag_color*texture2D(texture0, tex_coord0);
    }
    else{
    //the default gl_FragColor output that Kivy uses
        gl_FragColor = frag_color*texture2D(texture0, tex_coord0);
    }
}
'''


class WidTest(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        self.canvas = RenderContext(use_parent_projection=True, use_parent_modelview=True)
        self.canvas.shader.fs = waveeffect
        BLUE = .1, .2, .6
        with self.canvas:
            Color(*BLUE)
            Rectangle(size=self.size, pos=self.pos)
        Clock.schedule_interval(self.update, 1 / 50)

    def update(self, dt):
        self.counter += 1
        self.canvas["a"] = self.counter % 500000.


wid = Widget()
test = WidTest(size=Window.size)
wid.add_widget(test)
runTouchApp(wid)

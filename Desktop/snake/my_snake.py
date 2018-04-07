from tkinter import *
from random import randint
import time

class Ball:
    def __init__(self,canvas,snake,score,color):
        self.canvas=canvas
        self.snake=snake
        self.score=score
        self.id=canvas.create_oval(10,10,30,30,fill=color,outline=color)
        self.respawn()
    def respawn(self):
        xd=randint(1,27)*20
        yd=randint(1,16)*20
        self.canvas.coords(self.id,-10,-10,10,10)
        self.canvas.coords(self.id)
        self.canvas.move(self.id,xd,yd)
        self.canvas.coords(self.id)
        for resp in range(0,snake.length-1):
            if self.canvas.coords(self.id) == snake.coords[resp]:
                self.respawn()
    def pose(self):
        pos = self.canvas.coords(self.id)
        pose=self.canvas.coords(self.snake.id)
        if pos[0] >= pose[0] and pos[2] <= pose[2]:
            if pos[1] >= pose[1] and pos[3] <= pose[3]:
                ball.respawn()
                score.hit()
                snake.length=snake.length+1
                snake.space.append(snake.length)
                posit=snake.canvas.coords(snake.id)
                snake.coords.append(posit)
                return True
        return False
    
class Snake:
    def __init__(self,canvas,score,color):
        self.canvas=canvas
        self.score=score
        self.id=canvas.create_rectangle(10,10,30,30,fill=color,outline=color)
        self.canvas.move(self.id,260,140)
        self.x=0
        self.y=0
        self.started=False
        self.cuz=0
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
        self.canvas.bind_all('<Button-1>',self.start)
        self.move=None
        self.length=1
        self.coords=[]
        self.space=[]
        self.maxx=0
    def start(self,evt):
        self.started=True
        rand=randint(0,3)
        if rand == 0:
            self.y=-20
            self.x=0
            self.move=0 #up 0
        if rand == 1:
            self.y=20
            self.x=0
            self.move=1 #down 1
        if rand == 2:
            self.x=20
            self.y=0
            self.move=2 #right 2
        if rand == 3:
            self.x=-20
            self.y=0
            self.move=3 #left 3
    def turn_up(self,evt):
        if self.move != 1:
            self.y=-20
            self.x=0
            self.move=0 #up 0
    def turn_down(self,evt):
        if self.move != 0:
            self.y=20
            self.x=0
            self.move=1 #down 1
    def turn_right(self,evt):
        if self.move != 3:
            self.x=20
            self.y=0
            self.move=2 #right 2
    def turn_left(self,evt):
        if self.move != 2:
            self.x=-20
            self.y=0
            self.move=3 #left 3
    def teleport(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        x1=pos[0]
        y1=pos[1]
        x2=pos[2]
        y2=pos[3]
        if pos[0] < 10:
            x1right=x1+540
            x2right=x2+540
            self.canvas.coords(self.id,x1right,y1,x2right,y2)
        if pos[1] < 10:
            y1down=y1+320
            y2down=y2+320
            self.canvas.coords(self.id,x1,y1down,x2,y2down)
        if pos[2] > 560:
            x1left=x1-540
            x2left=x2-540
            self.canvas.coords(self.id,x1left,y1,x2left,y2)
        if pos[3] > 330:
            y1up=y1-320
            y2up=y2-320
            self.canvas.coords(self.id,x1,y1up,x2,y2up) #teleport
    def fragment(self):
        posit=self.canvas.coords(self.id)
        self.coords.append(posit)
        color='black'
        if self.length<len(self.coords):
            for gh in range(0,self.length):#!!!!!!!!!
                del self.coords[0]
            for t in range(0,self.length-1):
                fpos=self.canvas.coords(self.space[t])
                self.coords.append(fpos)
        for num_of_frag in range(self.maxx,self.length-1):
            if styled==0:
                color='white'
            if styled==1:
                color='black'
            if styled==2:
                color='black'                
            self.space[self.length-2]=canvas.create_rectangle(self.coords[num_of_frag],fill=color,outline=color)
            self.maxx=self.maxx+1 #create the frag number

        for move_of_frag in range(0,self.length-1):
            self.canvas.coords(self.space[move_of_frag],self.coords[move_of_frag]) #move the frag
            #delete not using code
    def cus(self):
        poscus=self.canvas.coords(self.id)
        for cuss in range(0,self.length-1):
            if poscus == self.coords[cuss]:
                print("FUCK")
                self.cuz=1
            
class Score:
    def __init__(self,canvas,color):
        self.score=0
        self.canvas=canvas
        self.id=canvas.create_text(120,379,text=self.score,font=('Helvetica',20),fill=color,anchor=W)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text=self.score)
        
def ask_for_style():
    style=str(input("Input style of game(negative,classic,standard):"))
    if style == "negative" or style == "Negative" or style == "n":
        return 0
    if style == "classic" or style == "Classic" or style == "c":
        return 1
    if style == "standard" or style == "Standard" or style == "s":
        return 2
    else:
        print('ERROR')
        
styled=ask_for_style()
if styled==0:
    colormenu='white'
    text='black'
    colorball='white'
    colorcanvas='black'
if styled==1:
    colormenu='black'
    text='white'
    colorball='black'
    colorcanvas='white'       
if styled==2:
    colormenu="blue"
    text = 'white'
    colorball= 'blue'
    colorcanvas='white'
    
tk=Tk()
tk.title('Snake')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width=560,height=400,bd = 0,highlightthickness = 0,bg=colorcanvas)
canvas.pack()
lbl=Label(tk, text='SCORE:', font=("Helvetica", 20),bg=colormenu,fg=text)
lbl.place(x=10,y=360)
design=canvas.create_rectangle(-3,330,560,403,fill=colormenu)
score=Score(canvas,text)
snake=Snake(canvas,score,colorcanvas)
ball=Ball(canvas,snake,score,colorball)
design=canvas.create_rectangle(-3,330,560,360,fill=colormenu,outline=colormenu)
design1=canvas.create_rectangle(-3,0,10,330,fill=colormenu,outline=colormenu)
design3=canvas.create_rectangle(550,0,560,330,fill=colormenu,outline=colormenu)
design2=canvas.create_rectangle(-3,-3,560,10,fill=colormenu,outline=colormenu)
fg=0

while 1:
    if snake.started==True and snake.cuz!=1:
        if fg == 0:
            snake.length=snake.length+1
            snake.space.append(snake.length)
            posit=snake.canvas.coords(snake.id)
            snake.coords.append(posit)
            fg=fg+1
        snake.teleport()
        ball.pose()
        snake.cus()
        snake.fragment()
    if score.score==432:
        lbl1=Label(tk, text='''You won
Score: %s'''%(score.score), font=("Helvetica", 75),fg=colormenu,bg=colorcanvas)
        lbl1.place(x=26,y=28)        
    if snake.cuz==1:
        lbl1=Label(tk, text='''Game over
Score: %s'''%(score.score), font=("Helvetica", 75),fg=colormenu,bg=colorcanvas)
        lbl1.place(x=26,y=28)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)
    

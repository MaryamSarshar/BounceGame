from tkinter import *
import time
import random
tk= Tk()
tk.title("Bounce Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=400 , height= 400,bd = 0,highlightthickness=0,bg="grey")
canvas.grid(row=0,column=0)
tk.update()




class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,25,25,fill =color)
        self.canvas.move(self.id ,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
        

    def hit_paddle(self,pos):
        paddl_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddl_pos[0] and pos[0] <= paddl_pos[2]:
            if pos[3] >= paddl_pos[1] and pos[3] <= paddl_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True 
        return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
               
        if self.hit_paddle(pos) == True:
            self.y = -5
        if pos[0] <=0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

  
    
    def delet_ball(self):
        self.canvas.delete(self.id)


class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.started = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.canvas.bind_all("<Button-1>",self.start_game)
        

    def turn_left(self,event):
        self.x = -3
    
    def turn_right(self,event):
        self.x = 3
    
    def start_game(self,event):
        self.started =True
        

    def delet_paddle(self):
        self.canvas.delete(self.id)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -1


class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(350,10,text=self.score,fill=color,font=1)

    def hit(self):
        self.score +=1
        self.canvas.itemconfig(self.id,text = self.score)
    



score = Score(canvas,"green")
paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,score,"red")
# ball2 = Ball(canvas,paddle,"yellow")

score_on_screen = ("Score "+str(score.score)+"!")

game_over = canvas.create_text(200,200,text='Game Over!!',fill = "black",font =("Times",22),state ="hidden")
final_scor = canvas.create_text(200,230,text= score_on_screen,fill = "purple",font =2,state ="hidden")
while 1:
    if ball.hit_bottom == False and paddle.started == True: #and ball2.hit_bottom == False:
        ball.draw()
        # ball2.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over,state = "normal")
        canvas.itemconfig(final_scor,state = "normal", text="Score "+str(score.score)+"!")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    

# def game_over():
#     tk.destroy()
#     top.deiconify()
# top = Toplevel()
# canvas = Canvas(top, width=400 , height= 400,bd = 0,highlightthickness=0,bg="grey")
# canvas.grid(row=0,column=0)
# game_over_but = Button(top,text = " Game Over! ",command = game_over,fg="red",font=2)
# game_over_but.grid(row=0,column=0)
# tk.withdraw()
# paddle.delet_paddle()
# ball.delet_ball()
# # ball2.delet_ball()

# # while 1:
#     tk.update_idletasks()
#     tk.update()
#     time.sleep(0.01)


    













# Expanding circle by timer



import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def time_handler() : 
    global radius
    if radius <= 10 :
        radius += 2
    elif radius > 10 :
         radius -= 1    
    
    
# Draw handler
def draw(canvas) :
    canvas.draw_circle([200,200],radius,12,"Red")
    canvas.draw_circle([400,400],radius,12,"Red")
    canvas.draw_circle([200,400],radius,12,"Red")
    canvas.draw_circle([400,200],radius,12,"Red")
        
# Create frame and timer
frame = simplegui.create_frame("timer",500,500)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000,time_handler)

# Start timer
frame.start()
timer.start()


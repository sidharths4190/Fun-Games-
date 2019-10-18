import simplegui 

counter = 0
count = 5

# Timer handler
def tick():
    global counter
    if counter < 60 :
        counter += 1
    
    elif counter == 60 :
        counter = 0
        counter += 1
    
    
def tickb():
    global count
    if count < 100 :
        count += 1
    
    elif count == 100 :
        count = 0
        count += 1
     
    
# Event handlers for buttons 
def start() :
    timer.start()
    time.start()
    
def stop() :
    timer.stop()
    time.stop()
    
def reset() :
    global counter
    global count
    counter = 0
    count = 0
    timer.stop()
    time.stop()
    
def draw(canvas) :
    canvas.draw_text(str(counter) +":" +str(count),[200,200],50,"Red")
    

        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 400, 400)
timer = simplegui.create_timer(1000, tick)
time = simplegui.create_timer(10, tickb)
frame.add_button("START",start,70)
frame.add_button("STOP",stop,70)
frame.add_button("RESET",reset,70)
frame.set_draw_handler(draw)

# Start timer
frame.start()
time.start()
timer.start()

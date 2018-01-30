'''
Carton-Fulcrum Torque Vector (CFTV) is a program that visualises an egg carton atop a fulcrum. It calculates the direction and the magnitude, shown as the resultant torque vector 
'''

carton_w = 50 # The carton width, in # of sockets
carton_h = 2 # the carton height, in # of sickets
cartonsize = carton_h*carton_w
carton = [int(round(random(0, 1))) for x in range(cartonsize)] #generate a random carton
eggsize = 40 # arbitrary adjustable egg diameter, in pixels
socketsize = eggsize+(eggsize/4) # the size of the egg socket
egg_weight = 50*9.81 # the average egg weighs about 50g
torques = [x for x in range(cartonsize)]
carton = [round(random(0, 1)) for x in range(cartonsize)]
egg_y = [socketsize*floor(y/carton_w) for i, y in enumerate(range(cartonsize))]
egg_x = [socketsize*(x%(cartonsize/carton_h)) for x in range(cartonsize)]
inch_meter = 0.0254 # inch to meter ratio
conv = socketsize/2
pixel_inch = socketsize/2 # pixel to inch ratio. A carton is about a foot long, / by six to get 2 inches per egg socket, each socket is divided by two to get pixel>inch. 25 for our purposes. 
fulltq= []
fulc_x_coord = socketsize*(carton_w/2) + socketsize/2 # These Two
fulc_y_coord = socketsize*(carton_h/2) + socketsize/2   # Lines will create a fulcrum in the middle of the carton
window_x = int(socketsize*(carton_w)*2) # set the window size
window_y = int(socketsize*(carton_h)*(1 + carton_w+1/(carton_h))) # set the window size

def draw():
    if keyPressed:     #
        if key == 'r': # press R to run a nother simulation. 
            setup()    #
    
def setup():
    strokeWeight(2)
    fulltq = []
    torques = [x for x in range(cartonsize)]
    size(window_x, window_y)
    noStroke()
    textAlign(CENTER)
    textSize(14) # set the font size
    background(155, 110, 90) # set the background to brown
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    carton = [round(random(0, 1)) for x in range(cartonsize)] #  change this to change how the carton is generated ~~~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    for i, ex in enumerate(egg_x): # iterate through the egg coordinate list and create the sockets
            x = egg_x[i]
            y = egg_y[i]
            fill(170)
            ellipse(ex+socketsize, y+socketsize, socketsize, socketsize)
    for ind, egg in enumerate(carton): # iterate through the carton list and create the eggs where they have been placed by the carton list comprehension
        if egg == 1:
                fill(255)
                ellipse(egg_x[ind]+socketsize, egg_y[ind]+socketsize*0.9, eggsize, eggsize+int(eggsize/5))
    
    #For each egg in the carton, calculate the torque based on fulcrum position
    x2 = fulc_x_coord
    y2 = fulc_y_coord
    for ind, space in enumerate(carton):
        x1 = egg_x[ind]+socketsize
        y1 = egg_y[ind]+socketsize
        torq = calc_torque(egg_weight, x2, y2, x1, y1)
        direction = [torq*((x2-x1)),torq*((y2-y1))] # torque x the distance vector
        if space == 1: # if the space in the list is a 1 (indicating an egg)
            torques[ind] = [torq*(x2-x1),torq*(y2-y1)] # add the calculated torque to the torque list
        else:
            torques[ind] = 0
            
    # Generate the visual torque vectors being going through the list and making them into coordinate vectors
    textAlign(LEFT)
    text("Torque Vectors: ", socketsize*(carton_w+1), socketsize)
    torq_x = 0
    torq_y = 0
    for i, tq in enumerate(torques):
            torq = calc_torque(egg_weight, fulc_x_coord, fulc_y_coord, egg_x[ind]+socketsize, egg_y[ind]+socketsize)
            print(tq)
            if tq != 0:
                    fulltq.append([tq[0]/torq, tq[1]/torq])
    count = 0
    for i, t in enumerate(fulltq):
        count = i
        if t != 0:
            fill(255)
            sb = [(-1)*t[0], (-1)*t[1]]
            text("" + str(sb), socketsize*(carton_w+1), socketsize+15+15*i)
            arrow(fulc_x_coord, fulc_y_coord, fulc_x_coord-t[0], fulc_y_coord-t[1])
    
    # Add the vector components to obtain resultant torque vectors and draw torque vector arrows. 
    res_x = 0
    res_y = 0
    ox = socketsize*(carton_w+1)
    oy = (socketsize*carton_h)*(cartonsize/carton_w)
    for indx, t in enumerate(fulltq):
        if indx == 0:
            res_x = t[0]
            res_y = t[1]
        else: 
            res_x = t[0] + res_x
            res_y = t[1] + res_y
    res_tq_vec = (res_x, res_y)
    arrow(socketsize*(carton_w+1), (socketsize*carton_h)*(cartonsize/carton_w), socketsize*(carton_w+1)-res_x, (socketsize*carton_h)*(cartonsize/carton_w)-res_y, 0, 255, 0)
    strokeWeight(5)
    arrow(fulc_x_coord, fulc_y_coord, fulc_x_coord-res_x, fulc_y_coord-res_y, 0, 255, 0)
    strokeWeight(2)
    textAlign(LEFT)
    fill(255)        
    textSize
    text("Resultant Vector: ", socketsize*(carton_w+1), socketsize+30+15*(count+1))
    b = [(-1)*res_tq_vec[0], (-1)*res_tq_vec[1]]
    text("" + str(b), socketsize*(carton_w+1), socketsize+30+15*(count+2))
    fill(0)
    
    textAlign(CENTER)
    # Create the Fulcrum
    fill(0)
    ellipse(fulc_x_coord, fulc_y_coord, 5, 5)
    text("Fulcrum", fulc_x_coord, fulc_y_coord + socketsize/4)
    fill(255)
    textAlign(LEFT)

            

def arrow(x1, y1, x2, y2, col1=255, col2=0, col3=0):
    '''
    Basic function for drawing an arrow
    x1: x of start point
    y1: y of start point
    x2: x of end point
    y2: y of endpoint
    col1, 2, 3: rgb color params for arrow
    '''
    stroke(col1, col2, col3)
    fill(col1, col2, col3)
    line(x1, y1, x2, y2)
    pushMatrix()
    translate(x2, y2)
    a = atan2(x1-x2, y2-y1)
    rotate(a)
    line(0, 0, -5, -5)
    line(0, 0, 5, -5)
    popMatrix()
    noStroke()

     

def calc_torque(weight, fulc_y, fulc_x, pos_y, pos_x):
    '''
    A function for calculating torque
    param weight: the weight of an object
    param fulc_y: the y coord of the fulcrum
    param fulc_x: the x coord of the fulcrum
    param pos_y: the y coord of the egg
    param pos_x: the x coord of the egg
    returns torque: the torque of the system
    '''
    '''
    if pos_x < fulc_x_coord:
        pos_x = 0-pos_x
    if pos_y > fulc_y_coord:
        pos_y = 0-pos_y
    '''
    distance = sqrt(sq(pos_x - fulc_x) + sq(pos_y - fulc_y)) # distance using distance formula 
    torque = weight*distance*pixel_inch*inch_meter # torque using torqe formula
    return torque
# HENRY TU
# main.py
# PAINT PROJECT ICS3U MIDTERM
# MICROSOFT PAINT CLONE


import tkinter as tk
from random import *
from tkinter import filedialog
import os
from pygame import *
import platform
from math import *


# Setup for loading files
root = tk.Tk()  # this initializes the Tk engine
root.withdraw()  # by default the Tk root will show a little window. This
# just hides that window

# Stamp import
stamp8 = image.load("stamps/stamp8.png")  # Windows logo

# Icon
display.set_icon(stamp8)

# Initialize display
screen = display.set_mode((1280, 700))

# Gets the size of the screen so window can be centerd
inf = display.Info()
w, h = inf.current_w, inf.current_h

# Sets it to the center
os.environ['SDL_VIDEO_WINDOW_POS'] = str(w // 2 - 640) + "," + str(h // 2 - 350)

# Font import
font.init()
ubuntuFont = font.Font("fonts/Lato.ttf", 30)
ubuntuFontSmall = font.Font("fonts/Lato.ttf", 15)
timesNewRomanFont = font.Font("fonts/TimesNewRomans.ttf", 30)
comicSansFont = font.Font("fonts/ComicSans.ttf", 30)

# Essential UI import
wall1 = image.load("images/wall1.jpg")
colourPicker = image.load("images/col.jpg")  # Colour Picker
wallpaper = image.load("images/wallpaper.jpg")
pepe = transform.scale(image.load("images/pepe.png"), (80, 80))

snowden = transform.scale(image.load("images/snowden.jpg"), (300, 169))

# Menu icons
menuIcon = transform.scale(image.load("icons/menu.png"), (30, 30))
textIcon = transform.scale(image.load("icons/text.png"), (30, 30))

redoIcon = transform.scale(image.load("icons/redo.png"), (30, 30))
undoIcon = transform.scale(image.load("icons/undo.png"), (30, 30))
lowVolIcon = transform.scale(image.load("icons/lowVol.png"), (30, 30))
highVolIcon = transform.scale(image.load("icons/highVol.png"), (30, 30))
muteVolIcon = transform.scale(image.load("icons/mute.png"), (30, 30))
filterIcon = transform.scale(image.load("icons/filter.png"), (30, 30))
shapesIcon = transform.scale(image.load("icons/shapes.png"), (30, 30))
brushIcon = transform.scale(image.load("icons/brush.png"), (30, 30))

stickerIcon = transform.scale(image.load("icons/sticker.png"), (30, 30))

saveIcon = transform.scale(image.load("icons/save.png"), (30, 30))
saveasIcon = transform.scale(image.load("icons/saveas.png"), (30, 30))
newIcon = transform.scale(image.load("icons/new.png"), (30, 30))
importIcon = transform.scale(image.load("icons/import.png"), (30, 30))
aboutIcon = transform.scale(image.load("icons/about.png"), (30, 30))
helpIcon = transform.scale(image.load("icons/help.png"), (30, 30))

# Minor icons
pickerIcon = transform.scale(image.load("icons/picker.png"), (30, 30))
palatteIcon = transform.scale(image.load("icons/palette.png"), (30, 30))

# Brush menu icons
brushTool = transform.scale(image.load("icons/brushTool.png"), (40, 40))
eraserTool = transform.scale(image.load("icons/eraserTool.png"), (40, 40))
spraypaintTool = transform.scale(image.load("icons/spraypaintTool.png"), (40, 40))
penTool = transform.scale(image.load("icons/penTool.png"), (40, 40))
paintBucketTool = transform.scale(image.load("icons/paintBucketTool.png"), (40, 40))
markerTool = transform.scale(image.load("icons/markerTool.png"), (40, 40))

# Filter menu icons
pixelFilter = transform.scale(image.load("icons/pixelFilter.png"), (40, 40))
invertFilter = transform.scale(image.load("icons/invertFilter.png"), (40, 40))
blackwhiteFilter = transform.scale(image.load("icons/blackFilter.png"), (40, 40))
threshholdFilter = transform.scale(image.load("icons/threshholdFilter.png"), (40, 40))
blurFilter = transform.scale(image.load("icons/blurFilter.png"), (40, 40))
sepiaFilter = transform.scale(image.load("icons/sepiaFilter.png"), (40, 40))

ellipseShape = transform.scale(image.load("icons/ellipseShape.png"), (40, 40))
circleShape = transform.scale(image.load("icons/roundShape.png"), (40, 40))

rectShape = transform.scale(image.load("icons/squareShape.png"), (60, 40))
squareShape = transform.scale(image.load("icons/squareShape.png"), (40, 40))

lineShape = transform.scale(image.load("icons/lineShape.png"), (40, 40))
polygonShape = transform.scale(image.load("icons/polygonShape.png"), (40, 40))
equationShape = transform.scale(image.load("icons/curvedShape.png"), (40, 40))
triangleShape = transform.scale(image.load("icons/triangle.png"), (40, 40))


# Stamp import
stampList = []
stampCroppedList = []
for i in range(1,9): #Cycles through the stamp names
    stampList.append(image.load(("stamps/stamp%s.png"%i)))  # Word logo
    stampCroppedList.append(transform.scale(image.load(("stamps/stamp%s.png"%i)), (40, 40)))


# Toggle buttons
buttonOff = image.load("icons/switchOff.png")
buttonOn = image.load("icons/switchOn.png")

fileName = "Untitled"  # File name used for saving

display.set_caption("Mike-ro-soft Paint 2.0 ")  # Caption at the top of the window


# FPS Clock
clock = time.Clock()

# Scale the photos
wall1 = transform.scale(wall1, (500, 250))
wallpaper = transform.scale(wallpaper, (1280, 720))
colourPicker = transform.scale(colourPicker, (500, 500))
colourPicker = transform.rotate(colourPicker, 270)

# Initial Value for smooth lines
mxo, myo = 0, 0

# Location of mouse on down
mxs, mys = 0, 0


# Generating rainbows, uses these values to cycle through colours
rainCycle = 1
rainRate = 0.05

# Flags
paletteVisible = False  # Colour palette visibility
polygonFill = False  # Fill shapes
drawnUI = False  # Whether the UI elements we already drawn
imageToBeLoaded = False  # Whether a photo is to be put on the canvas, used for loading
blood = False  # Blood spray paint selected
snapping = False  # Mouse snapping
drawerVisible = False  # Left drawer
menuOpen = False  # If any window is open
drawnDrawer = False  # Makes sure drawer is only drawn once
aboutVisible = False  # ABout window
savePromptVisible = False  # Save window
graphPromptVisible = False
helpPromptVisible = False
actionMade = False  # Whether an action has been made since last save
roundLine = False  # Whether line tool makes lines with round ends
rainbow = False #Rainbow paint enabled

nextAction = None  # When a command to clear canvas, what is the next step

# Stores information for polygon
polygonList = []

# Checks OS
if platform.system() == "Windows":
    musicEnabled = True  # If music is enabled, doesnt work on linux
else:
    musicEnabled = False

# Import music

musicList=[]
for i in range(8,0,-1):
    musicList.append("audio/song%i.ogg"%(i))

shuffle(musicList) #Randomize music

if musicEnabled: #Cycles through music
    mixer.init()
    mixer.music.load(musicList.pop())
    mixer.music.queue(musicList.pop())
    mixer.music.set_endevent(USEREVENT)
    mixer.music.play()
    volume = 1



# Current screen
currentScreen = "Menu"

# Sets initial cursor size
cursorSize = 4

# DRAWING AREA
#Rects
paletteMiniRect = Rect(1025, 535, 240, 120)
paletteRect = Rect(390, 100, 500, 500)
helpPromptRect = Rect(365, 250, 550, 200)
aboutWindowRect = Rect(365, 280, 550, 140)
canvasRect = Rect(20, 80, 960, 600)
wideCanvasRect = Rect(0, 50, 1000,
                      700)  # larger rect containing area around canvas to allow for mouse to transition off
drawArea = screen.subsurface(canvasRect)  # Establishes Drawing area
paletteSurface = screen.subsurface(390, 100, 500, 500)

# Stores previous frames in case user wants to undo something
undoList = []
redoList = []

# File used for custom cursor
customCursorImage = None

# Colours
BLACK = (0, 0, 0)
BACKGROUND = (186, 186, 186)  # BG colour
WINDOWS = (55, 58, 66)  # Colour of the windows
SIDEBAR = (234, 234, 234)
BUTTONCOL = (225, 225, 225)
BUTTONHOVER = (0, 166, 204)
BUTTONCLICK = (198, 198, 198)

# Button rects
paletteButtonRect = Rect(1026, 651, 238, 48)
paletteCloseButtonRect = Rect(390, 610, 500, 48)
colourPickerButtonRect = Rect(1146, 481, 118, 48)
colourPreviewRect = Rect(1025, 480, 120, 50)
sliderRect = Rect(1020, 380, 250, 60)

# Start and load buttons
startNewFileButton = Rect(390, 510, 500, 48)
loadFileButton = Rect(390, 450, 500, 48)

# Text menu buttons
ubuntuFontBox = Rect(1020, 140, 250, 60)
timesNewRomanFontBox = Rect(1020, 210, 250, 60)
comicSansFontBox = Rect(1020, 280, 250, 60)

textContent = ""

# Allows the user to see how much work will be lost if not saved
startTime = None  # Tells timer to reset next time action is made
actionsMade = 0

# Menu index
menuIndex = "Brush"
menuIndexCode = {"LeftMenu": 0, "Blank1": 1, "Blank2": 2, "Blank3": 3, "Blank4": 4, "Blank5": 5, "Blank6": 6,
                 "Brush": 7, "Sticker": 8, "Shapes": 9, "Text": 10, "Filters": 11, "Blank12": 12, "VolMute": 13,
                 "VolDown": 14, "VolUp": 15, "Blank16": 16, "Blank17": 17, "Blank18": 18, "Undo": 19, "Redo": 20}

# Contents of help
# First line
helpList1 = {"Brush": "Make lines that follow the cursor", "Spray Paint": "Draw random dots",
             "Pen": "Draw lines with sharp edge", "Eraser": "Clear a region of marks",
             "Colour Picker": "Select colours from the canvas", "Stamp 1": "Click or drag on canvas to draw",
             "Stamp 2": "Click or drag on canvas to draw", "Stamp 3": "Click or drag on canvas to draw",
             "Stamp 4": "Click or drag on canvas to draw", "Stamp 5": "Click or drag on canvas to draw",
             "Stamp 6": "Click or drag on canvas to draw", "Stamp 7": "Click or drag on canvas to draw",
             "Stamp 8": "Click or drag on canvas to draw", "Rectangle": "Click and drag to draw rectangles",
             "Ellipse": "Click and drag to draw ellipses", "Line": "Click and drag to draw lines",
             "Bucket": "Click region to fill", "Marker": "Draw lines with transparency",
             "Text": "Type to stamp text to canvas", "Circle": "Click and drag to draw circles",
             "Square": "Click and drag to draw squares", "Stamp Custom": "Use a custom image to draw",
             "Polygon": "Draw Custom Shapes", "Pixelate": "Simplifies the canvas by",
             "Threshhold": "Snaps to black or white", "BlackWhite": "Converts the canvas to greyscale",
             "Invert": "Inverts the RGB values", "Blur": "Applies a blur effect", "Sepia": "Applies a brown tint",
             "Blood": "Adds a dripping effect to spray paint", "Snapping": "Snaps the cursor to a preset",
             "FillPoly": "Fills polygon as it is being drawn", "RoundLine": "Round line end caps",
             "Rainbow": "Generate rainbows for colour","Graph":"Lines from given equations",
             "Triangle":"Generate triangles from points"}

# Second line
helpList2 = {"Brush": "Scroll to change cursor sizes", "Spray Paint": "Scroll to change cursor size",
             "Pen": "Scroll to change cursor size", "Eraser": "Scroll to change cursor size", "Colour Picker": "",
             "Stamp 1": "Scroll to change cursor size", "Stamp 2": "Scroll to change cursor size",
             "Stamp 3": "Scroll to change cursor size", "Stamp 4": "Scroll to change cursor size",
             "Stamp 5": "Scroll to change cursor size", "Stamp 6": "Scroll to change cursor size",
             "Stamp 7": "Scroll to change cursor size", "Stamp 8": "Scroll to change cursor size",
             "Rectangle": "Select if filled in shapes menu", "Ellipse": "Select if filled in shapes menu",
             "Line": "Scrolling changes thickness", "Bucket": "", "Marker": "Scroll to change cursor size",
             "Text": "Click to place down text", "Circle": "Choose if filled in shapes menu",
             "Square": "Choose if filled in shapes menu", "Stamp Custom": "Scroll to change cursor size",
             "Polygon": "Connect line or right click to end", "Pixelate": "grouping pixels into clustors",
             "Threshhold": "depending on colour", "BlackWhite": "", "Invert": "", "Blur": "", "Sepia": "", "Blood": "",
             "Snapping": "interval", "FillPoly": "", "RoundLine": "", "Rainbow": "","Graph":"Use mouse cursor to change scale","Triangle":"",
             "Grid":""}

# Colour List for palette
currentColours = [(243, 155, 17)]

# Calculates recommended colours
for i in range(-255, 0, 14):
    # Generates gradients that will always be valid
    currentColours.append((abs(currentColours[0][0] + i), abs(currentColours[0][1] + i), abs(currentColours[0][2] + i)))

# Default tool so it doesnt crash
currentTool = "Brush"

# If hte program is still running
running = True

# Creates a translucent surface to gradially darken
backDrop = Surface((1280, 700))

# Decreases alpha
for i in range(255, 80, -6):
    screen.blit(wallpaper, (0, 0))  # Adds window wallpaper
    backDrop.set_alpha(i)  # Makes it transparent
    screen.blit(backDrop, (0, 0))  # puts the transparent backdrop
    display.flip()  # Updates

# Creates window
for i in range(0, 100, 5):
    screen.blit(wallpaper, (0, 0))  # Replaces background
    screen.blit(backDrop, (0, 0))  # Makes it dark again

    width = i * (550 / 100)  # Sets the W and H of the "window"
    height = i * (480 / 100)

    x = 640 - width // 2  # Centres the window
    y = 350 - height // 2

    # Draws the window and updates screen
    draw.rect(screen, (188, 188, 188), (x, y, width, height))
    display.flip()


# FUNCTIONS-------------------------------------------------------------------------------------



# When the canvas is to be cleared
def clear_canvas(fileName, drawArea, undoList, redoList):
    fileName = "Untitled"  # Clear file name
    drawArea.fill((255, 255, 255))  # Clear canvas

    saveAction()  # Saves the action that was just performed for undo list
    undoList = []
    undoList.append(drawArea.copy())  # Adds the screen to the list
    redoList = []  # Clears the redo list because they are no longer valid

    return fileName, drawArea, undoList, redoList


# When an action is made, run this to update cursor and undo lists
def saveAction():  # Saves the action that was just performed for undo list
    global undoList, drawArea, redoList, cursorCache, actionMade, startTime, unixTime, actionsMade

    undoList.append(drawArea.copy())  # Adds the screen to the list
    redoList = []  # Clears the redo list because they are no longer valid

    # If the mouse is clicked, the screen is recorded so that the cursor can be drawn fluidly
    cursorCache = drawArea.copy()

    actionMade = True  # So that when we close, we can check if it is saved

    actionsMade += 1

    if startTime == None:
        startTime = unixTime


# Distance formula
def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# Algorithm used to fill an area
def floodFill(mx, my, surface, fillCol):
    if canvasRect.collidepoint(mx, my):

        # List of pixels that need to be checked
        colourQueue = [(mx, my)]

        # Gets the starting colour to make sure only certain pixels are filled
        startCol = surface.get_at(colourQueue[0])

        # Ensures the colour clicked is not the fill colour
        if startCol != fillCol:

            # Runs through the list of coordinates
            while len(colourQueue) > 0:

                """
                newFill = []
                for fx, fy in colourQueue:

                    if fx < 960 and fy < 600 and surface.get_at((fx, fy)) == startCol:
                        drawArea.set_at((fx, fy), fillCol)
                        newFill += [(fx + 1, fy), (fx - 1, fy), (fx, fy + 1), (fx, fy - 1)]
                    colourQueue = newFill

                """
                # Checks if the current pixel is the target colour
                if surface.get_at(colourQueue[0]) == startCol:
                    # Sets the pixel the fill colour
                    surface.set_at((colourQueue[0]), fillCol)

                    # Checks to make sure the pixel to the left of current pixel is valid
                    if colourQueue[0][1] - 1 >= 0:
                        # Adds pixel to queue
                        colourQueue.append((colourQueue[0][0], colourQueue[0][1] - 1))

                    if colourQueue[0][1] + 1 < 600:
                        colourQueue.append((colourQueue[0][0], colourQueue[0][1] + 1))

                    if colourQueue[0][0] - 1 >= 0:
                        colourQueue.append((colourQueue[0][0] - 1, colourQueue[0][1]))

                    if colourQueue[0][0] + 1 < 960:
                        colourQueue.append((colourQueue[0][0] + 1, colourQueue[0][1]))

                # Removes coordinate from the queue
                del colourQueue[0]


# Sepia filter
def applySepia(screen):
    # Goes through every pixels
    for x in range(0, 960, 1):
        for y in range(0, 600, 1):
            # Splits up the colour into RGB components
            inputRed = screen.get_at((x, y))[0]
            inputGreen = screen.get_at((x, y))[1]
            inputBlue = screen.get_at((x, y))[2]

            # Calculates the output values put through sepia equations
            outputRed = min((inputRed * .393) + (inputGreen * .769) + (inputBlue * .189), 255)
            outputGreen = min((inputRed * .349) + (inputGreen * .686) + (inputBlue * .168), 255)
            outputBlue = min((inputRed * .272) + (inputGreen * .534) + (inputBlue * .131), 255)

            # Sets pixel
            screen.set_at((x, y), (outputRed, outputGreen, outputBlue))


# IMAGE FILTERS TO APPLY TO ENTIRE SCREEN
def applyPixelate(screen):
    # Go through every pixel on canvas
    for x in range(0, 960, 10):
        for y in range(0, 600, 10):
            # Draws a rectangle with the same colour as every 10th pixel to give effect
            draw.rect(screen, (screen.get_at((x, y))), (x, y, 10, 10))


# Turns a single pixel black OR white
def applyThreshHold(screen):
    # Go through every pixel on canvas
    for x in range(960):
        for y in range(600):
            # Applies a threshhold filter to the current pixel
            screen.set_at((x, y), threshHold(128, screen.get_at((x, y))))


# Turns a single pixel b and w
def applyBlackAndWhite(screen):
    # Go through every pixel on canvas
    for x in range(960):
        for y in range(600):
            # Applies threshhold filter to current pixel
            screen.set_at((x, y), blackWhite(screen.get_at((x, y))))


# Inverts the screen colours
def applyInvertColours(screen):
    # Go through every pixel on canvas
    for x in range(960):
        for y in range(600):
            # Inverts the single pixel
            screen.set_at((x, y), invertColour(screen.get_at((x, y))))


# INIDIVIDUAL PIXEL FILTERS
#  turns colour to black or white
def threshHold(level, colour):
    # Determines the average level to get the limit
    average = (colour[0] + colour[1] + colour[2]) / 3

    # If the pixel average is within a range, turn pixels either white or black
    if average >= level:
        return (255, 255, 255)
    else:
        return (0, 0, 0)


# Inverts colour provided
def invertColour(colour):
    # Returns a number that is "flipped"
    return (255 - colour[0], 255 - colour[1], 255 - colour[2])


# Turns colour to greyscale
def blackWhite(colour):
    # Averages out the RGB values to become greyscale
    average = (colour[0] + colour[1] + colour[2]) / 3
    return average, average, average


# FUNCTIONS TO LOAD PHOTOS
# ADD PHOTO TO CNAVAS
def loadPhoto(customCursorImage, undoList, redoList):


    # Ask for a dialog to popup
    tempLoadImage = filedialog.askopenfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

    if tempLoadImage:
        customCursorImage = image.load(tempLoadImage)
        saveAction()  # Saves the action that was just performed for undo list
        return customCursorImage


# LOAD EXISTING PHOTO
def loadPhotoNewFile(screen, fileName, undoList, redoList):

    newFile = filedialog.askopenfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

    if newFile:
        loadFile = image.load(newFile)

        screen.fill((255, 255, 255))
        # Adds the new photo to canvas
        screen.blit(loadFile, (0, 0))

        saveAction()  # Saves the action that was just performed for undo list

        return str(newFile)



# Gets mouse location within canvas
def checkIfMouseOnScreen(mx, my):
    # Checks if mouse is on canvas
    if canvasRect.collidepoint(mx, my):
        # Returns the relative mouse position
        return ("%3i,%3i" % (mx - 20, my - 80))
    else:
        # Return that mouse is off canvas
        return ("N/A , N/A")


# Check if mouse in certain region
def mouseInRange(mx, my, x, y, w, h):
    if x < mx < x + w and y < my < y + h:
        return True
    else:
        return False


# Transparent markings
def toolMarker(mx, my, mxo, myo, screen, colour, size):
    # Creates a transparent surface in which to draw a dot on
    brushHead = Surface((size * 2, size * 2), SRCALPHA)
    # Draw a sized dot on surface
    draw.circle(brushHead, (colour[0], colour[1], colour[2], (200 - size) // 40), (size, size), size)

    # SMOOTH LINE CODE------------------------------------------------
    dx = mxo - mx  # Finds the delta between current mouse position and previous
    dy = myo - my

    distance = int((abs(dx) ** 2 + abs(dy) ** 2) ** 0.5) + 1  # Gets the distance between the points

    for i in range(distance):
        x = int(mx + i / distance * dx)  # Calculates where the circle should go
        y = int(my + i / distance * dy)
        screen.blit(brushHead, (x - size, y - size))
    # ----------------------------------------------------------

    # Returns mouse positions so next chain can be drawn
    return mx, my


# TOOL FUNCTIONS
# Tool to draw sharp bevelled lines
def toolPen(mx, my, mxo, myo, screen, colour, size):
    # SMOOTH LINE CODE------------------------------------------------
    dx = mxo - mx  # Finds the delta between current mouse position and previous
    dy = myo - my

    distance = int((abs(dx) ** 2 + abs(dy) ** 2) ** 0.5) + 1  # Gets the distance between the points

    for i in range(distance):
        x = int(mx + i / distance * dx)  # Calculates where the circle should go
        y = int(my + i / distance * dy)

        draw.line(screen, colour, (x - size // 2, y - 8 * size), (x + size // 2, y + 8 * size), size)

    # ----------------------------------------------------------
    return mx, my


# Square eraser
def toolEraser(mx, my, mxo, myo, screen, colour, size):
    # SMOOTH LINE CODE------------------------------------------------
    dx = mxo - mx  # Finds the delta between current mouse position and previous
    dy = myo - my

    distance = int((abs(dx) ** 2 + abs(dy) ** 2) ** 0.5) + 1  # Gets the distance between the points

    for i in range(distance):
        x = int(mx + i / distance * dx)  # Calculates where the circle should go
        y = int(my + i / distance * dy)
        draw.rect(screen, (255, 255, 255), (x - 2 * size, y - 2 * size, 4 * size, 4 * size))  # Draws figure

    # ----------------------------------------------------------
    return mx, my


# Brush tool
def toolBrush(mx, my, mxo, myo, screen, colour, size):
    # SMOOTH LINE CODE------------------------------------------------
    dx = mxo - mx  # Finds the delta between current mouse position and previous
    dy = myo - my

    distance = int((abs(dx) ** 2 + abs(dy) ** 2) ** 0.5) + 1  # Gets the distance between the points

    for i in range(distance):
        x = int(mx + i / distance * dx)  # Calculates where the circle should go
        y = int(my + i / distance * dy)
        draw.circle(screen, colour, (x, y), size // 2)  # Display the shape
    # ----------------------------------------------------------


    return mx, my


# Places dots randonly within a range
def toolSprayPaint(mx, my, mxo, myo, screen, colour, size):
    # Runs a loop for a certain amount of time to speed up the generation of points
    # SMOOTH LINE CODE------------------------------------------------
    dx = mxo - mx  # Finds the delta between current mouse position and previous
    dy = myo - my

    distance = int((abs(dx) ** 2 + abs(dy) ** 2) ** 0.5) + 1  # Gets the distance between the points

    for f in range(distance):
        x = int(mx + f / distance * dx)  # Calculates where the circle should go
        y = int(my + f / distance * dy)

        for i in range(int((size ** 2) / distance)):

            # Generates a random relative value for X and Y based on size
            randX = randint(-2 * size, 2 * size)
            randY = randint(-2 * size, 2 * size)

            # Checks if the random point is "valid" by checking if it is within the preset radius
            if dist(x, y, (randX + x), (randY + y)) < 2 * size:

                # Checks if the blood dripping feature is enabled
                if blood and 0 < y + randY < 600 and 0 < x + randX < 960:
                    # If the targetting pixel is already painted, go down until an empty spot is found
                    while screen.get_at((int(x + randX), int(y + randY))) == colour:
                        # Checks to make sure it is still on canvas
                        if (randY + 5) + y < 600:
                            randY += 5
                        else:
                            break

                screen.set_at((int(x + randX), int(y + randY)), colour)

    return mx, my


# Restores default cursor
def toolCursor():
    mouse.set_visible(True)


# Gets the colour at a pixel
def toolColourPicker(screen, mx, my):
    return screen.get_at((mx, my))


# Undo function
def undo(undoList, redoList, screen, cursorCache):
    # Makes sure the lists are not empty

    if len(undoList) > 1:
        # Moves the entry to redolist
        redoList.append(undoList.pop())

        # Adds the latest entry to the screen
        screen.blit(undoList[-1], (0, 0))

    else:
        screen.fill((255, 255, 255))

    # Returns list to update them
    return undoList, redoList, screen.copy()


# Redo function
def redo(undoList, redoList, screen, cursorCache):
    # Makes sure redo list is not empty
    if len(redoList) > 0:
        # Blits the latest entry
        screen.blit(redoList[-1], (0, 0))

        # Moves the entry to redolist and deletes
        undoList.append(redoList.pop())

    return undoList, redoList, screen.copy()


# END OF FUNCTIONS------------------------------------------------------------------------------------------------

while running:
    # If the mouse is hovered over a button give info
    hoverTool = None

    # Unix time
    unixTime = (time.get_ticks() // 1000)

    # Sets title and logo
    if fileName == None:
        fileName = "Untitled"

    # Updates caption for filename and FPS
    display.set_caption("Mike-ro-soft Paint 2.0 " + fileName + " FPS: " + str(round(clock.get_fps(), 2)))

    click = False  # Resets momentary click
    unclick = False

    # Mouse location
    mx, my = mouse.get_pos()

    # Mouse click status
    mb = mouse.get_pressed()

    # Relative mouse values to drawing canvas
    mxr = mx - 20
    myr = my - 80

    # If snapping is enabled, push to nearest grid
    if snapping:
        mxr -= mxr % 60
        myr -= myr % 60

    # Event loop
    for e in event.get():
        # e = event.wait()
        # Click button
        if e.type == QUIT:

            # If something was drawn without being saved
            if actionMade:

                # If the save prompt is not open yet
                if not savePromptVisible:
                    paletteVisible = False  # Closes all other subwindows
                    drawerVisible = False
                    aboutVisible = False
                    savePromptVisible = True
                    graphPromptVisible = False
                    helpPromptVisible = False
                    menuOpen = True

                    nextAction = "close"

                    endTime = unixTime  # Sets endTime to time of clicking close

            else:  # If no actions are unsaved
                running = False  # Kill the program


        if e.type == USEREVENT:
            musicList.insert(0,musicList.pop())
            mixer.music.load(musicList[-1])
            mixer.music.play()


        # If the mouse is clicked down, activate the momentary variable
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            mxs, mys = mx, my
            click = True

        # If mouse is released, activate momentary variable
        if e.type == MOUSEBUTTONUP and e.button == 1:
            unclick = True

        # If the current screen displayed is the canvas
        if currentScreen == "Drawing":

            # Saving for undo
            # If the mouse is clicked in the canvas (it means something has been drawn), save the previous state in a list
            if e.type == MOUSEBUTTONUP and e.button == 1 and not menuOpen and canvasRect.collidepoint(mx,
                                                                                                      my) and currentTool != "Colour Picker":
                # When the mouse is clicked in the canvas, the screen is saved for undo/redo
                saveAction()  # Saves the action that was just performed for undo list

            # Scroll wheel
            if e.type == MOUSEBUTTONDOWN and not menuOpen:
                # Scroll down
                if e.button == 5 and cursorSize > 3:
                    cursorSize -= 3
                # Scroll up
                if e.button == 4 and cursorSize < 100:
                    cursorSize += 3

            # Keyboard shortcuts
            if e.type == KEYDOWN and (not menuOpen or graphPromptVisible):

                drawArea.blit(cursorCache, (0, 0))
                if currentTool != "Text" and currentTool != "Graph":
                    if e.key == K_1:
                        currentTool = "Brush"
                        menuIndex = "Brush"
                    elif e.key == K_2:
                        currentTool = "Eraser"
                        menuIndex = "Brush"
                    elif e.key == K_3:
                        currentTool = "Pen"
                        menuIndex = "Brush"
                    elif e.key == K_4:
                        currentTool = "Spray Paint"
                        menuIndex = "Brush"
                    elif e.key == K_5:
                        currentTool = "Colour Picker"
                        menuIndex = "Brush"
                    elif e.key == K_6:
                        currentTool = "Rectangle"
                        menuIndex = "Shapes"
                    elif e.key == K_7:
                        currentTool = "Ellipse"
                        menuIndex = "Shapes"
                    elif e.key == K_8:
                        currentTool = "Line"
                        menuIndex = "Shapes"
                    elif e.key == K_9:
                        currentTool = "Bucket"
                        menuIndex = "Brush"
                    elif e.key == K_0:
                        currentTool = "Marker"
                        menuIndex = "Brush"
                    elif e.key == K_w:
                        currentTool = "Text"
                        menuIndex = "Text"
                        currentFont = "Ubuntu"

                    elif e.key == K_e:
                        currentTool = "Circle"
                        menuIndex = "Shapes"
                    elif e.key == K_r:
                        currentTool = "Square"
                        menuIndex = "Shapes"
                    elif e.key == K_y:
                        currentTool = "Polygon"
                        menuIndex = "Shapes"
                    elif e.key == K_g:
                        currentTool = "Spray Paint"
                        menuIndex = "Brush"
                        blood = True




                    elif e.key == K_u:
                        currentTool = "Stamp 1"
                        menuIndex = "Sticker"
                    elif e.key == K_i:
                        currentTool = "Stamp 2"
                        menuIndex = "Sticker"
                    elif e.key == K_o:
                        currentTool = "Stamp 3"
                        menuIndex = "Sticker"
                    elif e.key == K_p:
                        currentTool = "Stamp 4"
                        menuIndex = "Sticker"
                    elif e.key == K_h:
                        currentTool = "Stamp 5"
                        menuIndex = "Sticker"
                    elif e.key == K_j:
                        currentTool = "Stamp 6"
                        menuIndex = "Sticker"
                    elif e.key == K_k:
                        currentTool = "Stamp 7"
                        menuIndex = "Sticker"
                    elif e.key == K_l:
                        currentTool = "Stamp 8"
                        menuIndex = "Sticker"


                    # Filter shortcuts

                    # Invert Colours
                    elif e.key == K_v:

                        applyInvertColours(drawArea)

                        saveAction()  # Saves the action that was just performed for undo list


                    # Black and white filter
                    elif e.key == K_x:
                        applyBlackAndWhite(drawArea)

                        saveAction()  # Saves the action that was just performed for undo list


                    # Threshhold filter
                    elif e.key == K_c:
                        applyThreshHold(drawArea)

                        saveAction()  # Saves the action that was just performed for undo list


                    # Pixelate
                    elif e.key == K_a:
                        applyPixelate(drawArea)

                        saveAction()  # Saves the action that was just performed for undo list


                    # Blur
                    elif e.key == K_f:
                        for i in range(4):
                            blurCache = transform.smoothscale(drawArea.copy(), (64, 40))
                            blurCache = transform.smoothscale(blurCache, (960, 600))
                            drawArea.blit(blurCache, (0, 0))

                        saveAction()  # Saves the action that was just performed for undo list


                    # Sepia
                    elif e.key == K_d:
                        applySepia(drawArea)

                        saveAction()  # Saves the action that was just performed for undo list




                    # Load a photo, preserving previous ones
                    elif e.key == K_b:
                        customCursorImage = None  # Resets custom cursor
                        customCursorImage = loadPhoto(customCursorImage, undoList,
                                                      redoList)  # loads the photo into memory
                        if customCursorImage != None:  # Checks if photo is valid
                            currentTool = "Stamp Custom"  # Changes tool
                            saveAction()  # Saves the action that was just performed for undo list


                    # Loads photo, destroying the canvas
                    elif e.key == K_m:

                        fileName = loadPhotoNewFile(drawArea, fileName, undoList, redoList)  # Sets new file name

                        saveAction()  # Saves the action that was just performed

                        undoList = []
                        undoList.append(drawArea.copy())  # Adds the screen to the list
                        redoList = []  # Clears the redo list because they are no longer valid

                    # Clears the canvas
                    elif e.key == K_n:

                        # If the save prompt is not open yet
                        if actionMade:
                            if not savePromptVisible:
                                paletteVisible = False  # Closes all other subwindows
                                drawerVisible = False
                                aboutVisible = False
                                savePromptVisible = True
                                helpPromptVisible = False
                                graphPromptVisible = False
                                menuOpen = True

                                nextAction = "clear"

                                endTime = unixTime  # Sets endTime to time of clicking close



                    elif key.get_mods() & KMOD_CTRL and key.get_mods() & KMOD_SHIFT:
                        # Saveas dialog
                        if e.key == K_s:

                            tempFileName = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

                            if tempFileName:  # Checks if file name is valid


                                image.save(drawArea, tempFileName)  # Saves the photo
                                fileName = tempFileName  # Sets the file name
                                actionMade = False  # Resets actionmade as save completed
                                startTime = None  # Resets time of last save
                                actionsMade = 0  # Resets amount of unsaved actions


                    # Undo
                    elif key.get_mods() & KMOD_CTRL:
                        if e.key == K_z:
                            undoList, redoList, cursorCache = undo(undoList, redoList, drawArea, cursorCache)

                        # Redo
                        elif e.key == K_t:
                            undoList, redoList, cursorCache = redo(undoList, redoList, drawArea, cursorCache)

                        # Takes a screenshot
                        elif e.key == K_s:

                            # If the file name is not yet saved
                            if fileName == "Untitled":
                                tempFileName = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])  # Ask to get a name

                            if tempFileName:  # Checks if the set name is valid

                                image.save(drawArea, tempFileName)  # Saves the photo
                                fileName = tempFileName  # Sets as the file name
                                actionMade = False  # Resets actionmade as save completed
                                startTime = None  # Resets time of last save



                    # Toggles if polygon fill is on
                    elif e.key == K_q:
                        if polygonFill:
                            polygonFill = False
                        else:
                            polygonFill = True

                else:  # If the current tool is text, override all keyboard shortcuts

                    keyVal = e.unicode#key.name(e.key)  # Gets the letter pressed from keyboard

                    if key.get_pressed()[K_BACKSPACE]:
                        if not key.get_mods() & KMOD_CTRL:  # If ctrl+backspace clear the field
                            textContent = textContent[0:-1]  # Remove last item
                        else:
                            textContent = ""  # Clear

                    #Changes limit depending on tool
                    elif not graphPromptVisible and len(textContent) < 100:  # Checks if limit of 100 chars has been reahed

                        textContent += keyVal
                        #Adds the character to the textbox

                    elif graphPromptVisible and len(textContent) < 30:
                        textContent += keyVal


    # Menu screen selected
    if currentScreen == "Menu":

        # Draws the intro window
        draw.rect(screen, (188, 188, 188), (365, 100, 550, 480))

        # Draws the load button
        draw.rect(screen, BUTTONCOL, loadFileButton)

        # If mouse i on button
        if loadFileButton.collidepoint(mx, my):
            # Draw the hover button
            draw.rect(screen, BUTTONHOVER, loadFileButton)

            # But if the mouse is alsodown
            if unclick:
                # Draw the clicked
                draw.rect(screen, BUTTONCLICK, loadFileButton)

                # Attempt to load the file

                tempFileName = filedialog.askopenfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

                if tempFileName:
                    loadFile = image.load(tempFileName)
                    imageToBeLoaded = True

                else:
                    tempFileName = None

                # If the file returned is valid
                if tempFileName != None:
                    # Sets file name
                    fileName = tempFileName
                    # Advances screen
                    currentScreen = "Drawing"
                    mxo, myo = mxr, myr

        # Start new file button
        draw.rect(screen, BUTTONCOL, startNewFileButton)

        # Checks if mouse on button
        if startNewFileButton.collidepoint(mx, my):

            # Draws hover
            draw.rect(screen, BUTTONHOVER, startNewFileButton)

            # If it is clicked
            if unclick:
                # Draw clicked
                draw.rect(screen, BUTTONCLICK, startNewFileButton)

                # Creates new faile name from date
                fileName = "Untitled"  # str("screenshots/" + datetime.now().strftime('%Y%m%d%H%M%S')) + ".jpg"

                # Advances screen
                currentScreen = "Drawing"
                mxo, myo = mxr, myr

        # Text dialogs
        screen.blit(ubuntuFont.render("Mike-ro-soft Paint 2.0", True, (0, 0, 0)), (390, 115))
        screen.blit(ubuntuFontSmall.render("created by Henry Tu", True, (80, 80, 80)), (390, 143))

        # Sample image
        screen.blit(wall1, (390, 190))

        # Text on button
        screen.blit(ubuntuFont.render("Load File", True, (0, 0, 0)), (420, 455))
        screen.blit(ubuntuFont.render("New File", True, (0, 0, 0)), (420, 515))

    # If the current screen is the drawing (Not the menu screen)
    elif currentScreen == "Drawing":

        # __________________________________________________________________________________________________________
        # START DRAW MENU ITEMS

        # Ensures that the UI is only drawn once
        if not drawnUI:
            drawnUI = True

            # DRAWS THE LAYOUT OF THE SCREEN
            draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground

            drawArea.fill((255, 255, 255))  # Clears the screen

            if imageToBeLoaded:
                drawArea.blit(loadFile, (0, 0))

            undoList = [drawArea.copy()]  # Resets undo list

            cursorCache = drawArea.copy()

            # Cursor cache

        draw.rect(screen, BACKGROUND, (0, 680, 1280, 20))  # Redraws botton portion so that text is reset

        draw.rect(screen, SIDEBAR, (1000, 0, 280, 700))  # Dock
        draw.rect(screen, (0, 166, 204), (1000, 0, 280, 120))  # Dock blue highlight

        draw.rect(screen, WINDOWS, (0, 0, 1280, 50))  # Top Bar

        draw.rect(screen, currentColours[0], colourPreviewRect)  # Current colour preview window

        # Highlight buttons
        draw.rect(screen, (210, 210, 210), (1145, 480, 120, 50))
        draw.rect(screen, (210, 210, 210), (1025, 650, 240, 50))

        # Draw button
        draw.rect(screen, BUTTONCOL, paletteButtonRect)
        draw.rect(screen, BUTTONCOL, colourPickerButtonRect)

        # SLIDER FOR CURSOR SIZE
        draw.rect(screen, BUTTONCLICK, (1030, 410, 230, 2))
        draw.rect(screen, BUTTONHOVER, (1030, 410, 230 * (cursorSize / 100), 2))
        draw.circle(screen, BUTTONHOVER, (int(1030 + 230 * (cursorSize / 100)), 410), 10)
        draw.circle(screen, BUTTONCLICK, (int(1030 + 230 * (cursorSize / 100)), 410), 6)

        # Test if mouse is on hitbox
        if sliderRect.collidepoint(mxs, mys) and mb[0] == 1 and not menuOpen:
            cursorSize = (mx - 1030) * 100 // 230

        # Controls the cursor size
        if cursorSize > 100:
            cursorSize = 100
        elif cursorSize < 1:
            cursorSize = 1

        # Displays a title for slider
        screen.blit(ubuntuFontSmall.render(("Size"), True, BLACK), (1030, 385))
        screen.blit(ubuntuFontSmall.render(str(cursorSize), True, BLACK), (1240, 385))

        # if colour palette preview is clicked
        if colourPreviewRect.collidepoint(mxs, mys) and unclick and not menuOpen:
            paletteVisible = True

        # If colour picker button is clicked
        if colourPickerButtonRect.collidepoint(mx, my) and not menuOpen:
            hoverTool = "Colour Picker"

            draw.rect(screen, BUTTONHOVER, colourPickerButtonRect)
            if click:

                rainbow = False #Turns of rainbow tool

                draw.rect(screen, BUTTONCLICK, colourPickerButtonRect)
                currentTool = "Colour Picker"

        # If the colour palette button is hit
        if paletteButtonRect.collidepoint(mx, my) and not menuOpen:
            draw.rect(screen, BUTTONHOVER, paletteButtonRect)

            if unclick:
                draw.rect(screen, BUTTONCLICK, paletteButtonRect)
                paletteVisible = True

        # Drawing in the colour squares (Gradients)
        currentCol = 1  # Current colour tile being drawn

        # Draws a 6x3 box of colours
        for x in range(6):
            for y in range(3):
                # Draws the box
                draw.rect(screen, currentColours[currentCol], (1025 + x * 40, 535 + y * 40, 40, 40))
                currentCol += 1

        # TEXT BOXES
        screen.blit(ubuntuFont.render(currentTool, True, (255, 255, 255)), (1010, 60))

        # Mouse location textbox
        screen.blit(ubuntuFontSmall.render(("Mouse location: " + checkIfMouseOnScreen(mx,
                                                                                      my) + " Current colour: R" + str(
            currentColours[0][0]) + " G" + str(currentColours[0][1]) + " B" + str(
            currentColours[0][2]) + " Cursor size: " + str(cursorSize)), True, BLACK), (20, 680))

        # Draws the background for the help textboxes
        draw.rect(screen, (255, 255, 255), (1025, 430, 240, 40))

        # TOP MENU BAR
        # If the mouse is in the top bar
        if mouseInRange(mx, my, 10, 5, 1260, 45) and not menuOpen:

            buttonNumber = (mx - 10) // 60
            # Gets the button number from the mouse position

            for index in menuIndexCode:
                # Goes through the code to match the button number with a certain action
                if menuIndexCode[index] == buttonNumber and index[0:5] != "Blank":
                    # Checks to make sure the button is actually being used
                    # "Blank" represents a placeholder
                    draw.rect(screen, (4, 59, 100), (10 + 60 * buttonNumber, 0, 60, 50), 0)
                    # Draws the highlight

                    # If the button is also clicked
                    if click:
                        if buttonNumber > 6 and buttonNumber < 12:  # Not momentary buttons
                            menuIndex = index

                        elif buttonNumber == 0:  # Left sliding menu

                            drawerVisible = True
                            drawnDrawer = False

                        elif buttonNumber == 19:  # Undo button
                            undoList, redoList, cursorCache = undo(undoList, redoList, drawArea, cursorCache)


                        elif buttonNumber == 20:  # Redo button
                            undoList, redoList, cursorCache = redo(undoList, redoList, drawArea, cursorCache)

                        if musicEnabled:
                            if buttonNumber == 13:  # volume mute button
                                if mixer.music.get_volume() == 0:  # Checks if mute and flips if needed
                                    mixer.music.set_volume(1)
                                else:
                                    mixer.music.set_volume(0)

                            elif buttonNumber == 14 and volume > 0.2:  # Volume down button
                                volume -= 0.2  # Deduces volume and updates
                                mixer.music.set_volume(volume)

                            elif buttonNumber == 15 and volume < 1:  # Volume up button
                                volume += 0.2  # Adds volume and updates
                                mixer.music.set_volume(volume)

        # If the current menu screen is brush
        if menuIndex == "Brush":

            # Makes a grid of buttons
            for x in range(0, 200, 100):
                for y in range(0, 150, 70):

                    # Gets the box mouse is in
                    xCord = x // 100
                    yCord = y // 70

                    # Draws the boxes
                    draw.rect(screen, BUTTONCOL, (1050 + x, 150 + y, 90, 60))

                    # If mouse mouse is over a button
                    if mouseInRange(mx, my, 1050 + x, 150 + y, 90, 60) and not menuOpen:

                        # Draw a highlight over it
                        draw.rect(screen, BUTTONHOVER, (1050 + x, 150 + y, 90, 60))

                        # Execute the command based on the button location
                        if (xCord, yCord) == (0, 0):
                            # If the mouse is being pressed
                            if click:
                                currentTool = "Brush"
                            else:
                                hoverTool = "Brush"
                        elif (xCord, yCord) == (0, 1):

                            if click:
                                currentTool = "Eraser"
                            else:
                                hoverTool = "Eraser"
                        elif (xCord, yCord) == (0, 2):

                            if click:
                                currentTool = "Pen"
                            else:
                                hoverTool = "Pen"
                        elif (xCord, yCord) == (1, 0):

                            if click:
                                currentTool = "Spray Paint"
                            else:
                                hoverTool = "Spray Paint"
                        elif (xCord, yCord) == (1, 1):

                            if click:
                                currentTool = "Bucket"
                            else:
                                hoverTool = "Bucket"
                        elif (xCord, yCord) == (1, 2):

                            if click:
                                currentTool = "Marker"
                            else:
                                hoverTool = "Marker"

            # Draws an indicator to show what button is already selected
            if currentTool == "Brush":
                draw.rect(screen, BUTTONCLICK, (1050, 150, 90, 60))
            elif currentTool == "Eraser":
                draw.rect(screen, BUTTONCLICK, (1050, 220, 90, 60))
            elif currentTool == "Pen":
                draw.rect(screen, BUTTONCLICK, (1050, 290, 90, 60))
            elif currentTool == "Spray Paint":
                draw.rect(screen, BUTTONCLICK, (1150, 150, 90, 60))
            elif currentTool == "Bucket":
                draw.rect(screen, BUTTONCLICK, (1150, 220, 90, 60))
            elif currentTool == "Marker":
                draw.rect(screen, BUTTONCLICK, (1150, 290, 90, 60))

            # Draw icons
            screen.blit(brushTool, (1070, 160))
            screen.blit(eraserTool, (1070, 230))
            screen.blit(penTool, (1070, 300))

            screen.blit(spraypaintTool, (1170, 160))
            screen.blit(paintBucketTool, (1170, 230))
            screen.blit(markerTool, (1170, 300))

            """
            if len(undoList) == 0:
                draw.rect(screen, (100, 100, 100), (10 + 60 * 19, 0, 60, 50), 0)

            if len(redoList) == 0:
                draw.rect(screen, (100, 100, 100), (10 + 60 * 20, 0, 60, 50), 0)
            """

            # Blood toggle switch
            if blood:
                screen.blit(buttonOn, (1150, 110))
            else:
                screen.blit(buttonOff, (1150, 110))

            # Blood title
            screen.blit(ubuntuFontSmall.render("Blood", True, BLACK), (1200, 125))

            # If the blood button is toggled
            if mouseInRange(mx, my, 1150, 120, 50, 30):
                if click:
                    if blood:
                        blood = False
                    else:
                        blood = True
                        currentTool = "Spray Paint"
                else:
                    hoverTool = "Blood"

            # Blood toggle switch
            if rainbow:
                screen.blit(buttonOn, (1050, 110))
            else:
                screen.blit(buttonOff, (1050, 110))

            # Blood title
            screen.blit(ubuntuFontSmall.render("Rainbw", True, BLACK), (1100, 125))

            # If the blood button is toggled
            if mouseInRange(mx, my, 1050, 120, 50, 30):
                if click:
                    if rainbow:
                        rainbow = False
                    else:
                        currentColours[0] = (255, 0, 0)
                        rainbow = True
                else:
                    hoverTool = "Rainbow"





        # Stickets menu selected
        elif menuIndex == "Sticker":

            # Makes a 2x4 grid of buttons
            for x in range(0, 200, 100):
                for y in range(0, 220, 60):

                    # Gets the coordinate of the button
                    xCord = x // 100
                    yCord = y // 60

                    # Draws the buttons
                    draw.rect(screen, BUTTONCOL, (1050 + x, 130 + y, 90, 55))

                    # If the mouse is over the button region
                    if mouseInRange(mx, my, 1050 + x, 130 + y, 90, 55) and not menuOpen:

                        # Draws the mouse hover
                        draw.rect(screen, BUTTONHOVER, (1050 + x, 130 + y, 90, 55))

                        hoverTool = "Stamp 1"

                        # If mouse is clicked, find the button and change tools
                        if click:
                            if (xCord, yCord) == (0, 0):
                                currentTool = "Stamp 1"
                            elif (xCord, yCord) == (0, 1):
                                currentTool = "Stamp 2"
                            elif (xCord, yCord) == (0, 2):
                                currentTool = "Stamp 3"
                            elif (xCord, yCord) == (0, 3):
                                currentTool = "Stamp 4"
                            elif (xCord, yCord) == (1, 0):
                                currentTool = "Stamp 5"
                            elif (xCord, yCord) == (1, 1):
                                currentTool = "Stamp 6"
                            elif (xCord, yCord) == (1, 2):
                                currentTool = "Stamp 7"
                            elif (xCord, yCord) == (1, 3):
                                currentTool = "Stamp 8"

            # Custom stamp button
            draw.rect(screen, BUTTONCOL, (1005, 130, 40, 235))

            # If the mouse is on the button
            if mouseInRange(mx, my, 1005, 130, 40, 235):
                # Draw the highlight
                draw.rect(screen, BUTTONHOVER, (1005, 130, 40, 235))

                hoverTool = "Stamp Custom"

                # When its clicked
                if unclick:

                    # Resets custom cursor
                    customCursorImage = None

                    # Loads the image
                    customCursorImage = loadPhoto(customCursorImage, undoList, redoList)

                    # If the image is valid, change tools
                    if customCursorImage != None:
                        currentTool = "Stamp Custom"
                        saveAction()  # Saves the action that was just performed for undo list

            # Checks the stamp and draws a highlight over current tool
            if currentTool == "Stamp 1":
                draw.rect(screen, BUTTONCLICK, (1050, 130, 90, 55))
            elif currentTool == "Stamp 2":
                draw.rect(screen, BUTTONCLICK, (1050, 190, 90, 55))
            elif currentTool == "Stamp 3":
                draw.rect(screen, BUTTONCLICK, (1050, 250, 90, 55))
            elif currentTool == "Stamp 4":
                draw.rect(screen, BUTTONCLICK, (1050, 310, 90, 55))
            elif currentTool == "Stamp 5":
                draw.rect(screen, BUTTONCLICK, (1150, 130, 90, 55))
            elif currentTool == "Stamp 6":
                draw.rect(screen, BUTTONCLICK, (1150, 190, 90, 55))
            elif currentTool == "Stamp 7":
                draw.rect(screen, BUTTONCLICK, (1150, 250, 90, 55))
            elif currentTool == "Stamp 8":
                draw.rect(screen, BUTTONCLICK, (1150, 310, 90, 55))
            elif currentTool == "Stamp Custom":
                draw.rect(screen, BUTTONCLICK, (1005, 130, 40, 235))

            # Draws the button icons

            for y in range(135,316,60):
                screen.blit(stampCroppedList[y//60 - 2], (1073, y))
                screen.blit(stampCroppedList[y//60 + 2], (1173, y))

            screen.blit(transform.rotate(ubuntuFont.render("Custom Stamp", True, BLACK), 90), (1005, 150))

        # SHapes menu
        elif menuIndex == "Shapes":

            # Same idea as the previous menu, no need to repeat
            for x in range(0, 200, 100):
                for y in range(0, 220, 60):
                    xCord = x // 100
                    yCord = y // 60

                    draw.rect(screen, BUTTONCOL, (1080 + x, 130 + y, 90, 55))
                    if mouseInRange(mx, my, 1080 + x, 130 + y, 90, 55) and not menuOpen:
                        draw.rect(screen, BUTTONHOVER, (1080 + x, 130 + y, 90, 55))

                        if (xCord, yCord) == (0, 0):
                            if click:
                                currentTool = "Rectangle"
                            else:
                                hoverTool = "Rectangle"

                        elif (xCord, yCord) == (0, 1):
                            if click:
                                currentTool = "Square"
                            else:
                                hoverTool = "Square"

                        elif (xCord, yCord) == (0, 2):
                            if click:
                                currentTool = "Ellipse"
                            else:
                                hoverTool = "Ellipse"

                        elif (xCord, yCord) == (0, 3):
                            if click:
                                currentTool = "Graph"
                            else:
                                hoverTool = "Graph"

                        elif (xCord, yCord) == (1, 0):
                            if click:
                                currentTool = "Line"
                            else:
                                hoverTool = "Line"

                        elif (xCord, yCord) == (1, 1):
                            if click:
                                currentTool = "Polygon"
                                polygonList = []
                            else:
                                hoverTool = "Polygon"

                        elif (xCord, yCord) == (1, 2):
                            if click:
                                currentTool = "Circle"
                            else:
                                hoverTool = "Circle"


                        elif (xCord, yCord) == (1, 3):
                            if click:
                                currentTool = "Triangle"
                            else:
                                hoverTool = "Triangle"

            if currentTool == "Rectangle":
                draw.rect(screen, BUTTONCLICK, (1080, 130, 90, 55))
            elif currentTool == "Square":
                draw.rect(screen, BUTTONCLICK, (1080, 190, 90, 55))
            elif currentTool == "Ellipse":
                draw.rect(screen, BUTTONCLICK, (1080, 250, 90, 55))
            elif currentTool == "Line":
                draw.rect(screen, BUTTONCLICK, (1180, 130, 90, 55))
            elif currentTool == "Polygon":
                draw.rect(screen, BUTTONCLICK, (1180, 190, 90, 55))
            elif currentTool == "Circle":
                draw.rect(screen, BUTTONCLICK, (1180, 250, 90, 55))
            elif currentTool == "Graph":
                draw.rect(screen, BUTTONCLICK, (1080, 310, 90, 55))
            elif currentTool == "Triangle":
                draw.rect(screen, BUTTONCLICK, (1180, 310, 90, 55))

            # TOGGLE SWITCH-----------------------------------------------------------------

            # Title
            screen.blit(ubuntuFontSmall.render("Fill polygon", True, BLACK), (1000, 160))

            # If the button is clicked, flip state
            if mouseInRange(mx, my, 1010, 125, 50, 30):
                if click:
                    if polygonFill:
                        polygonFill = False
                    else:
                        polygonFill = True
                else:
                    hoverTool = "FillPoly"

            if polygonFill:
                screen.blit(buttonOn, (1010, 120))
            else:
                screen.blit(buttonOff, (1010, 120))

            # TOGGLE SWITCH-------------------------------------------------------------------
            screen.blit(ubuntuFontSmall.render("Snapping", True, BLACK), (1008, 220))

            if mouseInRange(mx, my, 1010, 185, 50, 30):
                if click:
                    if snapping:
                        snapping = False
                    else:
                        snapping = True
                else:
                    hoverTool = "Snapping"

            # Changes graphic
            if snapping:
                screen.blit(buttonOn, (1010, 180))
            else:
                screen.blit(buttonOff, (1010, 180))

            # TOGGLE SWITCH-------------------------------------------------------------------
            screen.blit(ubuntuFontSmall.render("Round Line", True, BLACK), (1002, 280))

            if mouseInRange(mx, my, 1010, 245, 50, 30):
                if click:
                    currentTool = "Line"
                    if roundLine:
                        roundLine = False
                    else:
                        roundLine = True
                else:
                    hoverTool = "RoundLine"

            # Changes graphic
            if roundLine:
                screen.blit(buttonOn, (1010, 240))
            else:
                screen.blit(buttonOff, (1010, 240))


            # Button icons
            screen.blit(rectShape, (1100, 135))
            screen.blit(squareShape, (1110, 195))
            screen.blit(ellipseShape, (1105, 255))
            screen.blit(equationShape, (1105, 315))

            screen.blit(triangleShape, (1200, 315))
            screen.blit(lineShape, (1200, 135))
            screen.blit(polygonShape, (1200, 195))
            screen.blit(circleShape, (1200, 255))



        elif menuIndex == "Text":

            # Draws buttons
            draw.rect(screen, BUTTONCOL, ubuntuFontBox)
            draw.rect(screen, BUTTONCOL, timesNewRomanFontBox)
            draw.rect(screen, BUTTONCOL, comicSansFontBox)

            # Repeat down
            # If ubuntu box is hit
            if ubuntuFontBox.collidepoint(mx, my):
                draw.rect(screen, BUTTONHOVER, ubuntuFontBox)  # Draws highlight
                if click:  # If it's clicked
                    currentTool = "Text"  # Change tool
                    currentFont = "Ubuntu"  # Change font
                else:
                    hoverTool = "Text"

            if timesNewRomanFontBox.collidepoint(mx, my):
                draw.rect(screen, BUTTONHOVER, timesNewRomanFontBox)
                if click:
                    currentTool = "Text"
                    currentFont = "TimesNewRoman"
                else:
                    hoverTool = "Text"

            if comicSansFontBox.collidepoint(mx, my):
                draw.rect(screen, BUTTONHOVER, comicSansFontBox)
                if click:
                    currentTool = "Text"
                    currentFont = "ComicSans"
                else:
                    hoverTool = "Text"

            if currentTool == "Text":
                if currentFont == "Ubuntu":
                    draw.rect(screen, BUTTONCLICK, ubuntuFontBox)

                if currentFont == "TimesNewRoman":
                    draw.rect(screen, BUTTONCLICK, timesNewRomanFontBox)

                if currentFont == "ComicSans":
                    draw.rect(screen, BUTTONCLICK, comicSansFontBox)

            # TItles over button
            screen.blit(ubuntuFont.render("Ubuntu", True, (0, 0, 0)), (1030, 150))

            screen.blit(timesNewRomanFont.render("Times New Romans", True, (0, 0, 0)), (1030, 220))

            screen.blit(comicSansFont.render("Comic Sans", True, (0, 0, 0)), (1030, 290))

        # FILTER MENU
        elif menuIndex == "Filters":

            # Same as above, no need to repeat
            for x in range(0, 200, 100):
                for y in range(0, 150, 70):
                    xCord = x // 100
                    yCord = y // 70

                    draw.rect(screen, BUTTONCOL, (1050 + x, 150 + y, 90, 60))
                    if mouseInRange(mx, my, 1050 + x, 150 + y, 90, 60) and not menuOpen:
                        draw.rect(screen, BUTTONHOVER, (1050 + x, 150 + y, 90, 60))

                        if (xCord, yCord) == (0, 0):
                            if unclick:
                                applyPixelate(drawArea)  # Applies the filter
                            else:
                                hoverTool = "Pixelate"

                        elif (xCord, yCord) == (0, 1):
                            if unclick:
                                applyThreshHold(drawArea)
                            else:
                                hoverTool = "Threshhold"

                        elif (xCord, yCord) == (0, 2):
                            if unclick:
                                applyBlackAndWhite(drawArea)
                            else:
                                hoverTool = "BlackWhite"

                        elif (xCord, yCord) == (1, 0):
                            if unclick:
                                applyInvertColours(drawArea)

                            else:
                                hoverTool = "Invert"

                        elif (xCord, yCord) == (1, 1):

                            if unclick:
                                for i in range(4):
                                    blurCache = transform.smoothscale(drawArea.copy(), (64, 40))
                                    blurCache = transform.smoothscale(blurCache, (960, 600))
                                    drawArea.blit(blurCache, (0, 0))


                            else:
                                hoverTool = "Blur"

                        elif (xCord, yCord) == (1, 2):
                            if unclick:
                                applySepia(drawArea)

                            else:
                                hoverTool = "Sepia"

                        if unclick:
                            saveAction()  # Saves the action that was just performed for undo list

            # Draws the icons
            screen.blit(pixelFilter, (1073, 160))
            screen.blit(blackwhiteFilter, (1073, 230))
            screen.blit(threshholdFilter, (1073, 300))

            screen.blit(invertFilter, (1173, 160))
            screen.blit(blurFilter, (1173, 230))
            screen.blit(sepiaFilter, (1173, 300))

        # Draws an indicator to show what menu item is selected
        draw.rect(screen, (4, 159, 195), (10 + 60 * menuIndexCode[menuIndex], 45, 60, 5), 0)

        # Draws a mute indicator
        if musicEnabled and mixer.music.get_volume() == 0:
            draw.rect(screen, (255, 50, 50), (790, 45, 60, 5), 0)

        # ICONS
        screen.blit(menuIcon, (25, 5))
        screen.blit(brushIcon, (445, 5))
        screen.blit(stickerIcon, (505, 5))
        screen.blit(textIcon, (625, 5))
        screen.blit(shapesIcon, (565, 5))
        screen.blit(filterIcon, (685, 5))

        # Only draws the icons if on windows
        if musicEnabled:
            screen.blit(muteVolIcon, (805, 5))
            screen.blit(lowVolIcon, (865, 5))
            screen.blit(highVolIcon, (925, 5))

        screen.blit(undoIcon, (1165, 5))
        screen.blit(redoIcon, (1225, 5))

        screen.blit(palatteIcon, (1040, 660))
        screen.blit(ubuntuFontSmall.render(("More colours"), True, BLACK), (1080, 665))
        screen.blit(pickerIcon, (1190, 490))

        if hoverTool != None:
            # HELP BOXES TEXT
            screen.blit(ubuntuFontSmall.render(helpList1[hoverTool], True, BLACK), (1027, 430))
            screen.blit(ubuntuFontSmall.render(helpList2[hoverTool], True, BLACK), (1027, 450))

        else:
            # HELP BOXES TEXT
            screen.blit(ubuntuFontSmall.render(helpList1[currentTool], True, BLACK), (1027, 430))
            screen.blit(ubuntuFontSmall.render(helpList2[currentTool], True, BLACK), (1027, 450))

        # MENU ITEMS END
        # _____________________________________________________________________________________
        # TOOLS BEGIN

        # Checks if mouse is on colour gradient selector and automatically switches tool
        # Checks to make sure the palette is not visible to avoid conflicts
        # Mini palette
        if paletteMiniRect.collidepoint(mx, my) and not menuOpen:
            mouse.set_visible(False)
            # Turns off cursor so that custom cursor can be added

            localUnderColour = toolColourPicker(screen, mx, my)  # Colour detected under hte mouse
            # This is the colour that is underneath the cursor (on the palette)

            draw.line(screen, invertColour(localUnderColour), (mx - 6, my), (mx + 6, my), 2)
            draw.line(screen, invertColour(localUnderColour), (mx, my - 6), (mx, my + 6), 2)
            # Draws cross with inverted colours for visibility

            draw.circle(screen, invertColour(localUnderColour), (mx + 20, my + 20), 20)
            draw.circle(screen, localUnderColour, (mx + 20, my + 20), 15)
            # Draws preview window

            if click:  # If the mouse is clicked with one burst

                rainbow = False #Turns of rainbow automatically

                # Clears out colour palette and gets new colours and gradients
                currentColours = []
                currentColours.append(localUnderColour)

                # adds the newly selected colour into colour list and generates some colours that are similar
                for i in range(-255, 0, 14):
                    # Generates gradients that will always be valid
                    currentColours.append(
                        (abs(localUnderColour[0] + i), abs(localUnderColour[1] + i), abs(localUnderColour[2] + i)))

        elif canvasRect.collidepoint(mx, my) and not menuOpen:  # if the mouse is in the canvas, also make it disappear
            mouse.set_visible(False)


        else:  # If mouse is not on any useful surface, turn cursor back on
            # mxo, myo = mxr, myr  # Resets oldcursor location because it is no longer applicable
            toolCursor()  # Reverts to default cursor

            # Clears the cursor so that it does not akwardly remain on the canvas
            if not clearedCursor:
                clearedCursor = True
                drawArea.blit(cursorCache, (0, 0))

        if rainbow:  # Rainbow colour option

            # If rainbow cycle reaches either end
            if rainCycle == 0 or rainCycle == 100:
                rainRate *= -1  # Flip the count

            # Advances cycle count
            rainCycle += rainRate

            # Calculates colours with math I don't quite understand
            R = 128 + sin((int(rainCycle) * 0.1 + 0) * 1.3) * 128
            G = 128 + sin((int(rainCycle) * 0.1 + 2) * 1.3) * 128
            B = 128 + sin((int(rainCycle) * 0.1 + 4) * 1.3) * 128

            # Sets the colour
            currentColours[0] = (R, G, B)

        # Resets the start position of the cursor if last location was outside of canvas
        if not wideCanvasRect.collidepoint(mxs,
                                           mys):  # This "canvas" is larger than the visible canvas to allow for the cursor to move out of the screen
            mxs, mys = mx, my

        if currentTool == "Graph" and not menuOpen:

            graphPromptVisible = True
            menuOpen = True

            toolCursor()  # makes cursor visible

            drawArea.blit(cursorCache, (0, 0))



        if wideCanvasRect.collidepoint(mxs, mys):  # If mouse is on the canvas



            # Pen tool
            # Checks to make sure the palette is not visible to avoid conflicts
            if currentTool == "Pen" and not menuOpen:
                if mb[0] == 1:  # If the mouse is held down
                    if not clearedCursor:  # Clears the cursor only ONCE
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Sets old mouse pos to draw in between
                    # mxo, myo = toolBrush(mxr, myr, mxo, myo, drawArea, currentColours[0], int(80-dist(mxo,myo,mxr,myr)))


                    mxo, myo = toolPen(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                else:
                    # Resets the mouse clear flag
                    clearedCursor = False

                    # Clears the screen of cursor
                    drawArea.blit(cursorCache, (0, 0))

                    # Resets position and draws the shape again
                    mxo, myo = mxr, myr
                    toolPen(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)


            # Eraser tool
            # Checks to make sure the palette is not visible to avoid conflicts
            elif currentTool == "Eraser" and not menuOpen:

                if mb[0] == 1:

                    # If the cursor is still on the screen
                    if not clearedCursor:
                        clearedCursor = True

                        # Clear the cursor
                        drawArea.blit(cursorCache, (0, 0))

                    # Draws the eraser and gets the omx,omy
                    mxo, myo = toolEraser(mxr, myr, mxo, myo, drawArea, (255, 255, 255), cursorSize)

                else:
                    # Reflags that cursor is not visiable
                    clearedCursor = False

                    # Draw the cursor
                    drawArea.blit(cursorCache, (0, 0))

                    # Resets old pos
                    mxo, myo = mxr, myr

                    # Draws eraser outline
                    draw.rect(drawArea, (0, 0, 0), (
                        mxr - 1 - 2 * cursorSize, myr - 1 - 2 * cursorSize, 4 * cursorSize + 2, 4 * cursorSize + 2))
                    draw.rect(drawArea, (255, 255, 255),
                              (mxr - 2 * cursorSize, myr - 2 * cursorSize, 4 * cursorSize, 4 * cursorSize))


            # Colour Picker tool
            elif currentTool == "Colour Picker" and canvasRect.collidepoint(mx, my) and not menuOpen:
                clearedCursor = False

                drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                localUnderColour = toolColourPicker(drawArea, mxr, myr)  # Colour detected under hte mouse

                # Draws cross
                draw.line(drawArea, invertColour(localUnderColour), (mxr - 6, myr), (mxr + 6, myr), 2)
                draw.line(drawArea, invertColour(localUnderColour), (mxr, myr - 6), (mxr, myr + 6), 2)

                # Draws preview window
                draw.circle(drawArea, invertColour(localUnderColour), (mxr + 20, myr + 20), 20)
                draw.circle(drawArea, localUnderColour, (mxr + 20, myr + 20), 15)

                if mb[0] == 1:
                    # Clears out colour palette and gets new colours and gradients
                    currentColours = []
                    currentColours.append(localUnderColour)

                    for i in range(-255, 0, 14):
                        # Generates gradients that will always be valid
                        currentColours.append(
                            (abs(localUnderColour[0] + i), abs(localUnderColour[1] + i), abs(localUnderColour[2] + i)))

            elif currentTool == "Text" and not menuOpen:

                # Gets the current font and sets it with the file
                if currentFont == "Ubuntu":
                    textFont = font.Font("fonts/Ubuntu-R.ttf", cursorSize * 3)
                elif currentFont == "TimesNewRoman":
                    textFont = font.Font("fonts/TimesNewRomans.ttf", cursorSize * 3)
                elif currentFont == "ComicSans":
                    textFont = font.Font("fonts/ComicSans.ttf", cursorSize * 3)

                textSurf = textFont.render(textContent, True, currentColours[0])

                drawArea.blit(cursorCache, (0, 0))

                if unclick:
                    textContent = ""

                if mb[0] == 1:
                    if not clearedCursor:  # If the cursor is still on the screen, clear it
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Draws the text
                    drawArea.blit(textSurf, (mxr, myr - textSurf.get_height() // 2))  # Draws text

                else:
                    clearedCursor = False  # Flag that cursor is now visible

                    drawArea.blit(cursorCache, (0, 0))  # Draws the cache

                    # Draws the text preview
                    drawArea.blit(textSurf, (mxr, myr - textSurf.get_height() // 2))  # Draws text

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)

                    draw.rect(drawArea, (0, 0, 0), (
                        mxr, myr - textSurf.get_height() // 2, max(textSurf.get_width(), cursorSize * 2),
                        textSurf.get_height()), 1)

            # Brush Tool
            # Checks to make sure the palette is not visible to avoid conflicts
            elif currentTool == "Brush" and not menuOpen:

                if mb[0] == 1:
                    if not clearedCursor:  # If the cursor is still on the screen, clear it
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Draws the brush
                    mxo, myo = toolBrush(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                else:
                    clearedCursor = False  # Flag that cursor is now visible

                    drawArea.blit(cursorCache, (0, 0))  # Draws the cache

                    mxo, myo = mxr, myr  # Resets the old position

                    # Draws the cursor preview
                    toolBrush(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)



            # Spray Paint tool
            # Checks to make sure the palette is not visible to avoid conflicts
            elif currentTool == "Spray Paint" and not menuOpen:
                if mb[0] == 1:

                    if not clearedCursor:  # Clears the cursor if not done
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Runs the spray paint function
                    mxo, myo = toolSprayPaint(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                else:
                    clearedCursor = False  # Flags that cursor is now on screen
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas
                    draw.circle(drawArea, currentColours[0], (mxr, myr), cursorSize * 2, 2)  # Draws preview circle

                    mxo, myo = mxr, myr

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)


            # Stamps
            elif currentTool[0:5] == "Stamp" and not menuOpen:

                # Gets the stampname from end of tool name
                if currentTool[-1] == "m":
                    stampName = customCursorImage
                else:
                    stampName = stampList[int(currentTool[-1])-1]


                # Makes the stamp dimensions proportional to scroll
                stampW = int((cursorSize / 100) * stampName.get_width())
                stampH = int((cursorSize / 100) * stampName.get_height())

                if mb[0] == 1:  # If the mouse is clicked
                    if not clearedCursor:  # Clears the cursor if not done so
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Blits the scaled stamp
                    drawArea.blit(transform.scale(stampName, (stampW, stampH)), (mxr - stampW // 2, myr - stampH // 2))

                else:

                    clearedCursor = False  # Flags that cursor is on screen
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Blit the stamp preview
                    drawArea.blit(transform.scale(stampName, (stampW, stampH)), (mxr - stampW // 2, myr - stampH // 2))

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)

            elif currentTool == "Polygon" and not menuOpen:

                # Flags that cursor is ALWAYS visible
                clearedCursor = False

                if polygonFill:  # IF the polygon is to be filled, the edge will be set to 0
                    edge = 0
                else:
                    edge = 2

                if click and len(polygonList) == 0:  # Gets the starting polygon location
                    polygonList.append((mxr, myr))

                if unclick:
                    polygonList.append((mxr, myr))  # Gets the points after that

                if not click and len(
                        polygonList) > 0:  # if the mouse is not clicked, draw the cursor along with the segments
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas
                    draw.line(drawArea, currentColours[0], (mxr, myr), polygonList[-1],
                              3)  # Draws latest line being previewed

                    for i in range(len(polygonList) - 1):  # Draws the lines being drawn
                        draw.line(drawArea, currentColours[0], polygonList[i], polygonList[i + 1], 3)

                if polygonList == []:  # If the shape is not being drawn, draw the cursor
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)

                # If the right mouse is clicked or line returns to orgin, clear list
                if (mb[2] == 1 and len(polygonList)>0) or len(polygonList) > 2 and polygonList[0][0] - 5 < polygonList[-1][0] < polygonList[0][0] + 5 and \
                                                polygonList[0][1] - 5 < polygonList[-1][1] < polygonList[0][1] + 5:
                    drawArea.blit(cursorCache, (0, 0))  # Clears canvas

                    draw.polygon(drawArea, currentColours[0], polygonList,
                                 edge)  # Draws the polygon so it may be filled

                    saveAction()

                    polygonList = []  # Resets list



            elif currentTool == "Rectangle" and not menuOpen:
                clearedCursor = False  # Flags that cursor is ALWAY visible

                if polygonFill:  # If shape is to be filled, edge is set to 0
                    edge = 0
                else:
                    edge = 2

                if click:  # If mouse is clicked, record pivot point
                    mxo = mxr
                    myo = myr

                if mb[0] == 1:  # IF mouse is being dragged
                    toolCursor()  # makes cursor visible

                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws the figure
                    draw.rect(drawArea, currentColours[0], (mxo, myo, (mxr - mxo), (myr - myo)), edge)

                else:
                    # Resets canvas
                    drawArea.blit(cursorCache, (0, 0))

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)

            elif currentTool == "Triangle" and not menuOpen:
                clearedCursor = False  # Flags that cursor is ALWAY visible

                if polygonFill:  # If shape is to be filled, edge is set to 0
                    edge = 0
                else:
                    edge = 2

                if len(polygonList) == 3: #When all points have been drawn, stop drawing
                    draw.polygon(drawArea, currentColours[0], polygonList, edge)
                    polygonList = []
                    saveAction()

                if unclick and len(polygonList)>0:
                    polygonList.append((mxr, myr))  # Gets the points after that

                    if polygonList[0] == polygonList[1]: #Removes duplicate
                        polygonList.pop(0)


                if click and len(polygonList) == 0:  # Gets the starting polygon location
                    polygonList.append((mxr, myr))

                if mb[1]==0 and len(polygonList) > 0:  # if the mouse is not clicked, draw the cursor along with the segments
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas
                    draw.line(drawArea, currentColours[0], (mxr, myr), polygonList[-1], 3)  # Draws latest line being previewed

                    draw.line(drawArea, currentColours[0], (mxr, myr), polygonList[0], 3)  # Draws latest line being previewed

                    for i in range(len(polygonList) - 1):  # Draws the lines being drawn
                        draw.line(drawArea, currentColours[0], polygonList[i], polygonList[i + 1], 3)


                if polygonList == []:  # If the shape is not being drawn, draw the cursor
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)


            elif currentTool == "Ellipse" and not menuOpen:

                clearedCursor = False  # Flags cursor ALWAYS visible

                if polygonFill:  # If polygon is to be filled,set edge to 0
                    edge = 0
                else:
                    edge = 2

                if click:  # If mouse is clicked, record locatoin
                    mxo, myo = mxr, myr

                if mb[0] == 1:  # If mouse is dragged
                    toolCursor()  # makes cursor visible

                    drawArea.blit(cursorCache, (0, 0))  # Reset canvas

                    ellipseRect = Rect(mxo, myo, (mxr - mxo), (myr - myo))  # Makes rect for shape
                    ellipseRect.normalize()  # Makes the values positive

                    if 0 < edge < min(abs(mxr - mxo), abs(myr - myo)) // 2:  # If the ellipse is wider than it's edge
                        draw.ellipse(drawArea, currentColours[0], ellipseRect, edge)
                    else:  # Makes the edge 0
                        draw.ellipse(drawArea, currentColours[0], ellipseRect, 0)

                else:  # Otherwise draw cross
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)


            elif currentTool == "Circle" and not menuOpen:
                clearedCursor = False  # Flags cursor as visible

                if polygonFill:  # If polygon is to be filled, set edge to 0
                    edge = 0
                else:
                    edge = 2

                # If the mouse is down, record the initial mouse location
                if click:
                    mxo, myo = mxr, myr

                # If the mouse is being held and dragged
                if mb[0] == 1:
                    toolCursor()  # makes cursor visible

                    # Clears the screen so cursor can move
                    drawArea.blit(cursorCache, (0, 0))

                    if 0 < edge < int(dist(mxo, myo, mxr, myr)):  # If the ellipse is wider than it's edge
                        draw.circle(drawArea, currentColours[0], (mxo, myo), int(dist(mxo, myo, mxr, myr)), edge)
                    else:  # Makes the edge 0
                        draw.circle(drawArea, currentColours[0], (mxo, myo), int(dist(mxo, myo, mxr, myr)), 0)

                else:
                    # If the mouse isnt held, just draw the cursor
                    drawArea.blit(cursorCache, (0, 0))
                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)



            elif currentTool == "Square" and not menuOpen:
                clearedCursor = False  # Flags cursor as visible

                if polygonFill:  # If shape is to be filled, make edge 0
                    edge = 0
                else:
                    edge = 2

                if click:
                    mxo, myo = mxr, myr  # Sets pivor point on initial click

                # If mouse is being dragged
                if mb[0] == 1:
                    toolCursor()  # makes cursor visible

                    # Resets canvas
                    drawArea.blit(cursorCache, (0, 0))

                    w = int(dist(mxo, myo, mxr, myr))
                    h = int(dist(mxo, myo, mxr, myr))

                    # Draws the figure
                    draw.rect(drawArea, currentColours[0], (mxo - w // 2, myo - h // 2, w, h), edge)

                else:
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)



            elif currentTool == "Line" and not menuOpen:
                clearedCursor = False  # Flags line as visible

                if click:
                    mxo, myo = mxr, myr  # If click set initial pivot

                if mb[0] == 1:  # If mouse is dragged

                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    if roundLine:
                        toolBrush(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)
                    else:
                        draw.line(drawArea, currentColours[0], (mxo, myo), (mxr, myr),
                                  cursorSize)  # Draw line to cursor

                else:
                    drawArea.blit(cursorCache, (0, 0))  # Reset canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)


            elif currentTool == "Bucket" and not menuOpen:

                if mb[0] == 1:  # IF mouse is down
                    if not clearedCursor:  # CLears the cursor
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # FIlls the area
                    floodFill(mxr, myr, drawArea, currentColours[0])

                else:
                    clearedCursor = False  # Flags cursor is now on
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)




            elif currentTool == "Marker" and not menuOpen:
                if mb[0] == 1:
                    if not clearedCursor:  # Clear the cursor
                        clearedCursor = True
                        drawArea.blit(cursorCache, (0, 0))

                    # Draw the marker
                    mxo, myo = toolMarker(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                else:
                    clearedCursor = False  # Flag cursor as visible
                    drawArea.blit(cursorCache, (0, 0))  # Resets canvas

                    mxo, myo = mxr, myr  # Resets mouse position

                    # Marker preview
                    toolMarker(mxr, myr, mxo, myo, drawArea, currentColours[0], cursorSize)

                    # Draws cross
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr - 11, myr), (mxr + 11, myr), 4)
                    draw.line(drawArea, invertColour(currentColours[0]), (mxr, myr - 11), (mxr, myr + 11), 4)

                    draw.line(drawArea, currentColours[0], (mxr - 12, myr), (mxr + 12, myr), 2)
                    draw.line(drawArea, currentColours[0], (mxr, myr - 12), (mxr, myr + 12), 2)

        # Tools end
        # ____________________________________________________________________________________________________________
        # SUBWINDOWS START

        # ABout window
        if aboutVisible:
            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))  # Draws the contents of the screen before the window

            screen.blit(backDrop, (0, 0))  # Makes it darker

            # Draws the window
            draw.rect(screen, (240, 240, 240), (365, 100, 550, 420))

            # Draws the close button
            draw.rect(screen, (230, 230, 230), loadFileButton)

            # Text dialogs
            screen.blit(ubuntuFont.render("Mike-ro-soft Paint 2.0", True, (0, 0, 0)), (390, 115))
            screen.blit(ubuntuFontSmall.render("created by Henry Tu", True, (80, 80, 80)), (390, 143))

            screen.blit(ubuntuFontSmall.render("Created for ICS3U midterm 2016", True, (80, 80, 80)), (390, 183))
            screen.blit(ubuntuFontSmall.render("Microsoft paint clone", True, (80, 80, 80)), (390, 198))
            screen.blit(ubuntuFontSmall.render("Icons courtesy of icons8.com", True, (80, 80, 80)), (390, 213))

            screen.blit(snowden, (490, 245))

            # If mouse i on button
            if loadFileButton.collidepoint(mx, my):
                # Draw the hover button
                draw.rect(screen, BUTTONHOVER, loadFileButton)

            # Text on button
            screen.blit(ubuntuFont.render("Close", True, (0, 0, 0)), (440, 455))

            if loadFileButton.collidepoint(mx, my):

                # But if the mouse is alsodown
                if unclick:
                    menuOpen = False
                    aboutVisible = False

                    # Restores background
                    draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                    drawArea.blit(cursorCache, (0, 0))

            if not aboutWindowRect.collidepoint(mx, my) and unclick:  # if mouse is not on window and click
                menuOpen = False  # Click window
                aboutVisible = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))

        if helpPromptVisible:

            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))

            screen.blit(backDrop, (0, 0))  # Transparent background

            draw.rect(screen, (255, 255, 255), (10, 0, 60, 50), 2)
            draw.rect(screen, (255, 255, 255), (430, 0, 300, 50), 2)
            draw.rect(screen, (255, 255, 255), (1150, 0, 120, 50), 2)
            draw.rect(screen, (255, 255, 255), (1050, 150, 190, 200), 2)

            draw.rect(screen, (255, 255, 255), (1020, 530, 250, 130), 2)

            draw.rect(screen, (255, 255, 255), (1020, 660, 250, 60), 2)

            draw.rect(screen, (255, 255, 255), (15, 680, 500, 40), 2)

            screen.blit(ubuntuFontSmall.render("Additional Actions", True, (255, 255, 255)), (10, 50))

            screen.blit(ubuntuFontSmall.render("Tool categories", True, (255, 255, 255)), (430, 50))

            screen.blit(ubuntuFontSmall.render("Undo/Redo", True, (255, 255, 255)), (1150, 50))

            screen.blit(ubuntuFontSmall.render("Tool selection", True, (255, 255, 255)), (1050, 350))

            screen.blit(transform.rotate(ubuntuFontSmall.render("Colour Gradients", True, (255, 255, 255)), 90),
                        (1000, 540))

            screen.blit(ubuntuFontSmall.render("Colour Palette", True, (255, 255, 255)), (1030, 680))

            screen.blit(ubuntuFontSmall.render("Information pane", True, (255, 255, 255)), (10, 660))

            closeHelpButton = Rect(390, 390, 500, 48)

            # Draws the window
            draw.rect(screen, (240, 240, 240), (365, 250, 550, 200))

            # Draws the close button
            draw.rect(screen, BUTTONCOL, closeHelpButton)

            screen.blit(pepe, (385, 290))

            # Draws titles
            screen.blit(ubuntuFont.render("It looks like you need some help", True, (0, 0, 0)), (465, 310))

            if closeHelpButton.collidepoint(mx, my):

                draw.rect(screen, BUTTONHOVER, closeHelpButton)

                # But if the mouse is alsodown
                if unclick:
                    menuOpen = False
                    helpPromptVisible = False
                    # Restores background
                    draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                    drawArea.blit(cursorCache, (0, 0))

                    continue

            # Text on button
            screen.blit(ubuntuFont.render("K bai, help is for weak btw", True, (0, 0, 0)), (440, 395))

            if not helpPromptRect.collidepoint(mx, my) and unclick:  # if mouse is not on window and click
                menuOpen = False  # Click window
                helpPromptVisible = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))

        # if the left drawer is open
        if drawerVisible:
            menuOpen = True  # Indicates a menu is open so that screen locks

            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))

            # Creates a translucent backdrop
            screen.blit(backDrop, (0, 0))

            if not drawnDrawer:  # If the drawer is not drawn
                drawnDrawer = True
                for x in range(0, 400, 2):  # Draw drawer sliding open
                    draw.rect(screen, (248, 248, 248), (0, 0, x, 700))
                    display.flip()

            # Redraws drawer
            draw.rect(screen, (248, 248, 248), (0, 0, 400, 700))

            # Draws highlight
            draw.rect(screen, BUTTONHOVER, (0, 0, 400, 50))

            # Draws buttons
            for y in range(6):
                draw.rect(screen, (250, 250, 250), (0, 50 + 60 * y + 2, 400, 57))

            # Draws buttons being hovered
            if mouseInRange(mx, my, 0, 50, 400, 360):
                mouseIndex = (my - 50) // 60

                draw.rect(screen, BUTTONHOVER, (0, 50 + 60 * mouseIndex + 2, 400, 57))

            # Draws the titles
            screen.blit(ubuntuFont.render("New", True, (90, 90, 90)), (50, 60))
            screen.blit(ubuntuFont.render("Open", True, (90, 90, 90)), (50, 120))
            screen.blit(ubuntuFont.render("Save", True, (90, 90, 90)), (50, 180))
            screen.blit(ubuntuFont.render("Save As", True, (90, 90, 90)), (50, 240))
            screen.blit(ubuntuFont.render("About", True, (90, 90, 90)), (50, 300))
            screen.blit(ubuntuFont.render("Help", True, (90, 90, 90)), (50, 360))

            # Draws the icons
            screen.blit(newIcon, (10, 62))
            screen.blit(importIcon, (10, 122))
            screen.blit(saveIcon, (10, 182))
            screen.blit(saveasIcon, (10, 242))
            screen.blit(aboutIcon, (10, 302))
            screen.blit(helpIcon, (10, 362))

            # If button is clicked
            if mouseInRange(mx, my, 0, 50, 400, 360):

                mouseIndex = (my - 50) // 60

                if unclick:  # If mouse released

                    # New
                    if mouseIndex == 0:

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

                        # If the save prompt is not open yet
                        if actionMade:
                            if not savePromptVisible:
                                paletteVisible = False  # Closes all other subwindows
                                drawerVisible = False
                                aboutVisible = False
                                savePromptVisible = True
                                helpPromptVisible = False
                                graphPromptVisible = False
                                menuOpen = True

                                nextAction = "clear"

                                endTime = unixTime  # Sets endTime to time of clicking close

                        else:
                            menuOpen = False
                            drawerVisible = False


                    # Open
                    elif mouseIndex == 1:
                        drawerVisible = False
                        menuOpen = False

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

                        fileName = loadPhotoNewFile(drawArea, fileName, undoList, redoList)

                        saveAction()  # Saves the action that was just performed for undo list
                        undoList = []
                        undoList.append(drawArea.copy())  # Adds the screen to the list
                        redoList = []  # Clears the redo list because they are no longer valid



                    # Save
                    elif mouseIndex == 2:

                        if fileName == "Untitled":  # If name is not set, prompt
                            tempFileName = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

                        if tempFileName:  # Check is name is valid

                            drawerVisible = False
                            menuOpen = False

                            # Restores background
                            draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                            drawArea.blit(cursorCache, (0, 0))

                            image.save(drawArea, tempFileName)  # Save canvas
                            fileName = tempFileName  # Sets name and close
                            actionMade = False  # Resets counters for save
                            startTime = None
                            actionsMade = 0

                    # Save as
                    elif mouseIndex == 3:


                        # Get file name for saving
                        tempFileName = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

                        if tempFileName:
                            # Closes menu
                            drawerVisible = False
                            menuOpen = False

                            # Restores background
                            draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                            drawArea.blit(cursorCache, (0, 0))

                            image.save(drawArea, tempFileName)  # Saves canvas
                            # Sets file name
                            fileName = tempFileName
                            actionMade = False  # Resets save counter
                            startTime = None
                            actionsMade = 0



                    # ABout
                    elif mouseIndex == 4:
                        drawerVisible = False  # Opens about menu
                        aboutVisible = True

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

                    # Help page
                    elif mouseIndex == 5:
                        drawerVisible = False  # Opens about menu
                        helpPromptVisible = True

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

            # Easy close
            if unclick and mouseInRange(mx, my, 400, 0, 8000, 700):
                drawerVisible = False  # Close drawer
                menuOpen = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))

        # If the paint palette is requested to be displayed
        # Put at the end to ensure the objects under it can still be seen
        if paletteVisible:
            menuOpen = True

            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))

            # Creates a translucent backdrop
            screen.blit(backDrop, (0, 0))

            # Message
            screen.blit(ubuntuFont.render("Select a colour to use", True, (255, 255, 255)), (390, 70))

            # mouse relative to palette
            mxrp = mx - 390
            myrp = my - 100

            paletteSurface.blit(colourPicker, (0, 0))  # Colour picker

            # Creates button to close the palette
            draw.rect(screen, BUTTONCOL, paletteCloseButtonRect)

            # If mouse hits the button
            if paletteCloseButtonRect.collidepoint(mx, my):
                draw.rect(screen, BUTTONHOVER, paletteCloseButtonRect)

            screen.blit(ubuntuFont.render("Close", True, (0, 0, 0)), (600, 618))

            # If the close button is hit
            if paletteCloseButtonRect.collidepoint(mxs, mys) and unclick:
                # Draws the click button
                paletteVisible = False
                menuOpen = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))

            # Checks if mouse is on colour Picker
            if paletteRect.collidepoint(mx, my):
                mouse.set_visible(False)
                # Turns the cursor off so that we can apply a custom one

                localUnderColour = toolColourPicker(screen, mx, my)  # Colour detected under hte mouse

                draw.line(paletteSurface, invertColour(localUnderColour), (mxrp - 6, myrp), (mxrp + 6, myrp), 2)
                draw.line(paletteSurface, invertColour(localUnderColour), (mxrp, myrp - 6), (mxrp, myrp + 6), 2)
                # Draws a cross cursor with inverted colours for visibility

                draw.circle(paletteSurface, invertColour(localUnderColour), (mxrp + 20, myrp + 20), 20)
                draw.circle(paletteSurface, localUnderColour, (mxrp + 20, myrp + 20), 15)
                # Draws a preview window circle with the hovered colour


                if mb[0] == 1:

                    rainbow = False

                    # Clears out colour palette and gets new colours and gradients
                    currentColours = []
                    currentColours.append(localUnderColour)

                    # adds the newly selected colour into colour list and generates some colours that are similar
                    for i in range(-255, 0, 14):
                        # Generates gradients that will always be valid
                        currentColours.append(
                            (abs(localUnderColour[0] + i), abs(localUnderColour[1] + i), abs(localUnderColour[2] + i)))

            # EASY CLOSE
            """
            if not mouseInRange(mx,my, 390, 100, 500, 500) and unclick:
                paletteVisible = False
                menuOpen = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))
            """

        if graphPromptVisible:

            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))

            screen.blit(backDrop, (0, 0))  # Transparent background


            # Draws the  window
            draw.rect(screen, (240, 240, 240), (365, 280, 550, 140))

            # Draws titles
            screen.blit(ubuntuFontSmall.render("Input equation to be graphed:", True, (0, 0, 0)),
                        (375, 290))

            #Textbox
            draw.rect(screen, (250,250,250), (375, 320, 530, 35))
            screen.blit(ubuntuFont.render(textContent, True, (0, 0, 0)), (380, 315))


            # Draws buttons
            draw.rect(screen, (230, 230, 230), (375, 360, 170, 50))
            draw.rect(screen, (230, 230, 230), (555, 360, 170, 50))

            #Cancel
            if mouseInRange(mx, my, 375, 360, 170, 50):
                draw.rect(screen, BUTTONHOVER, (375, 360, 170, 50))  # Hover button

                if unclick:
                    currentTool = "Brush" #Resets tool
                    graphPromptVisible = False #Closes windows
                    menuOpen = False

                    textContent = "" #Resets textbox

                    # Restores background
                    draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                    drawArea.blit(cursorCache, (0, 0))


            #Graph it
            if mouseInRange(mx, my, 555, 360, 170, 50):
                draw.rect(screen, BUTTONHOVER, (555, 360, 170, 50))  # Hover button
                if unclick:
                    currentTool = "Brush" #Resets tools
                    graphPromptVisible = False #Closes windows
                    menuOpen = False

                    # Restores background
                    draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                    drawArea.blit(cursorCache, (0, 0))

                    screenX = 960 #Screen size
                    screenY = 600
                    scale = cursorSize #Scaling controlled by cursor
                    unit = 1 #We're counting by 1s here


                    #Goes from left to right to draw lines
                    for i in range((-1 * screenX // 2) * scale * unit, (screenX // 2) * scale * unit):

                        #Try and except incase something weird is entered
                        try:
                            x = i / (scale ** 2 * unit) #Gets the scaled x value
                            y = eval(textContent)  #Uses equation to calculate Y value
                            xPos = screenX // 2 + i // (scale * unit) #the X and Y value and offsets it
                            yPos = screenY // 2 - (y * scale / unit)
                            draw.rect(drawArea, currentColours[0], [xPos, yPos, 2, 2]) #Draws the line

                        except: #Terminate operation if something goes wrong
                            break

                    saveAction()

                    textContent = ""

            screen.blit(ubuntuFont.render("Cancel", True, (80, 80, 80)), (380, 363))
            screen.blit(ubuntuFont.render("Graph it!", True, (80, 80, 80)), (560, 363))



        if savePromptVisible:

            draw.rect(screen, BACKGROUND, (0, 50, 1000, 630))  # Back ground
            drawArea.blit(cursorCache, (0, 0))

            screen.blit(backDrop, (0, 0))  # Transparent background

            # Draws the  window
            draw.rect(screen, (240, 240, 240), (365, 280, 550, 140))

            # Draws titles
            screen.blit(ubuntuFontSmall.render("Would you like to save your master piece?", True, (0, 0, 0)),
                        (375, 290))
            screen.blit(
                ubuntuFontSmall.render("If not saved, pressing 'Discard' will destroy your creation, so choose wisely",
                                       True, (0, 0, 0)), (375, 310))
            screen.blit(ubuntuFontSmall.render((str(endTime - startTime) + " second(s) of work and " + str(
                actionsMade) + " action(s) will be lost if not saved"), True, (255, 0, 0)), (375, 330))

            # Draws buttons
            draw.rect(screen, (230, 230, 230), (375, 360, 170, 50))
            draw.rect(screen, (230, 230, 230), (555, 360, 170, 50))
            draw.rect(screen, (230, 230, 230), (735, 360, 170, 50))

            # DISCARD BUTTON
            if mouseInRange(mx, my, 375, 360, 170, 50):
                draw.rect(screen, BUTTONHOVER, (375, 360, 170, 50))  # Hover button

                if unclick:
                    if nextAction == "close":
                        running = False  # Kills program
                    elif nextAction == "clear":  # When the new file button is clicked
                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

                        actionMade = False  # Reset save times
                        startTime = None
                        actionsMade = 0

                        fileName, drawArea, undoList, redoList = clear_canvas(fileName, drawArea, undoList, redoList)
                        menuOpen = False  # Close window
                        savePromptVisible = False

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

            # SAVE BUTTON
            if mouseInRange(mx, my, 555, 360, 170, 50):
                draw.rect(screen, BUTTONHOVER, (555, 360, 170, 50))  # Hover button
                if unclick:

                    if fileName == "Untitled":  # Checks if file name is set

                        # Gets file name from user
                        tempFileName = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'),\
                     ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])

                    if tempFileName:  # Checks if name is valid
                        fileName = tempFileName
                        drawerVisible = False
                        menuOpen = False

                        # Restores background
                        draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                        drawArea.blit(cursorCache, (0, 0))

                        image.save(drawArea, fileName)  # Save image
                        actionMade = False  # Reset save times
                        startTime = None
                        actionsMade = 0

                        if nextAction == "close":
                            running = False  # Kills program
                        elif nextAction == "clear":  # When the new file button is clicked
                            fileName, drawArea, undoList, redoList = clear_canvas(fileName, drawArea, undoList,
                                                                                  redoList)
                            menuOpen = False  # Close window
                            savePromptVisible = False

                            # Restores background
                            draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                            drawArea.blit(cursorCache, (0, 0))


            # CANCEL BUTTON
            if mouseInRange(mx, my, 735, 360, 170, 50):
                draw.rect(screen, BUTTONHOVER, (735, 360, 170, 50))  # Highlight button

                if unclick:
                    menuOpen = False  # Close window
                    savePromptVisible = False

                    # Restores background
                    draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                    drawArea.blit(cursorCache, (0, 0))

                    continue

            # Draws titles
            screen.blit(ubuntuFont.render("Discard", True, (80, 80, 80)), (380, 363))
            screen.blit(ubuntuFont.render("Save", True, (80, 80, 80)), (560, 363))
            screen.blit(ubuntuFont.render("Cancel", True, (80, 80, 80)), (740, 363))

            # Easy close
            if not mouseInRange(mxs, mys, 365, 280, 550, 140) and unclick and nextAction != "clear":
                menuOpen = False
                savePromptVisible = False

                # Restores background
                draw.rect(screen, BACKGROUND, (0, 0, 1280, 700))  # Back ground
                drawArea.blit(cursorCache, (0, 0))

    # __________________________________________________________________________________________________________________
    # SUBWINDOWS END

    clock.tick()  # Advances the clock for FPS
    display.flip()  # Updates the screen

display.quit()
quit()

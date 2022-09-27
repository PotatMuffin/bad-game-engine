from tkinter import TclError, Button, Tk, Canvas
from .game_object import Game_Object
from time import sleep

class Scene:
    def __init__(self, objects:list[Game_Object], name:str="", width="900", height="600", bg:str="#ffffff", fps=60):
        self.__new_objects:list[Game_Object] = []
        self.__active_objects:list[Game_Object] = []
        self.__destroyed_objects:list[Game_Object] = []

        self.__name = name
        self.__width = width
        self.__height = height
        self.__bg = bg
        self.__fps = fps
      
        for obj in objects:
            self.__new_objects.append(obj)
        
    def close(self):
        pass

    def init_game_object(self, *obj:Game_Object):
        for object in obj:
            self.__new_objects.append(object)
    
    def destroy_game_object(self, obj:Game_Object):
        self.__active_objects.remove(obj)
        self.__destroyed_objects.append(obj)
    
    def startloop(self):
        delta = 0
        # creates the window and canvas for the game
        self.__window = Tk()
        self.__window.title(self.__name)
        self.__window.resizable(False, False)

        self.__canvas = Canvas(self.__window, width=self.__width, height=self.__height, bg=self.__bg)
        self.__canvas.pack()

        # a dictionary with references to functions for the shapes 
        shapes = {
            'rect': self.__canvas.create_rectangle,
            'oval': self.__canvas.create_oval,
            'arc': self.__canvas.create_arc
        }

        while True:
            sleep(1/self.__fps)
            # taking the objects from __new_objects and puts it in __active_objects
            for _ in range(len(self.__new_objects)):
                obj = self.__new_objects.pop(0)
                self.__active_objects.append(obj)

            # removing the destroyed objects from the scene
            for obj in self.__destroyed_objects:
                self.__canvas.delete(obj.uuid)
                obj.on_destroy()
            
            self.__destroyed_objects.clear()

            # rendering the objects in __active_objects
            for obj in self.__active_objects:
                self.__canvas.delete(obj.uuid)
                shapes[obj.shape](obj.transform.position.x, obj.transform.position.y, obj.transform.width+obj.transform.position.x, obj.transform.position.y+obj.transform.height, fill=obj.colour, outline=obj.colour, tags=obj.uuid)

            # calls the update method of every object in __active_objects
            for obj in self.__active_objects:
                obj.update()

            self.__window.update()
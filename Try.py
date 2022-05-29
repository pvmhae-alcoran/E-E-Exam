from tkinter import *
import time


root = Tk()
root.title("Stop Watch")
root.geometry("299x350")
root.wm_attributes("-topmost", 1)


class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.e = 0
        self.m = 0
        self.makeWidgets()
        self.lap = ""
        self.laps = []
        self.lapmod2 = 0
        self.today = time.strftime("%d %b %Y %H-%M-%S", time.localtime())


    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr,font=("Times 40 bold"),bg="white")
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=3, padx=2)

        l2 = Label(self, text='---laps---', font=("Times 20 bold"),bg="sky blue")
        l2.pack(fill=X, expand=NO, pady=4, padx=2)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, font=("Times 15"), height = 5,
                         yscrollcommand=scrollbar.set)
        self.m.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=2)
        scrollbar.config(command=self.m.yview)
        scrollbar.pack(side=RIGHT, fill=Y)


    def update(self):

        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self.update)

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        milliseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, milliseconds))
        self.lap = '%02d:%02d:%02d' % (minutes, seconds, milliseconds)


    def _setLapTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        milliseconds = int((elap - minutes*60.0 - seconds)*100)            
        return '%02d:%02d:%02d' % (minutes, seconds, milliseconds)


    def Start(self):
        start_.place_forget()
        stop_.place(x=0,y=250, width= 100, height= 30)
        reset_.place_forget()
        lap_.place(x=100,y=250, width= 100, height= 30)
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self.update()
            self._running = 1


    def Stop(self):
        stop_.place_forget()
        start_.place(x=0,y=250, width= 100, height= 30)
        lap_.place_forget()
        reset_.place(x=100,y=250, width= 100, height= 30)
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0


    def Reset(self):
        reset_.place_forget()
        lap_.place(x=100,y=250, width= 100, height= 30)
        self.after_cancel(self._timer)  
        self._elapsedtime = 0.0
        self.laps = []
        self._setTime(self._elapsedtime)
        self._running = 0
        self.m.delete(0,END)


    def Lap(self):
        tempo = self._elapsedtime - self.lapmod2
        if self._running:
            self.laps.append(self.lap)
            self.m.insert(END, self.laps[-1])
            self.m.yview_moveto(1)
            self.lapmod2 = self._elapsedtime


sw = StopWatch(root)
sw.pack(side=TOP)


start_ = Button(root, text='Start', command=sw.Start, font=("Times 15"),bg=("#39FF14"))
lap_ = Button(root, text='Lap', command=sw.Lap, font=("Times 15"),bg=("silver"))
stop_ = Button(root, text='Stop', command=sw.Stop, font=("Times 15"),bg=("#ff0f0f"))
reset_ = Button(root, text='Reset', command=sw.Reset, font=("Times 15"),bg=("silver"))
    

start_.place(x=0,y=250, width= 100, height= 30)
lap_.place(x=100,y=250, width= 100, height= 30)


root.mainloop()

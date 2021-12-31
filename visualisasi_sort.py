from tkinter import *
import time
import random

root = Tk()
root.title('Aplikasi Visualisasi Quick Sort & Heap Sort')
root.geometry("880x640")
root.config (bg='white')

arr1 = []
arr2 = []
time_start = time.time()

def arrayVisual(arr, color, canvas):
    canvas.delete("all")
    c_width = 340
    c_height = 240
    x_width = c_width / (len(arr) + 1)
    offset = 10
    space = 5
    normalizedarr = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalizedarr):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 210
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    root.update_idletasks()

def randomArray():
    global arr1
    global arr2
    arr1 = []  
    arr2 = []
    
    length = int(inputN.get())
    for _ in range(length):
        arr1.append(random.randrange(1, 100))
    arr2[:] = arr1[:]
    arrayVisual(arr1,['red' for x in range(len(arr1))],canvas1)
    arrayVisual(arr2,['red' for x in range(len(arr2))],canvas2)


def partition(array,l,h):
    global time_start
    time_start = time.time() 

    i = ( l-1 )          
    p = array[h]     
  
    for j in range(l, h): 
        if   array[j] < p: 
            i = i+1 
            array[i],array[j] = array[j],array[i]
  
    array[i+1],array[h] = array[h],array[i+1] 
    
    return ( i+1 ) 
  
 
def quickSort(a,l,h, arrayVisual, canvas): 
    global time_start
    time_start = time.time()

    if l<h: 
        pin = partition(a,l,h)       
        quickSort(a, l, pin-1, arrayVisual, canvas)
        arrayVisual(a, ['green' if x == pin or x == pin+1 else 'red' for x in range(len(a))], canvas)
        updateTime(runTime2,time_start)   
        quickSort(a, pin+1, h, arrayVisual, canvas)
        arrayVisual(a, ['green' if x == pin or x == pin+1 else 'red' for x in range(len(a))], canvas)
        updateTime(runTime2,time_start)   

    arrayVisual(a, ['green' for x in range(len(a))], canvas)


###################### HEAP SORT #####################  
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr,arrayVisual,canvas):
    global time_start
    time_start = time.time()

    n = len(arr)
  
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        arrayVisual(arr, ['green' if x == i or x == i+1 else 'red' for x in range(len(arr))], canvas)
        updateTime(runTime1,time_start)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        arrayVisual(arr, ['green' if x == i or x == i+1 else 'red' for x in range(len(arr))], canvas)
        updateTime(runTime1,time_start)

    arrayVisual(arr, ['green' for x in range(len(arr))], canvas)
#########################################################

def run():
    global arr1
    global arr2

    heapSort(arr1, arrayVisual, canvas1)
    quickSort(arr2, 0, len(arr2)-1, arrayVisual, canvas2)

def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)
    
########################### User Interface #########################################
frameTombol = Frame(root, width = 720, height = 50, bg ='white')
frameTombol.grid(row = 0, column=0, padx =10, pady=10)

Label(frameTombol, text="Banyak elemen array:", bg= 'white').grid(row=0, column=0, padx=5,pady=5)
inputN = Entry(frameTombol)
inputN.grid(row=1, column=0, padx=5,pady=5)

tombolRandm =Button(frameTombol, text="Random Array", command=randomArray)
tombolRandm.grid(row=1, column=3, padx=5, pady=5)

tombolMulai = Button(frameTombol, text="Start", command=run)
tombolMulai.grid(row=1, column=5, padx=5, pady=5)

canvas1 = Canvas(root, width=340, height=240, bg = 'grey')
canvas1.grid(row=1, column=0, padx=10, pady=10)

canvas2 = Canvas(root, width=340, height=240, bg = 'grey')
canvas2.grid(row=2, column=0, padx=10, pady=10)

frameText1 = Frame(root, width = 720, height = 50, bg='white')
frameText1.grid(row= 1,column=1, padx=100,pady=100,sticky=W)
Label(frameText1,text="Heap Sort\n\nRunning Time (detik):\n\n",bg='white').grid(row=1,column=0)
runTime1 = Label(frameText1, text="",bg = "white")
runTime1.grid(row=1, column=1,pady=20,padx=40)

frameText2 = Frame(root, width = 720, height = 50, bg='white')
frameText2.grid(row= 2,column=1, padx=100,pady=100,sticky=W)
Label(frameText2,text="Quick Sort\n\nRunning Time (detik):\n\n",bg='white').grid(row=2,column=0)
runTime2 = Label(frameText2, text="", bg = "white")
runTime2.grid(row=2, column=1,pady=20,padx=40)
###################################################################################

root.mainloop()
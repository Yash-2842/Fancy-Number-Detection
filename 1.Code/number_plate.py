from tkinter import *
from tkinter import filedialog as fd
import cv2
import imutils
import pytesseract
from matplotlib import pyplot as plt
from api import *
import requests

list=[0,1,2,3,4,5,6,7,8,9]
def number_detect_bike(path):
    pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = cv2.imread(path)
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    edged = cv2.Canny(gray, 170, 200)
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()
    cv2.drawContours(image1, cnts, -1, (0,255,0),3)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    cnts = sorted(cnts, key= cv2.contourArea, reverse= True)[:30]
    NumberPlateCount = None
    image2 = image.copy()
    cv2.drawContours(image2, cnts, -1, (0,255,0),3)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    count = 0
    name = 1
    for i in cnts:
        perimeter = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02*perimeter, True)
        if(len(approx) == 4):
            NumberPlateCount = approx
            x, y, w, h = cv2.boundingRect(i)
            crp_img = image[y:int(y+h/2), x:x+w]
            crp_img1 = image[int(y+h/2)-5:y+h ,x:x+w]
            print(x,y)
            cv2.imwrite(str(name)+ '.png',crp_img)
            cv2.imwrite(str(name)+ '1.png', crp_img1)
            name += 1
            break
    cv2.drawContours(image,[NumberPlateCount], -1,(0,255,0),3)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    crop_img_loc = cv2.imread('1.png')
    crop_img_loc1=cv2.imread('11.png')
    plt.imshow(cv2.cvtColor(crop_img_loc, cv2.COLOR_BGR2RGB))
    plt.imshow(cv2.cvtColor(crop_img_loc1, cv2.COLOR_BGR2RGB))
    text = pytesseract.image_to_string(crop_img_loc, config ='--psm 6')
    text += pytesseract.image_to_string(crop_img_loc1, config='--psm 6')
    print(text)
    t1=""
    for i in range(0, 3):
        if text[i].isalpha():
            t1 += text[i]

    for i in range(3, len(text)):
        if text[i].isalnum():
            t1 += text[i]

    print(f"Number is : {t1}")
    # text1 = Label(text=t1,font=("Times New Roman",20,"bold"))
    # text1.place(x=490,y=250)
    label = Label(width=60, bg="#241571", fg="white",height=2,font=("Courier",10,'bold'))
    label.place(x=350, y=480)
    label.config(text=t1)
    response = requests.get(f"http://127.0.0.1:5000/{t1}")
    n = response.json()
    T = Label(width=50, bg="#241571", fg="white", height=3, font=("Courier", 15, 'bold'))
    T.config(text=f"name: {n['name']}\nemail:{n['email-id']}\nAdhar-no:{n['adhaar-no']} ")
    T.place(x=280, y=560)
    plt.show()
def number_detect_car(path):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image = cv2.imread(path)
        image = imutils.resize(image, width=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
        edged = cv2.Canny(gray, 170, 200)
        plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
        cnts, new = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        image1 = image.copy()
        cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
        plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
        NumberPlateCount = None
        image2 = image.copy()
        cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
        plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
        count = 0
        name = 1
        for i in cnts:
            perimeter = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
            if (len(approx) == 4):
                NumberPlateCount = approx
                x, y, w, h = cv2.boundingRect(i)
                crp_img = image[y:y + h, x:x + w]
                cv2.imwrite(str(name) + '.png', crp_img)
                name += 1
                break
        cv2.drawContours(image, [NumberPlateCount], -1, (0, 255, 0), 3)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        crop_img_loc = cv2.imread('1.png')
        plt.imshow(cv2.cvtColor(crop_img_loc, cv2.COLOR_BGR2RGB))
        text = pytesseract.image_to_string(crop_img_loc, config='--psm 6')
        t1 = ""
        for i in text:
            if i.isalnum():
                t1 += i
        print(f"Number is : {t1}")
        # text1 = Label(text=t1,font=("Times New Roman",20,"bold"))
        # text1.place(x=490,y=250)
        label = Label(width=48, bg="#241571", fg="white", height=2, font=("Courier", 18, 'bold'))
        label.place(x=220, y=480)
        label.config(text=t1)
        response = requests.get(f"http://127.0.0.1:5000/{t1}")
        n= response.json()
        print(n)
        # print(n['name'])
        T = Label(width=50, bg="#241571", fg="white", height=3, font=("Courier", 15, 'bold'))
        T.config(text=f"name: {n['name']}\nemail:{n['email-id']}\nAdhar-no:{n['adhaar-no']} ")
        T.place(x=280, y=560)
        #plt.show()

def openfile_car():
    path = fd.askopenfile()
    print(path.name)
    number_detect_car(path.name)

def openfile_bike():
    path = fd.askopenfile()
    print(path.name)
    number_detect_bike(path.name)







from tkinter import *

# import prompt_toolkit.layout.processors
from PIL import ImageTk,Image
#green=#20bf87
window=Tk()
window.title("NUMBER PLATE DETECTION")
#width,height
window.geometry("1100x675")
window.config(bg="white")
# window.config(padx=20,pady=20)



canvas1 = Canvas(height=20,width=1099,bg="#273386")
canvas1.grid(row=0,column=0,columnspan=3)
#Canvas Layout
canvas2 = Canvas(height=90,width=250,bg="white",highlightthickness=0)
img=ImageTk.PhotoImage(Image.open("name3.jpg"))
canvas2.create_image(110,40,image=img) #140,40
canvas2.grid(row=1,column=0,sticky=W)
#plate creator
canvas3 = Canvas(height=90,width=150,highlightthickness=0,bg="white")#bg="white
img1=ImageTk.PhotoImage(Image.open("check.jpg"))
canvas3.create_image(30,40,image=img1)
canvas3.create_text(103,40,text="Plate Creator",font=("Times New Roman",12,"bold"),fill="#273386")
canvas3.place(x=230,y=22)

#accessories rgb(238, 182, 14)
canvas4 = Canvas(height=90,width=150,highlightthickness=0,bg="white")#bg="white
img2=ImageTk.PhotoImage(Image.open("plus.jpg"))
canvas4.create_image(30,40,image=img2)
canvas4.create_text(110,40,text="Accessories",font=("Times New Roman",12,"bold"),fill="#273386")
canvas4.place(x=382,y=22)

#brush
canvas5 = Canvas(height=90,width=170,highlightthickness=0,bg="white")#bg="white
img3=ImageTk.PhotoImage(Image.open("brush.jpg"))
canvas5.create_image(30,40,image=img3)
canvas5.create_text(120,40,text="Design service",font=("Times New Roman",12,"bold"),fill="#273386")
canvas5.place(x=539,y=22)

#contact us
canvas6 = Canvas(height=90,width=158,highlightthickness=0,bg="white")#bg="white
img4=ImageTk.PhotoImage(Image.open("contact.jpg"))
canvas6.create_image(30,40,image=img4)
canvas6.create_text(110,40,text="Contact Us",font=("Times New Roman",12,"bold"),fill="#273386")
canvas6.place(x=930,y=22)

#BODY
canvas7 = Canvas(height=20,width=1099,bg="#20bf87")
canvas7.place(x=0,y=105)

#BACKIMG
canvas8 = Canvas(height=200,width=1099,bg="red")
img5=ImageTk.PhotoImage(Image.open("backimg.jpg"))
canvas8.create_image(550,102,image=img5)
canvas8.create_text(580,50,text="Car & Bike Plates",fill="white",font=("sans-serif",20,"bold"))
canvas8.create_text(550,100,text="NO.1 NUMBER PLATE RECOGNIZER ",fill="white",font=("sans-serif",20,"bold"))
# text=Label(text="NUMBER PLATE NUMBER",fg="#273386",bg="white",height=2,width=30)
# text.place(x=490,y=250)
canvas8.place(x=0,y=126)

#LABEL
my=Label(text="CUSTOMIZATION OF CAR&BIKE PLATES",font=("Times New Roamn",19,"bold"),fg="#273386",bg="white")
my.place(x=320,y=350)

#REST PART
car_b=Button(text="CAR",bg="#241571",activebackground="#48AAAD",width=30,font=("Times New Roamn",12,"bold"),fg="white",command=openfile_car)
car_b.place(x=220,y=400)

bike_b=Button(text="BIKE",bg="#241571",activebackground="#48AAAD",width=30,font=("Times New Roamn",12,"bold"),fg="white",command=openfile_bike)
bike_b.place(x=598,y=400)
#BUTTON
# button=Button(text="Click Me",bg="#241571",activebackground="#48AAAD",width=40,font=("Times New Roamn",12,"bold"),fg="white",command=openfile)
# button.bind("<Enter>",onButton)
# button.bind("<Leave>",leaveButton)
# button.place(x=390,y=510)
#NUMBER PLATE DISPLAY
window.mainloop()
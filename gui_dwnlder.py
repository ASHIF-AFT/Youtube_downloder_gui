from pytube import YouTube
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *

file_size=0

def startDownload():
    global file_size
    try:
        url=urlfield.get( )
        print(url)

        dBtn.config(text="pls wait.. ")
        dBtn.config(state=DISABLED)

        #filedialog.askdirectory
        path_to_save= askdirectory()
        print(path_to_save)
        if path_to_save is None:
            return
         #creating youtube object
        ob =YouTube(url)
        strms=ob.streams.all()
            #for i in strms:
            #    print(i)
        stream = ob.streams.first()
        stream.download(path_to_save)
        dBtn.config(text ="Done!")
        print("done! :)")
        dBtn.config(text="Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded Succesfully")
    except Exception as  e:
        print(e)
        print("error occured")

#GUI

ui= Tk()
ui.title("Youtube Downloader")
ui.iconbitmap('favicon.ico')
ui.geometry("500x400")

file=PhotoImage(file='ab.png')
headingIcon = Label(ui, image=file)
headingIcon.pack(side=TOP)

urlfield=Entry(ui,font=("Arial",14), justify=CENTER)
urlfield.pack(side=TOP, fill=X, padx=80)

#download
dBtn =Button(ui,text="Download",font=("Roboto",14), relief='ridge', command=startDownload)
dBtn.pack(side=TOP,pady=10)



ui.mainloop()
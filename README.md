# Converting PDF file to Image 

# Overview  
This is a GUI application to convert a PDF file into an image PNG file using Python.

![pdf2img](https://user-images.githubusercontent.com/87378628/135120383-b7200cf6-6113-4861-b92d-870120a93c15.png)

# Usage and set up
![package](https://user-images.githubusercontent.com/87378628/135120499-f13dedca-080a-443f-9520-d1633b441c96.png)

PDF2IMG GUI App needs the following Python packages to be installed: 
- pdf2image
- tkinter
- PIL 

You can install them using ```pip install -r requirements.txt.```

# How to use
After running the file main.py, a GUI window will appear. 
![display](https://user-images.githubusercontent.com/87378628/135120639-1e6260f3-c5cf-42d6-b39e-a7f42e97bfa5.png)


After pasting the directory of the PDF file into the entry box and click Convert, the application will automatically convert into an image and save it in the same folder with the program.
![success](https://user-images.githubusercontent.com/87378628/135741075-bd6c7ff7-e56e-4f21-8615-b1622c5b7782.png)


However, if no PDF file matching with your file location is found, there will be a message box to let you know that.
![nopdffound](https://user-images.githubusercontent.com/87378628/135120899-979452ca-bcfb-4cb7-a889-3f60a1a70070.png)
# pdf2img

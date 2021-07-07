import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):
    if filename.endswith(("png","jpg","jpeg","gif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.move(filename, "Images")

    if filename.endswith(("deb","exe","dmg")):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.move(filename, "Apps")
    
    if filename.endswith(("pdf")):
        if not os.path.exists("PDF"):
            os.mkdir("PDF")
        shutil.move(filename, "PDF")
    
    if filename.endswith(("doc","docx","xlsx","xls","pptx","ppt")):
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        shutil.move(filename, "Documents")

    if filename.endswith(("zip","tar","gz","rar")):
        if not os.path.exists("Archives"):
            os.mkdir("Archives")
        shutil.move(filename, "Archives")

print("Done Organizing This Folder")
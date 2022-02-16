import os


#Path of the folder you want to rename the insides of. Currently set to one folder, maybe being able to choose a folder coming later.
path = "E:/Backups/Documents/Valokuvausprojekti/Omat/Renamechamber"

def main():
    #What will be the name of the new file. It will be printed as "*prefix*_*number 1 to infinity*.*jpg or nef*"
    prefix = input("Give your desired prefix for the files: ").capitalize()
    jpgcount = 1
    nefcount = 1
    #Check if the file is a jpg or a nef file.
    for count, filename in enumerate(os.listdir(path)):
        if ".JPG" in filename or ".jpg" in filename:
            dst = f"{prefix}_{str(jpgcount)}.JPG"
            jpgcount += 1
        elif ".NEF" in filename or ".nef" in filename:
            dst = f"{prefix}_{str(nefcount)}.NEF"
            nefcount += 1
        else:
            #Failsafe
            print("something went wrong")
            os.system("pause")
            exit()

        #The actual renaming part. Src = the source path of the image and dst = the new path for the image, including the new name
        src = f"{path}/{filename}"
        dst = f"{path}/{dst}"
        os.rename(src, dst)
        
    #After the renaming display a message and prevents the window from closing on itself.
    print("All files renamed!")
    os.system("pause")
            
if __name__ == '__main__':
    main()
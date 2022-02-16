import os

path = "E:/Backups/Documents/Valokuvausprojekti/Omat/Renamechamber"

def main():
    prefix = input("Give your desired prefix for the files: ").capitalize()
    jpgcount = 1
    nefcount = 1
    for count, filename in enumerate(os.listdir(path)):
        if ".JPG" in filename or ".jpg" in filename:
            dst = f"{prefix}_{str(jpgcount)}.JPG"
            jpgcount += 1
        elif ".NEF" in filename or ".nef" in filename:
            dst = f"{prefix}_{str(nefcount)}.NEF"
            nefcount += 1
        else:
            print("something went wrong")
            exit()

        src = f"{path}/{filename}"
        dst = f"{path}/{dst}"
        os.rename(src, dst)
        
    print("All files renamed!")
    os.system("pause")
            
if __name__ == '__main__':
    main()
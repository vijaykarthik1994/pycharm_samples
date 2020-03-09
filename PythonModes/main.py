import  mods.XMLReader as reader
import sys as tes

if __name__ == "__main__":
    try:
        # print(tes.path)
        print(reader.__doc__)
        print(reader.__name__)
        reader = reader.MyReader("demo.txtx")
        reader.ReadFileData()
    except SystemError:
         print("System error")
    except:
        print("Unknown error")





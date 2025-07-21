import os

def SecureFileReader(fname, fpath):

    try:
        found = False
        for dir_path, dir_names, file_names in os.walk(fpath):
            if fname in file_names:
                found = True
                file_path = os.path.join(dir_path, fname)
                with open(file_path, "r") as file:
                    content = file.readlines()
                    for line in content:
                        print(line)
                break  # No need to continue searching once the file is found
            
              
        if not found:
            raise FileNotFoundError("File does not exist.")
        
    except FileNotFoundError:
        print("File not found")
    
    except PermissionError:
        print("Required permissions not met")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        
    else:
        print("File contents have been successfully printed.\n")

# Driver code
SecureFileReader("Paran.txt", r"C:\Users\paran\OneDrive\Desktop")
print()
SecureFileReader("RandomFileDoesNotExist.txt", r"Z:\Programming and Design Patterns")
print()
SecureFileReader("textfile.txt", r"Z:\Programming and Design Patterns")

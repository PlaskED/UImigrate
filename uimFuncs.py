import os

#WTF/account/realm/Char
def getPaths(acc="acc", realm="realm", char="char"):
    root = "./WTF"
    paths = {}
    paths["account"] = "{}/{}".format(root,acc)
    paths["realm"] = "{}/{}".format(paths["account"], realm)
    paths["char"] = "{}/{}".format(paths["realm"], char)
    return paths

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    """Open "path" for writing, creating any parent directories as needed."""
    mkdir_p(os.path.dirname(path))
    return open(path, 'w+')

def migrateAccount(old_path, new_path):
    var_path = old_path["account"]+'/SavedVariables/' 
    for file in os.listdir(var_path):
        if file.endswith(".lua"):
            write_buffer = ""
            with open(var_path+file, 'r+') as f:
                for line in f:
                    line = line.replace(old_path["realm"].split("/")[-1], new_path["realm"].split("/")[-1])
                    line = line.replace(old_path["char"].split("/")[-1], new_path["char"].split("/")[-1])
                    print(line)
                    write_buffer += line

            with safe_open_w(new_path["account"]+"/SavedVariables/"+file) as f2:
                f2.writelines(write_buffer)
            print(file)
    return

def migrateRealm(oldpath, newpath):
    return

def migrateChar(oldpath, newpath):
    return




#print(getDirs())

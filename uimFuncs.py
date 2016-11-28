import os

#WTF/account/realm/Char
def getDirs(acc="acc", realm="realm", char="char"):
    #root = os.path.relpath(".","..")+"/WTF/"
    root = "./WTF"
    dirs = {}
    dirs["account"] = "{}/{}".format(root,acc)
    dirs["realm"] = "{}/{}".format(dirs["account"], realm)
    dirs["char"] = "{}/{}".format(dirs["realm"], char)
    
    return dirs

def migrateAccount(oldpath, newpath):
    for file in os.listdir(oldpath+'/SavedVariables'):
        if file.endswith(".lua"):
            print(file)
    return

def migrateRealm(oldpath, newpath):
    return

def migrateChar(oldpath, newpath):
    return


#print(getDirs())

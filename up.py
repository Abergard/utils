import os, sys, getopt

build_dir = {'GLFW'      : 'c:\\src\\glfw\\build',
             'glbinding' : 'c:\\src\\glbinding\\build',
             'LLVM'     : 'c:\\src\\llvm\\build'}

clang_svn = {'llvm' : 'c:\\src\\llvm',
             'clang' : 'c:\\src\\llvm\\tools\\clang'}

svn_dir = {'LLVM' : clang_svn}

build_shared_lib = {'GLFW'      : 'ON',
                    'glbinding' : 'ON',
                    'LLVM'      : 'OFF'}

clean = "rm -rf "
cmake = "cmake -G \"Visual Studio 14 2015 Win64\" -DCMAKE_BUILD_TYPE=RELEASE -DBUILD_SHARED_LIBS:BOOL="

def main(argv):
    if(len(sys.argv) < 2 or
       (sys.argv[1] != "all" and not sys.argv[1] in build_dir)):
        print("Available lib to update: ")
        for key in build_dir:
            print('-' + key)
        exit()

    lib = sys.argv[1]
    if(lib == "all"):
       updateAllLibrary()
    else:
       updateLibrary(lib);
       
def checkMinimalArgvLen():
    return 

def updateAllLibrary():
    for lib in build_dir:
       compileLibrary(lib)

def updateLibrary(lib):
    if(isThirdArgument("svn")):
        updateSvnRepository(lib)
    else:
        compileLibrary(lib)

def compileLibrary(lib):
    if(isThirdArgument("r")):
        cleanBuildDirectory(lib)
        createBuildDirectory(lib)
    runCmake(lib)
    build(lib)
    
def isThirdArgument(arg):
    return (len(sys.argv) > 2 and sys.argv[2] == arg)

def updateSvnRepository(lib):
    reps = svn_dir[lib]
    for rep in reps:
        svnUpdate(reps[rep])

def svnUpdate(repository):
    command("cd " + repository + " & " + "svn up")

def cleanBuildDirectory(lib):
    command("rm -rf " + build_dir[lib])

def createBuildDirectory(lib):
    command("mkdir " + build_dir[lib])

def runCmake(lib):
    command("cd " + build_dir[lib] + " & " + cmake + build_shared_lib[lib] + " ..")

def build(lib):
    command("cd " + build_dir[lib] + " & " +
            "MSBuild14.exe " + lib + ".sln /p:Configuration=Release /v:m")

def command(command):
    print('> ' + command)
    os.system(command)

if __name__ == "__main__":
     main(sys.argv[1:])

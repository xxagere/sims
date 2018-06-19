#sh importantcode.sh

from settings import *
import os
import webbrowser
import platform


homefolder = os.path.dirname(os.path.abspath(__file__))
# 0 = worked
# 1 = error
link = ""
givenemail = ""

def cmd(x):
    try:
        result = os.system(x)
        if int(result) != 0:
            print x
            return int(result)
        else:
            return int(result)
    except ZeroDivisionError:
        print x
        print "Sorry ! Query doesn't seem to work!"
    

def checkSettings():
    if len(str(linktorepo)) > 0 and len(str(email)) > 0:
        global link
        global givenemail
        link = str(linktorepo)
        givenemail = str(email)
        print "Important settings set - great!"
    else:
        raw_input("Settings Not Set Correctly!")

def createShFile():
    f = open("importantcode.sh","w+")
    code = '''
git config --global user.email "''' + str(givenemail) + '''"
for Y in {2017..2018}
do
  mkdir $Y
  cd $Y
  for M in {01..12}
  do
    mkdir $M
    cd $M
    for D in {01..31}
    do
      mkdir $D
      cd $D
      for i in {01..12}
      do
        echo "$i on $M/$D/$Y" > commit.md
        export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
        export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
        git add commit.md -f
        git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
        git push origin master
      done
      cd ../
    done
    cd ../
  done
  cd ../
done
git push origin master
git rm -rf 20**
git rm -rf 19**
git commit -am "cleanup"
git push origin master
'''
    f.write(code)
    f.close


def CheckWGET():
    if cmd("wget") > 0:
        plat = platform.system()
        plat = plat.lower()
        if plat == "windows": #Should work for most Windows Users.
            webbrowser.open("https://eternallybored.org/misc/wget/1.19.4/32/wget.exe")
            print "Please complete the following install. Then restart this program."
            raw_input()
            quit()
        if plat == "linux": #For Debian users only.
            if cmd('sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"') != 0:
                print "Please install 'wget' manully, then restart this program."
                raw_input()
                quit()
        if plat == "mac": # Should work for most Macs.
            if cmd('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)') != 0:
                print "Please manually install 'wget' manually for your Mac, then restart this program."
                raw_input()
                quit()
            if cmd("brew install wget") != 0:
                print "Please manually install 'wget' manually for your Mac, then restart this program."
                raw_input()
                quit()
        else:
            print "Not really needed"
    else:
        print "WGET is installed - great!"

def CheckGIT():
    if cmd("git --version") > 0:
        plat = platform.system()
        plat = plat.lower()
        if plat == "windows":
            webbrowser.open("https://git-scm.com/download/win")
            print "Please complete the following install. Then restart this program."
            raw_input()
            quit()
        if plat == "linux": #For Debian users only.
            if cmd('apt-get install git"') != 0:
                print "Please install 'git' manully for your linux version, then restart this program."
                raw_input()
                quit()
        if plat == "mac":
            if cmd("brew install git") != 0:
                print "Please manually install Git for your Mac, then restart this program."
                raw_input()
                quit()
    else:
        print "Git is installed - great!"


def itWorked():
    print "You did it!"
    raw_input()
    
def setUpHack():
    global homefolder
    global link
    plat = platform.system()
    plat = plat.lower()
    if plat == "windows":
        test = "git push"
        command = "cd " + str(homefolder) + " && git init && " + "git remote add origin " + str(link) + ' && echo "I am a very nice readme file." > README.md && git add --all && ' + 'git commit -m "init"'
        cmd(test)
        cmd(command)
        #create special batch file:
        code = '"C:\Program Files\Git\git-bash.exe" "' + str(homefolder) + '\importantcode.sh"'
        f = open("starthack.bat", "w+")
        f.write(code)
        f.close()
        os.startfile("starthack.bat")
        #cmd('"C:\Program Files\Git\git-bash.exe" ' + '"' + str + homefolder + '\\importantcode.sh"')
        itWorked()
            
    if plat == "linux": #For Debian users only.
        cmd("cd ~/Desktop")
        cmd("cd verynicefolder && git init")
        cmd("git remote add origin " + str(link))
        cmd('echo "I am a very nice readme file." > README.md && git add --all')
        cmd('git commit -m "init" && git push -u origin master')
        createShFile()
        filelocation = homefolder.replace("\\", "/")
        cmd("sh " + str(filelocation) + "/importantcode.sh")

        itWorked()

    if plat == "mac":
        cmd("cd ~/Desktop")
        cmd("cd verynicefolder && git init")
        cmd("git remote add origin " + str(link))
        cmd('echo "I am a very nice readme file." > README.md && git add --all')
        cmd('git commit -m "init" && git push -u origin master')
        createShFile()
        filelocation = homefolder.replace("\\", "/")
        cmd("sh " + str(filelocation) + "/importantcode.sh")

        itWorked()

def start():
    createShFile()
    checkSettings()
    raw_input("Press the enter key to continue:")
    CheckGIT()
    raw_input("Press the enter key to continue:")
    setUpHack()

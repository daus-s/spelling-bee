#!/bin/bash

# HOMEBREW, PYTHON, FLASK REQUIRED
#installed flag
installed_flag=false
if !($installed_flag);
    then
        # check if homebrew exists
        if ! command -v brew &> /dev/null
            then
                #if not install
                echo "Homebrew not found. Installing..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            else
                brew_version=$(brew --version | awk 'NR==1{print $2}')
                echo "Homebrew requirement satisfied: ${brew_version}"
        fi        
        #install python after checking
        if ! command -v python3 &> /dev/null
            then
                echo "Python not found. Installing..."
                brew install python3
            else 
                python_version=$(python3 --version | awk 'NR==1{print $2}')
                echo "Python requirement satisfied: ${python_version}"
        fi
        #install flask
        pip install -U flask

        dir=$(pwd)
        #before moving the package contents
        sed -i '' "s|{PATH_TO_DIRECTORY}|${dir}|g" Spelling\ Bee.app/Contents/document.wflow
        cp -a ./Spelling\ Bee.app /Applications/

        #flip installed flag to true
        sed  -i '' "5s#false#true#" ./installer.sh
    else
        echo "Already installed. Exiting..."
        sleep 2
fi

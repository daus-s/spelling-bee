#WELCOME
#!/bin/bash
echo "*******************************************" >> ~/Documents/TwitchProjects/spelling-bee/logs/log
if pgrep -f "Spelling\ Bee" > /dev/null; then
    echo "Existing instance found. Terminating..." >> ~/Documents/TwitchProjects/spelling-bee/logs/log
    pkill -f "Spelling\ Bee"
fi


if lsof -Pi :4174 -sTCP:LISTEN -t >/dev/null ; then
    echo "Something is already running on port 4174. Killing it..." >> ~/Documents/TwitchProjects/spelling-bee/logs/log
    lsof -t -i :4174 | xargs kill
fi

/usr/bin/python3 ~/Documents/TwitchProjects/spelling-bee/app.py &
FLASK_PID=$! 
sleep 5
open -na "Google Chrome" --args --new-window "http://localhost:4174" --incognito
sleep 3600
kill $FLASK_PID
#GOODBYE

#WELCOME
#!/bin/bash
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
    echo "Something is already running on port 5000. Killing it..."
    lsof -t -i :5000 | xargs kill
fi
export FLASK_APP=app.py
flask run & 
FLASK_PID=$!
open -na "Google Chrome" --args --new-window "http://127.0.0.1:5000" --incognito
sleep 3600
kill $FLASK_PID
#GOODBYE

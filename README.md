# spelling-bee
Happy birthday Anna! Don't use this unless you're really stuck :)

## Abstract
This repository contains the code used to solve the 'Spelling Bee' game from [NYT games](https://www.nytimes.com/games/). It is built using a simple filter function on two lists of words, valid English words and a list provided by Apple on MacOS. The valid English list is referred to as `dict` and was generated by pinging [dictionaryapi.dev](https://dictionaryapi.dev/). An installer, app package, and all system requirements are provided.

## Game Logic
Psuedo-code:
```
input -> word, required, allowed
while not invalid
  if word length < 4
    invalid
  if not word contains required
    invalid
  letters = word as list
  for char l: letters
    if l not in allowed + [required]
      invalid
  valid
```
The logic goes as follows:
- Check the length requirement, if it is less than 4, return 
The filter runs on any word with the constraints. If the constraints are met it will add the word to the list. Otherwise, nothing is returned to be added. The checks are executed in the order of least computation. That is the length check, the simplest filter, is performed first to avoid unnecessarily performing long filtering processes. Second, the rf flag is checked (required flag), if the required letter is not contained then there is no point in performing the allowed check. Finally, once in the loop check if each word contains any letters not in the allowed letter list. As soon as a disallowed letter is detected exit. This does not have a large impact on each word but when running the filter ~$2\cdot10^{5}$ times the impact becomes more noticeable. 
## Instructions
- Download [`spelling-bee.zip`](https://github.com/daus-s/spelling-bee/raw/main/spelling-bee.zip)
  - This contains the directory with the source (src), resources, and templates, and executable files necessary to run this program.
    ```
    spelling-bee
     | package
        | templates
           | index.html
        | static
           | styles.css
           | arrow.png
        | src
           | app.py
           | wordmatics.py
        | resources
           | dict #all valid English words
           | words #all words according to /usr/share/dict/words (cp /usr/share/dict/words .)
        | Spelling\ Bee.app #contains all files for App 
        installer.sh
    ```
- Extract zip file via CLI or in Finder
  - ##### Finder
    - Extract the zip file using the default zip utility built into MacOS. 
    <img width="584" alt="Screenshot 2023-10-27 at 12 46 45 AM" src="https://github.com/daus-s/spelling-bee/assets/48344654/d763e25d-2c24-4d26-a4c3-56f99275e496">

      **Figure 1.** View of extracting the zip file using the default MacOS extracting tool. The size of the extracted folder is about 6.3MB
    
    <img width="577" alt="Screenshot 2023-10-27 at 12 45 10 AM" src="https://github.com/daus-s/spelling-bee/assets/48344654/c0c11fdd-e0d3-4be6-beed-d11ec7ce3bcd">

  
    **Figure 2.** The extracted package contents
  - ##### Terminal/CLI
    - Run the command
      - `$ unzip -q package.zip` **-q** is used to silence the extraction.
      - Ensure you are in the correct directory where the package file is. To move this directory somewhere else run `mv ~/Downloads/spelling-bee.zip <desired_directory_location>`. **Note:** this is now unnecessary as the installer uses the same pattern in installing and is not user-dependent.

- Run the installer script
  - Navigate into the package directory.
    - `user$ cd ~/Downloads/spelling-bee/package/`
    - `user$ ls`
   
      <img width="492" alt="Screenshot 2023-10-27 at 12 50 20 AM" src="https://github.com/daus-s/spelling-bee/assets/48344654/6c9a8acc-0891-46bc-b2af-e19511d79fb8">
      
      **Figure 3.** Output of the previous commands.
  - Run the installer script via `./installer.sh`
    - If this error: `-bash: ./installer.sh: Permission denied`, is generated run: `chmod +x installer.sh`
    - This file has been chmod'ed already

- This has put the `Spelling Bee.app` in the Applications folder and will be runnable via the shortcut in the Launchpad. The program files will be located in the folder `~/` on MacOS, which is `/Users/<yourname>/`. 
## Technologies Used
This project was mainly built using Python, HTML, and CSS. The framework used to build the app itself is Flask. The app is run via an Apple Auttomator app. Each component of this project had intentionality in the technology used. While seemingly meaningless, the reason Flask is used is that early versions of the App would ping [dictionaryapi.dev](dictionaryapi.dev). Flask has very strong compatibility with API calls. This is likely to be changed in future updates to help with the ease of use. Frameworks like TKinter will likely replace the browser-based application as there is no more reliance on any API calls. The HTML and CSS are basic web tools, there are no external libraries employed outside of the Google fonts used for the website.
## Issues dealt with
### Control Port 5000
In early development, the app would not be returned on the port although there were no issues from the Flask server's side. This turned out to be because of a choice of both Apple and the Flask developers to assign port 5000.

'Port 5000 is now used for Airplay as well as port 7000 as of macOS Monterey. So yes, it's normal ! Apple decided to use those ports even though a lot of developers use those ports by default.' -[tama](https://apple.stackexchange.com/users/396787/tama)
```
$ export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
$ flask run
 * Running on http://127.0.0.1:5000/
```
-[Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/config/)

This issue was not immediately apparent. Sometimes, the server would load the Flask app other times it would return an access denied 403 response code. It was not until finding that ports 5000 and 7000 are used by MacOS was the  app able to be  run consistently.
#### Solution
A random numbered port was chosen that was not assigned according to the entirely comprehensive list on Wikipedia /s.

Port No.
4174

### Checking Words against a 'more correct' list
There are many words in the list that Apple has on disk that match the requirements of NYT Games Spelling Bee but are not considered to be words in their word list. The first iterations were using longer and longer prompts on ChatGPT, however, this proved inefficient and not rigorous. As Alexander Kurz says "If you need to be right 100% of the time you must use math; 1% wrong in one million is still a lot." The next solution was to not remove any assuming NYT Games list was a subset of `/usr/shared/dict/words/` (which b.t.w. exists on all Macs if you ever need a set of all words)

<img width="487" alt="Screenshot 2023-10-27 at 1 31 24 AM" src="https://github.com/daus-s/spelling-bee/assets/48344654/6040eaf4-347f-4f3d-ad37-54df609df846">

**Figure 4.** $A \subseteq B$, where `/usr/shared/dict/words` is *A*, and B is the set that NYT Games uses. 
The next solution was to create a more rigorous and comprehensive dictionary. This was done using a script that pinged the [dictionaryapi.dev](https://dictionaryapi.dev/) for each word in the Apple dictionary. If the response code was 200 the word was added. However, the final version of the app includes both the list corrected by the dictionaryAPI script and the list of words from Apple to guarantee that there are no words missing. Look to the future developments section to see how this can be improved. 
### Pinging DictionaryAPI
As stated before a script was used to validate or invalidate each word in the Apple set. The script took approximately 3 days as the API has a request limit for every 300 seconds. The limiter is set to 450 requests per 300,000 milliseconds. 
```
limiter = rateLimit({
        windowMs: 5 * 60 * 1000, // 5 minutes
        max: 450 // limit each IP to 450 requests per windowMs
    }),
```
The script would often freeze and stop querying which is not the desired behavior for a script that needs to run continuously. The solution was to check if the response code was 429 and then wait the limiter time. It would then resume execution after that. 
Issues arose with the previous version because the first word that hit 429 would not be validated. This meant that the only fully working versions would use the response code check and sleep logic.
### Computation time and C++ vs. Python
Naturally with large lists runtime can be an issue. The initial version of this project was a C++ program that would use the filter logic against the original list. The output would be sent to `stdout`. This was used by early versions of the Flask app by reading in the output from the C++ program being executed. This, however, would break once the Automator App was created. The C+ file would not execute with error code 127. 

The first attempts a resoilving this proving fruitless led to a move to python. The working version uses Python to execute the filter logic on the same lists. While it does lose some speed for the single call it is hardly noticeable. This was added into wordmatics.py as a new function. 
## Future Developments
Some developments in the future include moving away from the browser-based Flask, narrowing the English dictionary down more, generating said dictionary from the API, and improving runtime by migrating to C++ for the logic. 

Moving away from Flask likely would use TKinter or some other Python-based GUI. This would allow the program to execute and close exactly with the window and not leave any ports open or in use. 

Improvements to the list of words are necessary. There are still frequently words that NYT Games does not consider valid. This could be done by checking both the language tag on the response as well as checking the type of word (e.g. verb, adverb, noun, proper noun, etc.). Additionally if [dictionaryapi.dev](dictionaryapi.dev) has a list or some way to find many words by queries a list could be created from that.

While it has little impact in this application, large volume filtering of strings in Python will become much slower as input increases. This is a clear reason why using something like C++ to perform the logic would be beneficial. This logic for filtering is specific but the idea of filtering strings is not. Using a more efficient language can reduce runtime and drastically improve efficiency. 

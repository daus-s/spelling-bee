# spelling-bee
Happy birthday! Don't use this unless you're really stuck :)

## Abstract

## Instructions
- Download [`package.zip`](https://github.com/daus-s/spelling-bee/raw/main/package.zip)
  - This contains the directory with source, resources, and templates and executable files necesary to run this program.
    ```
    package
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
    <img width="584" alt="Screenshot 2023-10-24 at 2 33 20 PM" src="https://github.com/daus-s/spelling-bee/assets/48344654/648081c2-f822-47a7-aacc-363db565d8a9">
    
      **Figure 1.** View of extracting the zip file using the default MacOS extracting tool. The size of the extracted folder is about 6.3MB
    
    <img width="577" alt="Screenshot 2023-10-24 at 2 46 38 PM" src="https://github.com/daus-s/spelling-bee/assets/48344654/8f68de16-6e80-4714-9f26-70275828fcc1">
  
    **Figure 2.** The extracted package contents
  - ##### Terminal/CLI
    - Run the command `$ unzip package.zip`
      - Ensure you are in the correct directory where the package file is. To move this directory somewhere else run `mv ~/Downloads/package.zip <desired_directory_location>`.

- Run the installer script
  - Navigate into the package directory.
    - `user$ cd ~/Downloads/package`
    - `user$ ls`
      <img width="606" alt="Screenshot 2023-10-24 at 3 03 53 PM" src="https://github.com/daus-s/spelling-bee/assets/48344654/b627c811-90f2-4d58-9d4c-5ecf19f1cec4">
      **Figure 3.** Output of the previous commands.
  - Run the installer script via `./installer.sh`
    - If this error: `-bash: ./installer.sh: Permission denied`, is generated run: `chmod +x installer.sh`
    - This file has been chmod'ed already

- This has put the `Spelling Bee.app` in the Applications folder and will be runnable via the shortcut in the Launchpad.
## Technologies Used
## Issues dealt with
## Future Developments

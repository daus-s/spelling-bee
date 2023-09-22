#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <array>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

const char* FILENAME = "/usr/share/dict/words";
int MODE = 0; //if active then it is python use 

char* spacer(string s)
{
    int l = 16;
    if (s.length() > 16)
    {
        cout << "bad formatting issue..." << endl;
    }
    char* b = new char[l-s.length()];

    for (int i = 0; i < l-s.length(); ++i)
    {
        b[i] = ' ';
    }
    return b;
    
}

bool filter(string word, char* allowed, char req)
{
    //printf("\nfilter: %s", word.c_str());
    const char* w = word.data();
    int len = word.length();

    if (len < 4)
        return false;

    bool rf = false;
    for (int i = 0; i < len; ++i)
    {
        if (w[i] == req)
        {
            //cout << " CR ";
            rf = true;
        }
        if (tolower(w[i]) != tolower(allowed[0]) &&
            tolower(w[i]) != tolower(allowed[1]) &&
            tolower(w[i]) != tolower(allowed[2]) &&
            tolower(w[i]) != tolower(allowed[3]) &&
            tolower(w[i]) != tolower(allowed[4]) &&
            tolower(w[i]) != tolower(allowed[5]) &&
            tolower(w[i]) != tolower(req))
            {
                //cout << "HI";
                return false;
            }
    }
    return rf;
}


char** get_args(string str)
{
 
    vector<string> tokens;

    // Returns first token
    char* c_str = strdup(str.c_str());
    const char* delimiter = " ";
    char* token = strtok(c_str, delimiter);

    // Keep printing tokens while one of the
    // delimiters present in str[].
    while (token != NULL)
    {
        tokens.push_back(token);
        token = strtok(NULL, delimiter);
    }
 
    // Free the allocated memory for c_str
    free(c_str);

    // Allocate memory for an array of char pointers
    char** args = new char*[tokens.size() + 1];

    // Copy each token to the char array
    for(size_t i = 0; i < tokens.size(); ++i)
    {
        args[i] = new char[tokens[i].length() + 1];
        strcpy(args[i], tokens[i].c_str());
    }

    // Set the last element of the array to NULL (for termination)
    args[tokens.size()] = NULL;

    return args;
}

string GetStdoutFromCommand(string cmd) {

  string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");

  stream = popen(cmd.c_str(), "r");
  if (stream) {
    while (!feof(stream))
      if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
    pclose(stream);
  }
  return data;
}

int main(int argc, char ** argv)
{
    if (argc != 4 && argc !=3)
    {
        return 2;
    }
    if (argc == 4)
        MODE = atoi(argv[3]);

    if (!MODE)
        printf("%s, %s\n", argv[1], argv[2]);

    //read words from
    //usr/share/dict/words
    string wc_cmd = "wc -l /usr/share/dict/words";
    char** cmd_tkns = get_args(GetStdoutFromCommand(wc_cmd));
    int sz = atoi(cmd_tkns[0]);
    //read /usr/share/dict/words
    string* words = new string[sz];

    ifstream file(FILENAME);

    if (file.is_open())
    {
        for (int i = 0; i < sz && getline(file, words[i]); ++i)
        {
            // Do nothing; just reading lines from the file
        }
        file.close();
    }
    else
    {
        std::cerr << "Unable to open file: " << FILENAME << std::endl;
    }

    vector<string> v;

    for (int i = 0; i < sz; ++i)
    {
        bool f = filter(words[i], argv[1], argv[2][0]);
        if (f)
        {
            v.push_back(words[i]);
        }
        //printf(" %s", f ? "true" : "false");

    }
    float x = (float)v.size();
    int u = floor(sqrt(x));
    int l = ceil(sqrt(x));

    int row = l;
    if ((x - l) > (u - x))
    {
        //closer to upperbound
        row = u;
    }

    
    for (int i = 0; i < v.size(); ++i)
    {
        if (MODE){
            std::cout << v[i] << ((i == v.size()-1) ? "\n" : ", ");
        }
        else {
            std::cout << v[i] << ((i + 1) % row ? spacer(v[i]) : "\n");
        }
    }
    cout << endl;
    return 0;
}
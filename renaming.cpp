#include <cstdlib>
#include <dirent.h>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;
int main()
{
std::string directory;

std::cout << "Enter directory: ";
std::cin >> directory;
DIR *pdir = NULL;
struct dirent *pent = NULL;
const char * DIRECTORY;

// convert directory string to const char
DIRECTORY = directory.c_str();

pdir = opendir (DIRECTORY);

int i = -2;
std::string s, oldname, newname;
const char * OLDNAME, * NEWNAME;

while (pent = readdir (pdir))
{
    // convert int i to str s
    std::stringstream out;
    out << setfill('0')<< setw(5) << i;
    s = out.str();

    oldname = (std::string(DIRECTORY)+pent->d_name).c_str();
    newname = (std::string(DIRECTORY)+"f"+s+".png").c_str();

    OLDNAME = oldname.c_str();
    NEWNAME = newname.c_str();

    rename(OLDNAME, NEWNAME);

    i++;
} 
}

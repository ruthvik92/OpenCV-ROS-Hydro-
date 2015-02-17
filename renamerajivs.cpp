#include <cstdlib>
#include <dirent.h>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int listdir(const char *path, vector<string>& list) {
  struct dirent *entry;
  DIR *dp;
 
  dp = opendir(path);
  if (dp == NULL) {
    perror("opendir");
    return -1;
  }
 
  while((entry = readdir(dp)))
     list.push_back(entry->d_name);
 
  closedir(dp);
  return 0;
}
 
int main(int argc, char **argv) {

  int counter = 1;
  
  vector<string> fileList;
  	 
  if (argc == 1)
	listdir(".",fileList); /// fill the fileList vector with lisdir//files in current directory.
 
  while (++counter <= argc) {
    printf("\nListing %s...\n", argv[counter-1]);
    listdir(argv[counter-1],fileList);
  }
 
   vector<string>::iterator v = fileList.begin();
   while( v != fileList.end()) {
      cout << "value of v = " << *v << endl;
      v++;
	
  // refer this link http://www.cplusplus.com/reference/cstdio/rename/
  // fileList will have list of all the files in the directory 
 // now u have to parse every filename and rename it according to the pattern u want 
   }
  return 0;
}


























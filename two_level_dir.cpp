#include <iostream>
#include <string>

using namespace std;

string root, dirNames[10], sdirNames[100], fNames[1000];
int flag = 0, sdCount[10] = {0}, fCount[100] = {0};

int searchDir(string tempDir){
    for (int i = 0; i < flag; i++){
        if (dirNames[i] == tempDir)
            return i;
    }
    return -1;
}

int searchSDir(string tempSDir, int x, int i){
    for (int j = x; j < i; j++){
        if (sdirNames[j] == tempSDir)
            return j;
    }
    return -1;
}

int searchFile(string tempFile, int s, int f){
    for (int i = s; i < f; i++){
        if (fNames[i] == tempFile)
            return i;
    }
    return -1;
}

void addDir(){
    string tempDir;
    cout << "Enter the name of the directory to be created: ";
    cin >> tempDir;
    int x = searchDir(tempDir);
    if (x != -1)
        cout << "\nDirectory already exists!\n";
    else
        dirNames[flag++] = tempDir;
}

void addSDir(){
    int cv = 1;
    string temp;
    if (flag == 0){
        cout << "\nPlease create a directory first!\n";
        return;
    }
    cout << "Enter the name of the directory inside which the sub-directory is to be created: ";
    cin >> temp;
    int x = searchDir(temp);
    int i = x;
    if (x == -1){
        cout << "\nDirectory does not exist!" << endl;
        return;
    }
    i = i * 10;
    i = i + sdCount[x];
    while (cv){
        string tempSDir;
        cout << "Enter the name of the sub-directory to be created inside '" << temp << "': ";
        cin >> tempSDir;
        int y = searchSDir(tempSDir, x, i);
        if (y != -1)
            cout << "\nSub-Directory already exists!\n";
        else{
            sdirNames[i] = tempSDir;
            sdCount[x]++;
        }
        int tempch;
        cout << "\nPress 1 to create more sub-directories, Press 0 for Main Menu: ";
        cin >> tempch;
        cv = tempch;
        i++;
    }
}

void addFile(){
    int cv = 1;
    string tempDir;
    if (flag == 0){
        cout << "\nPlease create a directory first!\n";
        return;
    }
    cout << "Enter the name of the directory: ";
    cin >> tempDir;
    int x = searchDir(tempDir);
    if (x == -1){
        cout << "\nDirectory does not exist\n";
        return;
    }
    int i = x;
    string tempSDir;
    i = i * 10;
    i = i + sdCount[x];
    cout << "Enter the name of the sub-directory inside '" << tempDir << "': ";
    cin >> tempSDir;
    int y = searchSDir(tempSDir, x, i);
    if (y == -1){
        cout << "\nSub-Directory does not exist\n";
        return;
    }
    int t = y * 10;
    int pos = t + fCount[t];
    while (cv) {
        string tempFile;
        cout << "Enter the name of the file to be created inside '" << tempSDir << "': ";
        cin >> tempFile;
        int z = searchFile(tempFile, t, pos);
        if (z != -1)
            cout << "\nFile already exists\n";
        else {
            fNames[pos] = tempFile;
            fCount[y]++;
        }
        int tempch;
        cout << "\nPress 1 to create more files, Press 0 for Main Menu: ";
        cin >> tempch;
        cv = tempch;
        pos++;
    }
}
void displayDirTree(){
    cout << "\n*****************************************************************************\n";
    cout << "\t||USERNAME: " << root << "||\t\n";
    cout << "*****************************************************************************\n";
    cout << "\tDIRECTORY\tSIZE\tSUB-DIRECTORIES\t\tSIZE\tFILES\n";
    cout << "*****************************************************************************\n";
    for (int i = 0; i < flag; i++){
        cout << "\n\t" << dirNames[i] << "\t\t" << sdCount[i] << "\t";
        if (sdCount[i] == 0)
            cout << "NONE\n";
        else {
            for (int j = i*10; j < sdCount[i]+(i*10); j++){
                cout << sdirNames[j] << "\t\t\t" << fCount[j] << "\t";
                if (fCount[j] == 0)
                    cout << "NONE\n\t\t\t\t";
                else{
                    for (int k = j*10; k < fCount[j]+(j*10); k++){
                        cout << fNames[k] << "\n\t\t\t\t\t\t\t\t";
                    }
                    cout << "\n\t\t\t\t";
                }
            }
        }
    }
    cout << "\n*****************************************************************************\n";
}

int main(){
    cout << "Enter the User Name: ";
    getline(cin, root);
    int ch, x = 1;
    while (x){
        cout << "\nPress 1 to create a directory inside root\n";
        cout << "Press 2 to create a sub-directory inside a directory\n";
        cout << "Press 3 to create a file inside a sub-directory\n";
        cout << "Press 4 to display the directory tree\n";
        cout << "Press 0 to exit\n";
        cin >> ch;
        switch(ch){
            case 0: x = 0;
                    break;
            case 1: addDir();
                    break;
            case 2: addSDir();
                    break;
            case 3: addFile();
                    break;
            case 4: displayDirTree();
        }
    }
    for (int i = 0; i < 5; i++){
        cout << i+1 << ". " << fNames[i] << endl;
    }
    return 0;
}
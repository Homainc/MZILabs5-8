#include <string>
#include <iostream>
#include "HMAC_SHA1.h"

using namespace std;

int main(){
    string key, msg;
    cout << "Enter key: ";
    getline(cin, key);
    cout << "Enter message: ";
    getline(cin, msg);
    BYTE* bkey = (BYTE*)key.c_str();
    BYTE* bmsg = (BYTE*)msg.c_str();
    CHMAC_SHA1 hmac;
    BYTE* result;
    hmac.HMAC_SHA1(bmsg, msg.length, bkey, key.length, result);
    printf("%s", (char*)result);
}
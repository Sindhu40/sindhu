void vowelOrConsonant(char x) 
{ 
    if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') 
        cout << "Vowel" << endl; 
    else
        cout << "Consonant" << endl 
} 
int main() 
{ 
    vowelOrConsonant('c'); 
    vowelOrConsonant('e'); 
    return 0; 
} 

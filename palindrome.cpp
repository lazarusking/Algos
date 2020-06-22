#include <iostream>
#include <string>
#include <sstream>
using namespace std;
typedef long long int llt;
class palindrome
{
public:
    llt numIs;
    llt reverse{0};

    void palindromeCheck(llt value)
    {
        numIs = value;
        while (value != 0)
        {
            reverse = reverse * 10 + value % 10;
            value = value / 10;
        }
        if (numIs == reverse)
            cout << numIs << " is already a numeric palindrome.";
        else
        {
            palindromePrint();
        }
    }
    void palindromePrint()
    {
        std::stringstream ss;
        llt M = reverse;
        llt append;
        ss << numIs << M;        
        ss>>append;
        cout << M << " should be appended to make "
             << numIs << " a palindrome: " << append;
    }
};
int main()
{
    llt num = {0};
    cout << "Enter an integer to check whether it's a Palindromic numeral: ";
    cin >> num;
    palindrome pal;
    pal.palindromeCheck(num);
    return 0;
}

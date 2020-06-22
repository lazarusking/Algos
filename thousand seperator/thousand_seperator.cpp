#include <iostream>
#include <string>
using namespace std;
typedef long long int llt;

void thousand_sep(llt num){
    std::string num_str=std::to_string(num);
    int pos=num_str.length()-3;
    while (pos>0){
        num_str.insert(pos,",");
        pos-=3;
    }
    cout<<num_str;
};
int main(){
    llt num;
    //Just input the value at the start since only one cout is needed in the question
    cin>>num;
    thousand_sep(num);
    return 0;
}

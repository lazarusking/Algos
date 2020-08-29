#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
class primes
{
public:
    vector<int> primenums;

    void list(int n)
    {
        int num = 2;
     primenums.resize(n - 1);
        for (int i = 0; i < primenums.size(); i++)
      {
            primenums[i] = i + 2;
        }
        int it{2};
        int val{0};
        while ((primenums[val] * primenums[val]) < n)//less than square of
        {
            //cout<<primenums[val]<<"now "<<"\n";
            for (int i = 0; i<n/primenums[val]; i++)
            {
                std::vector<int>::iterator position = std::find(primenums.begin(), primenums.end(), primenums[val] * it);
                //removes all multiples of num(from 2)
                //cout << primenums[val] * it << ' ';
                if (position != primenums.end())
                { // == primenums.end() means the element was not found
                    primenums.erase(position);
                }
                it++;
            }
            it = {2};//reinitialize 'it' since it carries over the value used in the loop
            num++;
            val++;
        }
       
        for (auto i = primenums.begin(); i != primenums.end(); i++)
        {
            std::cout << *i << ' ';
        }
    }
};
int main()
{
    primes out;
    int to_prime;
    cout<<"Input an integer between 2 and 10000 to find all primes in that range: ";
    cin>>to_prime;
    out.list(to_prime);
    return 0;
}

#include <iostream>

int main()
{
	using namespace std;
	int i{};
	int numSun{0};  
	int days{ 2 };
	/*
	Using 1-Monday
	2-Tuesday
	3-Wednesday
	4-Thursday
	5-Friday
	6-Saturday
	7-Sunday
	How many Sundays fell on the first month dduring twientieth century (1 Jan 1901 to 31 Dec 2000)
	After every leap year, the day it falls on Jan increases by one
	*/
	


	for (i = 1901; i < 2001; i++) {
		//cout << i << '\n';
		//cout << days << " count" << '\n';
		days++; //incrementing for the next year
		days = days % 7;

		//to increment when a leap year occurs
		if (i % 4 == 0) {
			//cout << "leap year :\n";
			days++;
		}

		/*increment numSun whenever days is 7(Sunday),
		because of the modulo calculation some of the days are 0
		which represent (7%7==0) still sunday
		*/
		if (days == 7|| days==0) {
			numSun++;
		}
		
	}

	cout << "###########################################################" << '\n';
	cout << "#                                                         #\n";
	cout << "# We have " << numSun << " Sundays from 1901 to 2000 falling on 1st Jan #" << '\n';
	cout << "#                                                         #\n";
	cout << "###########################################################";

	return 0;
}

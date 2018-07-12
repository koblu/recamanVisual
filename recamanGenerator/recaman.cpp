#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
using namespace std;

int main(){
	vector<int> numbers;
	set<int> numCheck;
	int currentJump, currentPlace = 0, highestJump;
	printf("What should the highest jump be?\n");
	cin >> highestJump;
	for(currentJump = 1; currentJump < highestJump; currentJump++){
		printf("%i ",currentPlace); 
		if(currentPlace - currentJump > 0 && numCheck.find(currentPlace- currentJump) == numCheck.end()){
			currentPlace = currentPlace - currentJump;
			numCheck.insert(currentPlace);
		}else{
			currentPlace = currentPlace + currentJump;
			numCheck.insert(currentPlace);
		}
	}	
	printf("\n");
	return 0;
}

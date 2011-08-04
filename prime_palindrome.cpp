/**
  * Prime Palindrome
  * Written by Eric Bakan
  */

#include <math.h>
#include <stdio.h>

//tests whether a given number is palindromic
bool isPalindrome(int num);

int main(int argc, char**argv) {

    //use a seive of eratosthenes
    //initialize the seive
    const int seiveSize=1000;
    bool seive[seiveSize];
    seive[0]=false;
    seive[1]=false;
    for(int i=1;i<seiveSize;i++) {
	seive[i]=true;
    }

    //sort the seive
    for(int i=2;i<seiveSize;i++) {
	for(int j=i*2;j<seiveSize;j+=i) {
	    seive[j]=false;
	}
    }

    //find the solution
    for(int i=seiveSize-1;i>=2;i--) {
	if(seive[i] && isPalindrome(i)) {
	    printf("%d\n",i);
	    break;
	}
    }
    return 0;
}

bool isPalindrome(int num) {
    int numcp=num;
    int len=0;
    while(numcp!=numcp/10) {
	numcp/=10;
	len++;
    }
    for(int i=0;i<len/2;i++) {
	int msd=num/((int)pow(10,len-(i+1)));
	int lsd=(num/((int)pow(10,i)))%10;
	if(msd!=lsd) {
	    return false;
	}
    }
    return true;
}

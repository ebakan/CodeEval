/**
  * Sum of Primes
  * Written by Eric Bakan
  */

#include <math.h>
#include <stdio.h>

//tests whether a given number is prime or not
//worst-case performance of O(n^.5)
bool isPrime(int num);

int main(int argc, char**argv) {
    int sum=0,count=0,i=2;

    //runs unti 1000 primes are found
    while(count<1000) {
	if(isPrime(i)) {
	    sum+=i;
	    count++;
	}
	i++;
    }

    printf("%d\n",sum);
    return 0;
}

bool isPrime(int num) {
    //easy O(1) base cases
    if(num<2)
	return false;
    if(num==2)
	return true;
    if(num%2==0)
	return false;

    //O(n^.5) worst-case
    int maxtest=ceil(sqrt(num));
    for(int i=2;i<=maxtest;i++) {
	if(num%i==0) {
	    return false;
	}
    }
    return true;
}

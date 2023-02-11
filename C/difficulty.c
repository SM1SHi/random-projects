#include <stdio.h>
#define COIN 100000000L

int provera(){
	long height = 775310;
        long int nSubsidy = 50 * COIN;
        nSubsidy >>= (height / 210000);
        return nSubsidy;
}

int main(){
        long long int b = provera();
        printf("%lld \n", b);
        return 0;
}


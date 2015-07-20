#include <stdio.h>

static inline int getNum()
{
    int c = getchar_unlocked() - '0';
    int res = 0;
    while(c < 0 || c > 9)
         c = getchar_unlocked() - '0';    
    
    res = c;
    c = getchar_unlocked() - '0';
    while(c >= 0 && c < 10){
        res = res * 10 + c;
        c = getchar_unlocked() - '0';
    }
            
    return res;
}

int main(void)
{
	int t = getNum();
	for (int i = 0; i < t; ++i)
	{
		int n = getNum();
		int k = getNum();
		int A[n] = {0};
		int B[n] = {0};
	}
	return 0;
}

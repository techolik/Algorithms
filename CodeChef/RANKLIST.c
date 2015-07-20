#include <math.h>
#include <stdio.h>

#ifdef __MINGW32__
#define getchar_unlocked getchar
#endif

static inline long long getNum()
{
    int c = getchar_unlocked() - '0';
    long long res = 0;
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

int main()
{
	int t, i;
	long long n, s, res, r;
	t = getNum();
	while(t--)
	{
		n = getNum();
		s = getNum();
		r = n * (n + 1) / 2 - s;
		if (r == 0)
		{
			printf("0\n");
			continue;
		}
		
		i = 1;
		while (r > n - i)
		{
			r -= (n - i);
			i++;
		}
			
		printf("%d\n", i);
	}
	return 0;
}
#include <cstdio>

static inline int getNum()
{
    int c(getchar() - '0');
    while(c < 0 || c > 9)
         c = getchar() - '0';    
    
    int res = c;
    c = getchar() - '0';
    while(c >= 0 && c < 10){
        res = res * 10 + c;
        c = getchar() - '0';
    }
            
    return res;
}

int main()
{
	printf("Ok");
	return 0;
}
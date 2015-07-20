#include <cstdio>
#include <cstdint>
#include <cinttypes>

using namespace std;

static inline int getNum()
{
    int c=getchar_unlocked() - '0';
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

int main()
{
    int size = 0, i = 0;
    int64_t m = 0, n = 0;
    size = getNum();
    for(i = 0; i < size; ++i)
    {
        m = getNum();
        n = getNum();
        if(m % 2 && n % 2)
            printf("%" PRIu64 "/%" PRIu64 "\n", (m * n - 1) / 2, m * n);
        else
            printf("1/2\n");
    }
   
   return 0;
}
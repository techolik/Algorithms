#include <cstdio>

static inline int getNum()
{
    int c(getchar_unlocked() - '0');
    while(c < 0 || c > 9)
         c = getchar_unlocked() - '0';    
    
    int res = c;
    c = getchar_unlocked() - '0';
    while(c >= 0 && c < 10){
        res = res * 10 + c;
        c = getchar_unlocked() - '0';
    }
            
    return res;
}
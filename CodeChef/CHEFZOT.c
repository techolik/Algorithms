#include <stdio.h>

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
    int max = 0, temp = 0;
    size = getNum();
    for(i = 0; i < size; ++i)
    {
        if(getNum())
            temp ++;
        else{
            if(temp > max) max = temp;
            temp = 0;
        }
    }
    
    if(temp > max) max = temp;   
    
    printf("%d", max);
   
   return 0;
}
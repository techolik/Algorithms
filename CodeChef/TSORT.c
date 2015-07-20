#include <stdio.h>
 
using namespace std;
 
static inline unsigned int getNum()
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
        
    //printf("%d\n", res);
    
    return res;
}
 
static unsigned int temp[1000001] = {0};
 
int main()
{
   int num(0);
   scanf("%d", &num);
   
   while(num --)
       temp[getNum()]++;
   
   for (unsigned int i = 0; i <= 1000000; ++i)
   {
       switch(temp[i])
       {
       case 0:
           continue;
       case 1: 
            printf("%d\n", i);
            break;
       case 2: 
            printf("%d\n%d\n", i, i);
            break;
       case 3: 
            printf("%d\n%d\n%d\n", i, i, i);
            break;
       case 4: 
            printf("%d\n%d\n%d\n%d\n", i, i, i, i);
            break;
       case 5: 
            printf("%d\n%d\n%d\n%d\n%d\n", i, i, i, i, i);
            break;
       case 6: 
            printf("%d\n%d\n%d\n%d\n%d\n%d\n", i, i, i, i, i, i);
            break;
       case 7: 
            printf("%d\n%d\n%d\n%d\n%d\n%d\n%d\n", i, i, i, i, i, i, i);
            break;
       case 8: 
            printf("%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n", i, i, i, i, i, i, i, i);
            break;
       default:
            for (unsigned int j = 0; j < temp[i]; ++j)
                printf("%d\n", i);
       }
   }
   
   return 0;
} 
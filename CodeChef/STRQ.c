#include <stdio.h>
#include <stdlib.h>

#define getchar_unlocked getchar
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

int main(void) {
	int limit = 1000001;
	char str[limit];
    size_t dummy = 0;
    int n = 0;
    int i = 0, j = 0;
    char a = 0, b = 0;
    int l = 0, r = 0, ca = 0, cr = 0;
    /*getline(&str, &dummy, stdin);*/
	/*fgets(str, limit, stdin);*/
	scanf("%s", str);
    scanf("%d", &n);
    for (i = 0; i < n; ++i)
    {
        a = getchar_unlocked();
        while (a < 'a' || a > 'z')
            a = getchar_unlocked();
        b = getchar_unlocked();
        while (b < 'a' || b > 'z')
            b = getchar_unlocked();
        l = getNum();
        r = getNum();
        
        for (j = l - 1; j < r; ++j)
        {
            if (str[j] == a)
                ca++;
            else if(str[j] == b)
                cr += ca;
        }
        
        printf("%d\n", cr);
        ca = 0;
        cr = 0;
    }
    
    free(str);
	return 0;
}


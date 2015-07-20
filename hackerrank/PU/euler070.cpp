#include <cstdio>
int main()
{
    int n = 10000000;
    int* d = new int[n + 1];
    for (int i = 0; i <= n; ++i)
        d[i] = i;
    for (int i = 2; i <= n; ++i)
        if (d[i] == i)
        {
            for (int j = i * 2; j <= n; j += i){
                d[j] = d[j] / i * (i - 1);
                ;
            }
            d[i] -= 1;
        }
    
    //for (int i = 1; i < 20; ++i)
    //    printf("%d\n", d[i]);
        
    int p10[10];
    p10[0] = 1;
    for (int i = 1; i < 10; ++i)
        p10[i] = 10 * p10[i - 1];
    
    int* patterns = new int[n];
    for (int i = 0; i < n; ++i)
    {
        int x = i + 1;
        while(x){
            patterns[i] += p10[x % 10];
            x /= 10;
        }
    }
    
    float mini = 100;
    int res = 0;
    for (int i = 2; i <= n; ++i)
    {
        int t = d[i];
        if (patterns[i - 1] == patterns[t - 1])
        {
            float r = float(i) / t;
            if (r < mini)
            {
                //printf("%d %d %f\n", i, t, r);
                mini = r;
                res = i;
            }
        }
    }
    printf("%d\n", res);
    
    delete d; 
    delete patterns;
    return 0;
}
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
    int t = 0, n = 0, i = 0, mode = 0, num;
    const static int LEN = 100000;
    int arr[LEN];
    scanf("%d", &t);
    while(t--)
    {
        mode = 0;
        memset(arr, 0, LEN * sizeof(int));
        n = getNum();
        i = n;
        for(i = 0; i < n; ++i)
        {
            num = getNum() - 1;
            arr[num]++;
            if (arr[num] > mode)
                mode = arr[num];
        }
        
        printf("%d\n", n - mode);
    }
    
	return 0;
}

/*
	Too bad... took the problem wrong
	
static inline int partition2(int* pData, int p, int r)
{
	int lo = p, hi = 0, t = 0;
	int key = pData[r];
	for (hi = p; hi < r; ++hi)
		if (pData[hi] <= key)
		{
			t = pData[lo];
			pData[lo] = pData[hi];
			pData[hi] = t;
			lo ++;
		}
	pData[r] = pData[lo];
	pData[lo] = key;
	return lo;
}

static inline int select(int* pData, int n, int m)
{
	int k = 0, p = 0, q = 0, r = n - 1;
	while (p < r)
	{
		q = partition2(pData, p, r);
		k = q - p + 1;
		if (m == k)
			return pData[q];
		if (m < k)
			r = q - 1;
		else
		{
			p = q + 1;
			m -= k;
		}
	}
	return pData[p];
}

int main(void)
{
    int t = 0, n = 0, i = 0, median = 0, steps = 0;
    int arr[100000];
    scanf("%d", &t);
    while(t--)
    {
        n = getNum();
        i = n;
        for(i = 0; i < n; ++i)
        {
            arr[i] = getNum();
        }
        median = select(arr, n, (n + 1) / 2);
        for(i = 0; i < n; ++i)
        {
            steps += (arr[i] < median) ? (median - arr[i]) : (arr[i] - median);
        }
        printf("%d\n", steps);
        steps = 0;
    }
    
	return 0;
}
*/

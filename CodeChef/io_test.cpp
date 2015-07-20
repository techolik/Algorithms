#include <cstdio>
#include <iostream>
#include "../3p/cycle.h"
#include "../3p/posix_getline.h"

#ifdef __MINGW32__
#define getchar_unlocked getchar
#endif

using namespace std;

static inline int getNum()
{
    register bool negative = 0;	
    register char c = getchar_unlocked();
    while(c < '0' || c > '9'){
		negative = c == '-';		
		c = getchar_unlocked();
	}
    
    register int res = c - '0';
    c = getchar_unlocked();
    while(c >= '0' && c <= '9'){
        res = res * 10 + (c - '0');
		//res = res << 3 + res << 1 + (c - '0');
        c = getchar_unlocked();
    }
	
	if (negative)
		res = ~(res - 1);
		
    return res;
} 

static inline void scan(int* i)
{
    register bool negative = false;	
    register char c = getchar_unlocked();
    while(c < '0' || c > '9'){
		negative = c == '-';		
		c = getchar_unlocked();
	}
    
    *i = c - '0';
    c = getchar_unlocked();
    while(c >= '0' && c <= '9'){
        *i = *i * 10 + (c - '0');
        c = getchar_unlocked();
    }
	
	if (negative)
		*i = ~(*i - 1);
}

static inline string getStr()
{
	string res;
    register char c = getchar_unlocked();
	while (c < 32 || c > 126)
		c = getchar_unlocked();
	res.push_back(c);
	c = getchar_unlocked();
	while(c >= 32 && c <= 126){
		res.push_back(c);
		c = getchar_unlocked();
	}
	return res;
}
static inline int getStr(char* str)
{
	register int n = 0;
    register char c = getchar_unlocked();
	while (c < 32 || c > 126)
		c = getchar_unlocked();
	str[n++] = c;
	c = getchar_unlocked();
	while(c >= 32 && c <= 126){
		str[n++] = c;
		c = getchar_unlocked();
	}
	return n;
}

//
// 1. 10 ^ 6 of randint(0, 10 ^ 6) each in a line:
//		getNum()	0.654658076
//		getNum()	0.670882368 //no register
//		scan()		0.686085045
//		scanf()		3.171534645
//		cin >> 		2.730607840
//
// 2. Same input but read as string:
//		scanf()			1.875152901
//		cin >> 			2.558219840
//		getline(c++)	2.132453415
//		getline(posix) 	0.845643105
//		getStr()		1.481307778
//		getStr(char*)	0.654742863
//
// 3. Line of string of 10 ^ 7
//
// 4. Write out line of string of 10 ^ 7:
//		printf			59.985262778
//		printf(accum)	1.152226345
//		cout			1.171247118
//		cout(accum)		0.196741428
//		fputs			0.985595585
//		fputs(accum)	0.214025116
int main()
{
    ticks start = getticks();
	int n = 10000000;
	string str(n, '0');
	for (int i = 0; i < n; ++i)
		fputs("a", stdout);
	//cout << str;
	
    double timed = elapsed(getticks(), start);
		
	fprintf(stderr, "%0.9f\n", timed / 1000000000);
	return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

#define getchar_unlocked getchar

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

struct Node{
	char 	ch;
	int 	pi;
	int		stats[4];
};

typedef vector<Node> Nodes;

int main(void) {
	char* str = NULL;
    size_t dummy = 0;
    getline(&str, &dummy, stdin);
    
	int ch = 0, ce = 0, cc = 0, cf = 0;
	Nodes nodes;
	nodes.reserve(1000000);
	int pi_h = 0, pi_e = 0, pi_c = 0, pi_f = 0;
	int i = 0;
	while(str[i] != '\0')
	{
		Node node;
		node.ch = str[i];
		node.stats[0] = ch;
		node.stats[1] = ce;
		node.stats[2] = cc;
		node.stats[3] = cf;
		if (str[i] == 'h')
		{
			node.pi = pi_h;
			pi_h = i;
			ch++;
		}
		else if(str[i] == 'e')
		{
			node.pi = pi_e;
			pi_e = i;
			ce++;
		}
		else if(str[i] == 'c')
		{
			node.pi = pi_c;
			pi_c = i;
			cc++;
		}
		else
		{
			node.pi = pi_f;
			pi_f = i;
			cf++;
		}
		
		nodes.push_back(node);
		i++;
	}

    int n = 0;		
    scanf("%d", &n);
    for (int j = 0; j < n; ++j)
    {
        char a = getchar_unlocked();
        while (a < 'a' || a > 'z')
            a = getchar_unlocked();
        char b = getchar_unlocked();
        while (b < 'a' || b > 'z')
            b = getchar_unlocked();
        int l = getNum() - 1;
        int r = getNum() - 1;        
        
		while (nodes[r].ch != b)
			r--;
		Node last = nodes[r];
		Node& first = nodes[l];
		int count_i = 0;
		if (a == 'e')
			count_i = 1;
		else if (a == 'c')
			count_i = 2;
		else if (a == 'f')
			count_i = 3;
			
		int count_remove = first.stats[count_i];
		int result = 0;
		while (1)
		{
			result += (last.stats[count_i] - count_remove);
			if (last.pi > l)
				last = nodes[last.pi];
			else
				break;
		}
        
        printf("%d\n", result);
    }
    
    free(str);
	return 0;
}


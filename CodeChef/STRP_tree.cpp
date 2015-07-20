#include <iostream>
#include <cstdio>
#include <cstring>
#include <stack>
#include <cstdint>
#include <cinttypes>

using namespace std;

//#define getchar_unlocked getchar

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

static inline string getStr()
{
	string str;
    int c = getchar_unlocked();
    while(c < 'a' || c > 'z')
         c = getchar_unlocked();    
    
    while(c >= 'a' && c <= 'z'){
		str.push_back(c);
        c = getchar_unlocked();
    }
            
    return str;
}

#define IC 0
#define IE 1
#define IF 2
#define IH 3

#define ICE 0
#define ICF 1
#define ICH 2
#define IEC 3
#define IEF 4
#define IEH 5
#define IFC 6
#define IFE 7
#define IFH 8
#define IHC 9
#define IHE 10
#define IHF 11

struct Node
{
	bool	leaf;
	int 	start;
	int 	end;
	int		mid;
	Node*	pLeft;
	Node*	pRight;
	
	uint32_t	stats[4]; 
	uint64_t	rels[12]; 
	
	Node(int start, int end, bool leaf = false) :
		leaf(leaf),
		start(start),
		end(end),
		pLeft(NULL),
		pRight(NULL)
	{
		mid = start + (end - start) / 2;
		memset(stats, 0, sizeof(int32_t) * 4);
		memset(rels, 0, sizeof(int64_t) * 12);
	}
	~Node()
	{
		delete pLeft;
		delete pRight;
	}
	
	void update(const string& str)
	{
		if (leaf)
		{
			for (int i = start; i <= end; ++i)
			{
				switch(str[i])
				{
					case 'c':
						stats[IC] += 1;
						rels[IEC] += stats[IE];
						rels[IFC] += stats[IF];
						rels[IHC] += stats[IH];
						break;
					case 'e':
						stats[IE] += 1;
						rels[ICE] += stats[IC];
						rels[IFE] += stats[IF];
						rels[IHE] += stats[IH];
						break;
					case 'f':
						stats[IF] += 1;
						rels[ICF] += stats[IC];
						rels[IEF] += stats[IE];
						rels[IHF] += stats[IH];
						break;
					case 'h':
						stats[IH] += 1;
						rels[ICH] += stats[IC];
						rels[IEH] += stats[IE];
						rels[IFH] += stats[IF];
						break;
				}
			}
		}
		else
		{
			for (int i = 0; i < 4; ++i)
			{
				stats[i] = pLeft->stats[i] + pRight->stats[i];
			}
			rels[ICE] = pLeft->rels[ICE] + pRight->rels[ICE] + pLeft->stats[IC] * pRight->stats[IE];
			rels[ICF] = pLeft->rels[ICF] + pRight->rels[ICF] + pLeft->stats[IC] * pRight->stats[IF];
			rels[ICH] = pLeft->rels[ICH] + pRight->rels[ICH] + pLeft->stats[IC] * pRight->stats[IH];
			
			rels[IEC] = pLeft->rels[IEC] + pRight->rels[IEC] + pLeft->stats[IE] * pRight->stats[IC];
			rels[IEF] = pLeft->rels[IEF] + pRight->rels[IEF] + pLeft->stats[IE] * pRight->stats[IF];
			rels[IEH] = pLeft->rels[IEH] + pRight->rels[IEH] + pLeft->stats[IE] * pRight->stats[IH];
			
			rels[IFC] = pLeft->rels[IFC] + pRight->rels[IFC] + pLeft->stats[IF] * pRight->stats[IC];
			rels[IFE] = pLeft->rels[IFE] + pRight->rels[IFE] + pLeft->stats[IF] * pRight->stats[IE];
			rels[IFH] = pLeft->rels[IFH] + pRight->rels[IFH] + pLeft->stats[IF] * pRight->stats[IH];
			
			rels[IHC] = pLeft->rels[IHC] + pRight->rels[IHC] + pLeft->stats[IH] * pRight->stats[IC];
			rels[IHE] = pLeft->rels[IHE] + pRight->rels[IHE] + pLeft->stats[IH] * pRight->stats[IE];
			rels[IHF] = pLeft->rels[IHF] + pRight->rels[IHF] + pLeft->stats[IH] * pRight->stats[IF];
		}
	}
	
	int stat_index(char a)
	{
		if (a == 'c')
			return IC;		
		if (a == 'e')
			return IE;
		if (a == 'f')
			return IF;
		if (a == 'h')
			return IH;
	}
	int rels_index(char a, char b)
	{
		if (a == 'c')
		{
			if (b == 'e')
				return ICE;		
			if (b == 'f')
				return ICF;	
			if (b == 'h')
				return ICH;	
		}
		if (a == 'e')
		{
			if (b == 'c')
				return IEC;		
			if (b == 'f')
				return IEF;	
			if (b == 'h')
				return IEH;	
		}
		if (a == 'f')
		{
			if (b == 'c')
				return IFC;		
			if (b == 'e')
				return IFE;	
			if (b == 'h')
				return IFH;	
		}
		if (a == 'h')
		{
			if (b == 'c')
				return IHC;	
			if (b == 'e')
				return IHE;		
			if (b == 'f')
				return IHF;	
		}
	}
	
	uint64_t find_words(const string& str, char a, char b, int l, int r)
	{
		Node* pBranch = this;
		
		// Walk till we have to split
		while(!pBranch->leaf)
		{
			if (l > pBranch->mid)		
				pBranch = pBranch->pRight;
			else if(r <= pBranch->mid)
				pBranch = pBranch->pLeft;
			else
				break;
		}
		
		uint32_t ca = 0;
		uint64_t cab = 0;
		if(pBranch->leaf)
		{
			// Get the result on the leaf
			for (int i = l; i <= r; ++i)
			{
				if (str[i] == a)
					ca++;
				else if(str[i] == b)
					cab += ca;
			}
			return cab;
		}
		
		// Walk down towards the left leaf and stack up the right wings along the way
		stack<Node*> right_wings;
		Node* pLeftLeaf = pBranch->pLeft;
		while (!pLeftLeaf->leaf)
		{
			if (l > pLeftLeaf->mid)
				pLeftLeaf = pLeftLeaf->pRight;
			else
			{
				right_wings.push(pLeftLeaf->pRight);
				pLeftLeaf = pLeftLeaf->pLeft;				
			}			
		}
		
		int ia = stat_index(a);
		int ib = stat_index(b);
		int iab = rels_index(a, b);
		
		// Get the result on the leaf
		for (int i = l; i <= pLeftLeaf->end; ++i)
		{
			if (str[i] == a)
				ca++;
			else if(str[i] == b)
				cab += ca;
		}		
		
		// Walk up towards the branching node and add up with the right wings
		while (!right_wings.empty())
		{
			Node* pRightWing = right_wings.top();
			cab = cab + pRightWing->rels[iab] + ca * pRightWing->stats[ib];
			ca += pRightWing->stats[ia];
			right_wings.pop();
		}
		
		// Then walk down towards the right leaf and add up with the left wings along the way
		Node* pRightLeaf = pBranch->pRight;
		while (!pRightLeaf->leaf)
		{
			if (r <= pRightLeaf->mid)
				pRightLeaf = pRightLeaf->pLeft;
			else
			{
				Node* pLeftWing = pRightLeaf->pLeft;
				cab = cab + pLeftWing->rels[iab] + ca * pLeftWing->stats[ib];
				ca += pLeftWing->stats[ia];
				
				pRightLeaf = pRightLeaf->pRight;
			}			
		}
		
		// We're finally at the right leaf...
		for (int i = pRightLeaf->start; i <= r; ++i)
		{
			if (str[i] == a)
				ca++;
			else if(str[i] == b)
				cab += ca;
		}		
		
		return cab;
	}	
}; 

const static int s_threshold = 100;
Node* build_tree(const string& str, int start, int end)
{
	Node* pNode(NULL);
	if (end - start < s_threshold){
		pNode = new Node(start, end, true);
	}
	else
	{	
		int mid = start + (end - start) / 2;
		Node* pLeft = build_tree(str, start, mid);
		Node* pRight = build_tree(str, mid + 1, end);
		
		pNode = new Node(start, end);
		pNode->pLeft = pLeft;
		pNode->pRight = pRight;
	}
	pNode->update(str);
	
	return pNode;
}

int main(void)
{
	string str;// = getStr();
    getline(cin, str);
	//return 0;
	Node* pRoot = build_tree(str, 0, str.size() - 1);
    int n = getNum();
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
        /*
		if (a == b)
			printf("%d\n", 0);
		else
			 */
			printf("%" PRIu64 "\n", pRoot->find_words(str, a, b, l, r));
    }
    
	delete pRoot;
	return 0;
}



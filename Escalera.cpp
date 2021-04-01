#include <iostream>
#include <cstdio>

using namespace std;

long long int DP(int Esca)
{
	if (Esca > n)
		return 0;
	if (Esca == n)
		return 1;
	if (memo[Esca] == -1)
	{
		for (int i = 1; i <= k; i++)
			memo[Esca] += DP(Esca + i);
		memo[Esca]++;
	}
	return memo[Esca];

	
}

int main (void)
{

	cin >> N >> k;

}
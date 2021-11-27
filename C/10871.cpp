#include <stdio.h>
#pragma warning(disable:4996)

int main()
{

// [0] 변수 선언부 
	int N	 = 1;
	int X	 = 0;
	int A[100001] = {0};

// [1] 데이터 입력
	scanf("%d %d", &N, &X);
	
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &A[i]); 
	}

// [2] X보다 작은 수 출력
	for (int i = 0; i < N; i++)
	{
		if (A[i] < X)
		{
			printf("%d ", A[i]);
		}
	}

	return 0;

}

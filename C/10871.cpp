#include <stdio.h>
#pragma warning(disable:4996)

int main()
{

// [0] ���� ����� 
	int N	 = 1;
	int X	 = 0;
	int A[100001] = {0};

// [1] ������ �Է�
	scanf("%d %d", &N, &X);
	
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &A[i]); 
	}

// [2] X���� ���� �� ���
	for (int i = 0; i < N; i++)
	{
		if (A[i] < X)
		{
			printf("%d ", A[i]);
		}
	}

	return 0;

}

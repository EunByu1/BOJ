#include <stdio.h>

#define SIZE 100

int main()
{

// [0] ���� ����� 
	int iTestCase = 0;
	int iSum[SIZE] = {};
	int i, j  = 0;
	int index = 0;
	int A 	  = 0;
	int B 	  = 0;

	
// [1] �׽�Ʈ ���̽��� ���� �Է� 
	scanf("%d", &iTestCase);
	
	
// [2] �׽�Ʈ ���̽��� ������ŭ ���� �Է�&���� �� ����  
	while(i < iTestCase)
	{
		
		scanf("%d %d", &A, &B);
		iSum[index] = A + B;
		
		index++;  	
		i++;
	
	}


// [3] �׽�Ʈ ���̽��� ������ŭ �迭 �� ��� 	
	for(int i = 0; i < iTestCase; i++)
	{
		printf("%d \n", iSum[i]);
	} 
	
	
	return 0;
	
}

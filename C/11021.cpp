#include <stdio.h>

#define SIZE 150

int main()
{
	
// [0] ���� �����
	int TestCase = 0;
	int iCount   = 0;
	int A	     = 0;
	int B	     = 0;
	int iStore[SIZE] = {0};
	
			
// [1] ������ �Է� (�׽�Ʈ ���̽��� ���� �Է�) 
	scanf("%d", &TestCase);
	
	
// [2] �׽�Ʈ ���̽��� ������ŭ ������ �߰� �Է� �� ���� -> ����  
	while(iCount < TestCase)
	{
		scanf("%d %d", &A, &B);
		iStore[iCount] = A+B;
		
		iCount++;
	}
	iCount = 0;
	 
	  
// [3] ����� �� ��� 
	while(iCount < TestCase)
	{
		printf("Case #%d: %d \n", iCount+1, iStore[iCount]);
		
		iCount ++;
	}

	return 0;
	 
}

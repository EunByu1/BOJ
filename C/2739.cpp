#include <stdio.h>

int main()
{
	
	// [0] ���� ����� 
	int iStep = 0;
	 
	 
	// [1] ������ �Է� 
	scanf("%d", &iStep);
	
	
	// [2] for���� ���� ������ ��� 
	for(int iValue = 1; iValue < 10; iValue++)
	{
		printf("%d * %d = %d \n", iStep, iValue, iStep * iValue);
	}

	return 0; 
	 
}

#include <stdio.h>

int main()
{

// [0] ���� �����  
	int iSum = 0;
	int in	 = 0;

		
// [1] ������ �Է� 
	scanf("%d", &in);


// [2] ���� 
	for(int i=1; i<in+1; i++)
	{
		iSum += i;
	}


// [3] ȭ�� ���
	printf("%d", iSum);

	return 0;

}

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{

// [0] ���� ����� 
	int iStarNum = 0;


// [1] ������ �Է�
	scanf("%d", &iStarNum);


// [2] ù° �ٺ��� N��° �ٱ��� ���ʴ�� �� ��� 
	for (int i = 1; i < iStarNum + 1; i++)
	{
		for (int j = 0; j < iStarNum - i; j++)
		{
			printf(" ");
		} // for (int j = 0; j < iStarNum - i; j++)

		for (int k = 0; k < i; k++)
		{
			printf("*");
		} // for (int k = 0; k < i; k++)

		printf("\n");
	}	  // for (int i = 1; i < iStarNum + 1; i++)

	return 0;

}

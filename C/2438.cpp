#include <stdio.h>

int main()
{

// [0] ���� ����� 
	int iStarNum = 0;


// [1] ������ �Է� -> ���� 
	scanf("%d", &iStarNum);
	
	
// [2] ����� ����ŭ loop -> �� ��� 
	for(int i = 1; i<iStarNum+1; i++)
	{
		for(int j = 0; j<i; j++ )
		{
			printf("*");
		}	// for(int j = 0; j<i; j++ )
		
		printf("\n");
	}	    // for(int i = 1; i<iStarNum+1; i++)
	
	return 0;
	
}


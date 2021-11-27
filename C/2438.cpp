#include <stdio.h>

int main()
{

// [0] 변수 선언부 
	int iStarNum = 0;


// [1] 데이터 입력 -> 저장 
	scanf("%d", &iStarNum);
	
	
// [2] 저장된 값만큼 loop -> 별 출력 
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


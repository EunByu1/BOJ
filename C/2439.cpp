#include <stdio.h>
#pragma warning(disable:4996)

int main()
{

// [0] 변수 선언부 
	int iStarNum = 0;


// [1] 데이터 입력
	scanf("%d", &iStarNum);


// [2] 첫째 줄부터 N번째 줄까지 차례대로 별 출력 
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

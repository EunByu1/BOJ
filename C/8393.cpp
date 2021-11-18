#include <stdio.h>

int main()
{

// [0] 변수 선언부  
	int iSum = 0;
	int in	 = 0;

		
// [1] 데이터 입력 
	scanf("%d", &in);


// [2] 연산 
	for(int i=1; i<in+1; i++)
	{
		iSum += i;
	}


// [3] 화면 출력
	printf("%d", iSum);

	return 0;

}

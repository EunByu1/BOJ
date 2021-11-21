#include <stdio.h>

int main()
{

// [0] 변수 선언부 
	int user = 0;
	
	
// [1] 데이터 입력  
	scanf("%d", &user);


// [2] 첫째 줄부터 N번째 줄 까지 차례대로 출력
	for(int i=0; i<user; i++)
	{
		printf("%d \n", i+1);
	}
	
	
	return 0;

}


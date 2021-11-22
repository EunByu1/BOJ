#include <stdio.h>

int main()
{

// [0] 변수 선언부 
	int user = 0;


// [1] 데이터 입력 
	scanf("%d", &user); 


// [2] N부터 1까지 한 줄에 하나씩 출력
	while(1)
	{
		printf("%d \n", user);
		user = user - 1;
		
		if (user == 0)
		{
			break;
		} 
	}
	
	return 0;
	
}
 

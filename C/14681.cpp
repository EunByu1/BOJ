# include <stdio.h>

int main()
{
	
// [0] 변수 선언부  
	int x;
	int y; 
	
	
// [1] 데이터 입력  
	scanf("%d", &x);
	scanf("%d", &y);


// [2] 조건 비교 후 출력  
	if (( x > 0 ) && ( y > 0 ))
	{
    	printf("1");
	}
	else if (( x > 0 ) && ( y < 0 ))
	{
    	printf("4");
	}
	else if (( x < 0 ) && ( y > 0 ))
	{
    	printf("2");
	}
	else
	{
    	printf("3");
	}
	
	return 0;

}	// int main()

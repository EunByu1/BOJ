# include <stdio.h>

int main()
{

// [0] 변수 선언부  
	int year; 


// [1] 데이터 입력
	scanf("%d", &year);


// [2] 조건 비교 및 출력
	if (( year % 4 ) == 0) 
	{
		if ((year % 100 ) != 0)
		{ 
        	printf("1");
    	}
		
		else if (( year % 400 ) == 0) 
		{
			printf("1");
		}
    	
		else 
		{
    		printf("0");
		}
	}		// if ( ( year % 4 ) == 0 ) 
	else 
	{
    	printf("0");
	}		//else 

return 0;

}

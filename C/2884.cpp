# include <stdio.h>

int main()
{
	
// [0] 변수 선언
	int hour   = 0;
	int minute = 0; 


// [1] 데이터 입력
	scanf("%d %d", &hour, &minute); 


// [2] 조건 비교 후 값 할당 
	if((0 <= minute) && (minute < 45))
	{
    	minute += 15;    
    	if((0 < hour) && (hour <= 23))
    	{
        	hour -= 1;
		}
		else
		{
        	hour = 23;  
		}
	}
	else
	{
 	   minute -= 45;
	}	


// [3] 데이터 출력 
	printf("%d %d", hour, minute);


	return 0;

} // int main()

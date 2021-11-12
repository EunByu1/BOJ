# include <stdio.h>

int main()
{
	
// [0] 변수 선언부 
	int score;
	
// [1] 값을 입력받음 
	scanf("%d", &score);				

// [2] 조건에 맞게 값을 출력함 
	if (score >= 90)
	{
	    printf("A");
	}

	else if (score >= 80)
	{
    	printf("B");
	}
	else if (score >= 70)
	{
    	printf("C");
	}
	else if (score >= 60)
	{
    	printf("D");
	}
	else
	{
    	printf("F");
	}	
	
	return 0;
}

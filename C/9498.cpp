# include <stdio.h>

int main()
{
	
// [0] ���� ����� 
	int score;
	
// [1] ���� �Է¹��� 
	scanf("%d", &score);				

// [2] ���ǿ� �°� ���� ����� 
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

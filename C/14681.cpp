# include <stdio.h>

int main()
{
	
// [0] ���� �����  
	int x;
	int y; 
	
	
// [1] ������ �Է�  
	scanf("%d", &x);
	scanf("%d", &y);


// [2] ���� �� �� ���  
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

# include <stdio.h>

int main()
{
	
// [0] ���� ����
	int hour   = 0;
	int minute = 0; 


// [1] ������ �Է�
	scanf("%d %d", &hour, &minute); 


// [2] ���� �� �� �� �Ҵ� 
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


// [3] ������ ��� 
	printf("%d %d", hour, minute);


	return 0;

} // int main()

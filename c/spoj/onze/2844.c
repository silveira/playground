#include<stdio.h>

int toogle = 0;
long int delta = 0;

void push_char(char current){
	if(current=='\n') {
		if(delta%11==0) {
			printf(" is a multiple of 11.\n");
		} else {
			printf(" is not a multiple of 11.\n");
		}

		toogle = 0;
		delta = 0;
		return;	
	} else {
		putchar(current);
	}

	if(toogle) {
		delta += current - '0';
	} else {
		delta -= current - '0';
	}

	toogle = !toogle;
}

int main(int argc, char* argv[]){
	char c;
	char last_c = '_';
	unsigned int counter = 1;

	c = getchar();

	while( !( (last_c=='0')&&(c=='\n')&&counter==2 )){
		if(c=='\n')
			counter=0;

		if(counter == 2 && last_c=='0'){
			push_char(last_c);
		}

		if(!( c=='0' && counter == 1)){
			push_char(c);
		} 

		last_c = c;
		c = getchar();
		counter++;
	}

	return 0;
}


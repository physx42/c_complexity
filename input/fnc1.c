// Prototypes
int fnc1(int x, int y);



int fnc1(int x, int y) {
	/* THis is a  comment */
	int a, b, c;
	c = x*x + y*y;
	/* This anif statement */
	if (c > 10) {
		a = c;
	}
	else {
		b = c;
	}
	
	c = a - b;
	b++;
	
	/*fnc2(c,b);*/
	
	while(1)
		break;
	
	return (c);
}

int main() {
	int m, n;
	m = 1;
	n = 54;
	fnc1(m,n);
	return 0;
}
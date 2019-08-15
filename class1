//numberSquare
//Language/Type: C++ parameters for %
//Author: Marty Stepp (on 2016/08/27)

//Write a function named numberSquare that accepts two integer parameters, a min and a max, and prints the numbers in the range from min to max inclusive in a square pattern. Each line of the square consists of a wrapping sequence of integers increasing from min and max. The first line begins with min, the second line begins with min + 1, and so on. When the sequence in any line reaches max, it wraps around back to min. You may assume that min is less than or equal to max. For example, the call of numberSquare(1, 5); should print:

//12345
//23451
//34512
//45123
//51234

//Solution:

//Shift Left

void numberSquare(int min, int max) {
    int col = max-min;
    int ix;
    int iy;
    
    for (int i=min; i<max+1; i++) {
        
        for (int ix=min;ix<min+col+1;ix++) {
            cout << ix-min+i;
            }
        
        for (int iy=min+col; iy<max; iy++) {
            cout << iy-max+i;
            }     
        
        cout << '\n';
        col--;
        
    }
}

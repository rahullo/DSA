// #include<iostream>

// using namespace std;
// int main()
// {
//     int num = 4, num2 = 4;
//     int num3 = 4, num4 = 4;
//     char ch = 'r';
//     char name = 'r';

//     // cout<<num<<" is the value of num and\n"<<num2<<" is the value of num2 ";
//     cout<<num++<<" "<<num<<endl;
//     cout<<++num2<<endl;
//     cout<<num3--<<" "<<num3<<endl;
//     cout<<--num4<<endl;

//     return 0;

// }

//////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int c = 45;
// int main()
// {
//     // int a, b, c, glo;
//     // cout<<"Enter the value of a: "<<endl;
//     // cin>>a;
//     // cout<<"Enter the value of b: "<<endl;
//     // cin>>b;
//     // c = a + b;
//     // cout<<"The sum is "<<c<<endl;
//     // glo = a + b +::c;
//     // cout<<"The global value of c is "<<::c<<endl;
//     // cout<<"The sum of a, b & global value is "<<glo;

//     float d = 34.4;
//     long double e = 34.4;
//     cout<<"The value of d is "<<d<<endl<<"The value of e is "<<e;

//     return 0;
// }
//////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

//   *******************Table Program***************************

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a, i, pro;
//     cout<<"Enter the number: "<<endl;
//     cin>>a;
//     for ( i = 1; i <= 10; i++)
//     {
//         pro = a * i;
//         cout<<a<<" X "<<i<<" = "<<pro<<endl;
//     }

//     return 0;
// }

///  0, 1, 1, 2, 3, 5, 8, 13, 21
///////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////
////  *******************If else **********************

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int age;
//     cout<<"Tell me your age"<<endl;
//     cin>>age;
//     if(age<18 ) {
//         cout<<"You can't come to our group";
//         return 0;
//     }
//     else{
//         cout<<"You can join our group: ";
//         return 0;
//     }
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int age, i;
//     cout<<"Tell me your age: "<<endl;
//     cin>>age;
//     switch (age)
//     {
//     case 18:
//         cout<<"You are under age";
//         break;
//     case 22:
//     cout<<"You are eligible: ";
//     break;

//     case 35:
//         cout<<"You area aged: ";
//         break;

//     default:
//         cout<<"Special case not allowed! ";
//         break;
//     }
//     return 0;
// }

///////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
// //********** Pointer ********************

// #include<iostream>
// #include<stdio.h>

// using namespace std;

// void swapping(int* a , int* b) {
//     int temp = *a;
//     *a = *b;
//     *b = temp;

// }
// int main()
// {
//     int a = 3, b = 5;
//     cout<<a<<"\t"<<b<<endl;
//     swapping(&a, &b);
//     cout<<a<<"\t"<<b;
//     return 0;
// }

///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////
/// class

// #include<iostream>
// #include<stdio.h>
// #include<string.h>

// using namespace std;

// class Binary {
//         string s;
//         void chk_bin(void);
//     public:
//         void read(void);
//         void display(void);
//         void ones(void);
// };

// void Binary::read(){
//     cout<<"Enter the binary number: "<<endl;
//     cin>>s;
// }

// void Binary::chk_bin(void){
//     for (int i = 0; i < s.length(); i++)
//     {
//         if(s.at(i) != '0' && s.at(i) != '1'){
//             cout<<endl<<"Entered input is not binary number!!!"<<endl;
//             break;
//         }
//     }

// }

// void Binary::display(){
//     chk_bin();
//     cout<<"Displaying your binary number: "<<endl;
//     for(int i = 0; i< s.length(); i++){
//         cout<<s.at(i);
//     }
// }

// void Binary:: ones(){
//     chk_bin();
//     for (int i = 0; i < s.length(); i++)
//     {
//         if(s.at(i) == '0'){
//             s.at(i) = '1';
//         }
//         else{
//             s.at(i) = '0';
//         }
//     }

// }

// int main()
// {
//     Binary b;
//     b.read();
//     b.display();
//     b.ones();
//     b.display();
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Shop
// {
// private:
//     int id[1000];
//     int price[1000];
//     int counter;
// public:
//     void init_counter(void){
//         counter = 0;
//         };
//     void setIdPrice(void);
//     void displayIdPrice(void);
// };

// void Shop:: setIdPrice(void){
//     cout<<"Enter the Id of product: "<< endl;
//     cin>>id[counter];
//     cout<<"Enter the price of product: "<<endl;
//     cin>>price[counter];
//     counter++;

// }

// void Shop:: displayIdPrice(void){
//     for (int i = 0; i < counter; i++)
//     {
//         cout<<"Price of ID "<<id[i]<<" is "<<price[i]<<" ."<<endl;
//     }

// }

// int main()
// {
//     Shop shopping;
//     shopping.init_counter();
//     shopping.setIdPrice();
//     shopping.setIdPrice();
//     shopping.setIdPrice();
//     shopping.setIdPrice();

//     shopping.displayIdPrice();
//     return 0;
// }

//// FRIEND CLASS;;

// #include <iostream>
// #include <stdio.h>

// using namespace std;

// class Complex;

// class Calculator
// {
// public:
//     int add(int a, int b)
//     {
//         return (a + b);
//     }

//     int sumOfComplex(Complex, Complex);
// };

// class Complex
// {
//     int a, b;
//     friend int Calculator ::sumOfComplex(Complex, Complex);

// public:
//     void setData(int num1, int num2)
//     {
//         a = num1;
//         b = num2;
//     }
//     void printNumber()
//     {
//         cout << "Your number is " << a << " + " << b << "i" << endl;
//     }
// };

// int Calculator::sumOfComplex(Complex o1, Complex o2)
// {
//     return ((o1.a) + (o2.a));
// }

// int main()
// {
//     Complex o1, o2;
//     o1.setData(2, 1);
//     o2.setData(4, 3);
//     Calculator cal;
//     int res = cal.sumOfComplex(o1, o2);
//     cout << endl
//          << res;
//     return 0;
// }


// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Y;


// class X{
//     int val1;
//     friend void swapping(X &, Y &);
//     public:
//         void setData(int val) {
//             val1 = val;
//         }

//         void displayData() {
//             cout<< val1<<endl;
//         }
// };

// class Y{
//     int val2;
//     friend void swapping(X &, Y &);
//     public:
//         void setData(int val) {
//             val2 = val;
//         }

//         void displayData() {
//             cout<< val2<<endl;
//         }
// };

// void swapping(X & a, Y & b) {
//     int temp = a.val1;
//     a.val1 = b.val2;
//     b.val2 = temp;
// }

// int main()
// {
//     X o1;
//     o1.setData(3);
//     Y o2;
//     o2.setData(5);  
//     o1.displayData();
//     o2.displayData();
//     swapping(o1, o2);
//     o1.displayData();
//     o2.displayData();
//     return 0;
// }


// constructor

// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Complex {
//     int a, b;
    
//     public:
//         Complex();

//         void printData(void){
//             cout<<"The sum of complex data is "<< a<< " + "<< b<<"i"<<endl;
//         }
// };

// Complex::Complex(void) {
//     a = 0;
//     b =0;
// }
// int main()
// {
//     Complex c1;
//     c1.printData();


    
//     return 0;
// }

//////////////////////////////////////////////////////////////
/////////////////////////////////////////////

// Parameterized constructor

// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Complex {
//     int a, b;
    
//     public:
//         Complex(int , int);

//         void printData(void){
//             cout<<"The sum of complex data is "<< a<< " + "<< b<<"i"<<endl;
//         }
// };

// Complex::Complex(int x, int y) {
//     a = x;
//     b = y;
// }
// int main()
// {
//     Complex c1(4, 5);
//     c1.printData();

//     Complex c2 = Complex(6, 7);
//     c2.printData();

    
//     return 0;
// }
////////////////////////////////
/////////////////////////////////////////
// #include<iostream>
// #include<stdio.h>
// #include<math.h>

// using namespace std;

// class Point{
//     int x, y;
//     friend int calculateDistance(Point , Point);
//     public:
//         Point(int, int);

//         void displayPoint(){
//             cout<<"The point is ("<<x<<", "<<y<< ")"<< endl;
//         }
// };

// Point:: Point(int a, int b){
//             x = a;
//             y = b;
//         }


// int calculateDistance(Point p1, Point p2) {
//     int c;
//     c = sqrt(((p1.x - p2.x)*(p1.x - p2.x)) +((p1.y - p2.y)*(p1.y - p2.y) ));
//     cout<<c<<endl;
//     return 0;
// };


// int main()
// {
//     Point p1(0, 1);
//     p1.displayPoint();

//    Point p2(0, 6);
//    p2.displayPoint();
//    calculateDistance(p1, p2);
    
//     return 0;
// }


//////////////////////////////////////////////////////////////////
///////////////////////////////////////////////
///INHERITANCE
// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Base{
//     int data1;
// public:
//     int data2;
//     void setData();
//     int getData1();
//     int getData2();
// };

// void Base:: setData(void){
//     data1 = 10;
//     data2 = 20;
// }

// int Base:: getData1(void){
//     return data1;
// }

// int Base::getData2(void){
//     return data2;
// }


// class Derived: public Base{
//     int data3;
// public:
//     void process();
//     void displayData();
// };

// void Derived::process(void){
//     data3 = data2* getData1();
// }

// void Derived:: displayData(void){
//     cout<<"Value of data 1 is "<<getData1()<<endl;
//     cout<<"Value of data 2 is "<<data2<<endl;
//     cout<<"Value of data 3 is "<<data3<<endl;


// }


// int main()
// {
//     Derived der;
//     der.setData();
//     der.process();
//     der.displayData();
//     return 0;
// }



// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Student{
//     protected:
//         int roll_number;

//     public:
//         void set_roll_number(int);
//         void get_roll_number();
// };

// void Student::set_roll_number(int roll){
//     roll_number = roll;
// }

// void Student::get_roll_number(){
//     cout<<"The roll number is "<<roll_number<<endl;
// }

// class Exam: public Student{
//         float maths;
//         float physics;
//     public:
//         void set_marks(float, float );
//         void get_marks();
// };

// void Exam::set_marks(float m1, float m2){
//     maths = m1;
//     physics = m2;
// }

// void Exam::get_marks(){
//     cout<<"The obtained marks in maths is: "<<maths<<endl;
//     cout<<"The obtained physics in maths is: "<<physics<<endl;
    
// }

// int main()
// {
    
//     return 0;
// }
////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
////////  Multiple Inheritance     /////////////

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// class Base1 {
// protected:
//     int base1int;
// public:
//     void set_base1int(int a){
//         base1int = a;
//     }
//     void show_base1(){
//         cout<<"The value of base1int "<<base1int<<endl;
//     }
// };

// class Base2 {
// protected:
//     int base2int;
// public:
//     void set_base2int(int a){
//         base2int = a;
//     }
//     void show_base2(){
//         cout<<"The value of base2int "<<base2int<<endl;
//     }
// };

// class Base3: public Base1, public Base2{
//     public:
//         void show(){
//             cout<<"The value of base1 is "<< base1int<<endl;
//             cout<<"The value of base2 is "<< base2int<<endl;
//             cout<<"The sum of values of base1 and base2 is "<< base1int + base2int<<endl;
//         }
// };


// int main()
// {
//     Base1 b1;
//     Base2 b2;
//     b1.set_base1int(3);
//     b1.show_base1();
//     b2.set_base2int(4);
//     b2.show_base2();
//     Base3 b3;
//     b3.set_base1int(30);
//     b3.set_base2int(42);
//     b3.show();
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>
// #include<math.h>

// using namespace std;

// class SimpleCalculator {
//     protected:
//         int num1, num2;
//     public:
//         void getNums(int a, int b){
//             num1 = a;
//             num2 = b;
//         }

//         void results(){
//             cout<<"The sum of num1 and num2 is "<<num1+num2<<endl;
//             cout<<"The subtraction of num1 and num2 is "<<num1-num2<<endl;
//             cout<<"The product of num1 and num2 is "<<num1*num2<<endl;
//             cout<<"The division of num1 and num2 is "<<num1/num2<<endl;

//         }
// };

// class ScietificCalculator: virtual public SimpleCalculator{
//     public:
        
//         void ShowResults(){
//             cout<<"The num1 to the power of num2 is "<<pow(num1, num2)<<endl;
//             cout<<"The sqare root of num1 and num2 is "<<sqrt(num1)<<" and "<< sqrt(num2)<<endl;

//         }
// };

// class HybridCalculator: public SimpleCalculator, public ScietificCalculator {
//         int num1, num2;
    
// };

// int main()
// {
//     SimpleCalculator simple;
//     ScietificCalculator science;
//     simple.getNums(2, 3);
//     simple.results();
//     cout<<endl;
//     science.getNums(4, 3);
//     science.ShowResults();
//     cout<<endl;
//     HybridCalculator hybrid;
//     hybrid.getNums(6, 2);


//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a, i;
//     cout<<"Enter the value of a: "<<endl;
//     cin>>a;
//     for(i = 1 ; i<= a ; i++){
//         cout<<i<<endl;
//     }
//     return 0;
// }


///VIRTUAL function >>/////
// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Base {
//     int a = 1;
//     public:
//         virtual void display(){
//             cout<<"1 The value of base class a is: "<<a<<endl;
//         }
// };

// class Derived: public Base {
//     int b = 2;
//     public:
//         void display(){
//             cout<<"2 The value of Derived class b is: "<<b<<endl;
//         }
// };


// int main()
// {
//     Base* b;
//     Base b1;
//     Derived* d;
//     Derived d1;
//     b = &d1;
//     b->display();

//     // b1.display();
//     // d1.display();
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a= 1, b = 2;
//     int* ptra = &a;
//     int* ptrb = &b;
//     cout<<a<<" "<<b;
//     int temp = (*ptra);
//     *ptra =  (*ptrb);
//     *ptrb = temp;
//     cout<<endl;
//     cout<<a<<" "<<b;
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;

// class Distance {
//     int d1, d2;
//     public:
//         void set_data(void){
//             cout<<"Enter the d1 and d2: "<<endl;
//             cin>>d1>>d2;
//         }
//         friend Distance sum_distance(Distance d1, Distance d2);
// };

// Distance sum_distance(Distance d1, Distance d2){
//     Distance sum;
//     sum = d1 + d2;
//     return sum;
// }

// int main()
// {
//     Distance dis;
//     dis.set_data();
//     // sum_distance();
//     return 0;
// }


// #include<iostream>
// #include<stdio.h>
// #include<cstring>

// using namespace std;
// int main()
// {
//     char str = 'My name is rahul';
//     char ch = 'r';
//     // cout<<"Enter the string and character "<<endl;
//     // cin>>str>>ch;
//     // cout<<str<<ch;
//     int i, count = 0;
//     for(i = 0; i < 100; i++){
//         if(str[i] == ch){
//             count++;
//         }
//     }
    
//     cout<<"Total number of count in string "<<str<<" is "<<endl;
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int i, j, k;
//     for(i = 0; i<=5; i++){
//         for(k = 0; k < 5-i; k++){
//             cout<<"  ";
//         }
//         for(j = 0; j <= i; j++){
//             cout<<"* ";
//         }
//         for(int k = 0; k<=i-1; k++){
//             cout<<"* ";
//         }
//         cout<<endl;
//     }
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int i, j, k;
//     for(i = 0; i<=5; i++){
//         for(k = 0; k < i; k++){
//             cout<<"  ";
//         }
//         for(j = 0; j <= 5-i; j++){
//             cout<<"* ";
//         }
//         for(int k = 0; k<=4-i; k++){
//             cout<<"* ";
//         }
//         cout<<endl;
//     }
//     return 0;
// }


// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int i, j, k;
//     for(i = 0; i<=5; i++){
//         for(k = 0; k < i; k++){
//             cout<<"*  ";
//         }
//         for(j = 0; j <= 5-i; j++){
//             cout<<"  ";
//         }
//         cout<<endl;
//     }
//     for(i = 0; i<=5; i++){
//         for(k = 0; k < 4-i; k++){
//             cout<<"*  ";
//         }
//         for(j = 0; j <= i; j++){
//             cout<<"  ";
//         }
//         cout<<endl;
//     }
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     string str;
//     char ch;
//     int count= 0;
//     cout<<"Enter the string: "<<endl;
//     getline(cin, str);
//     cout<<"Enter the character u wanna search: "<<endl;
//     cin>>ch;
//     for(int i = 0; i <= str.length(); i++){
//         if(str[i] == ch){
//             count++;
//         }
//     }
//     cout<<ch<<" is found "<<count<<" times"<<endl;
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     string str;
//     cout<<"Enter the string: "<<endl;
//     getline(cin, str);
//     cout<<str<<endl;
//     for(int i = str.length(); i >= 0; i--){
//         cout<<str[i];
//     }
//     return 0;
// }
#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    for(int i = 1; i <= 5; i++){
        int k = 1;
        for(int j = 1; j<=5; j++){
            if(j <= i){
                cout<<k<<" ";
                k = k*(i-j)/j;
            }
            else {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

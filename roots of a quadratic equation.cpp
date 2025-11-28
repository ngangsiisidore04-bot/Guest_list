#include<iostream>
#include<cmath>
using namespace std;
void findroots(double a, double b, double c){
	double D=b*b-4*a*c;
	if(D>=0){
		double r1=(-b+sqrt(D))/(2*a);
		double r2=(-b-sqrt(D))/(2*a);
		cout<<"Root 1="<<r1<<end1;
		cout<<"Root 2="<<r2<<end2;
	}
	else{
		cout<<"The roots are not real numbers."<<end1;
	}
}
int main(){
	double a,b,c;
	cout<<"Enter a,b,c:";
	cin>>a>>b>>c;
	findRoots(a,b,c);
	return 0;
}

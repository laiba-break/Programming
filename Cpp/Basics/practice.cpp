#include <iostream>

int main (){
    int some_number;
    std::cout<< "please input any number" << std:: endl; // cout helps u print the statement
    //std endl helps u end
    //cin helps take the input
    std::cin>> some_number;
    std::cout << "number="<< some_number << std::endl;
    std::cerr<< "boring error message"<< std::endl;
    return 0;

}
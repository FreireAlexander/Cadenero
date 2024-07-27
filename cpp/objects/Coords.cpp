#include <iostream>

#include "../headers/Coords.h"

using namespace std;

Coord::Coord(float _x, float _y){
    x = _x;
    y = _y;
}

void Coord::print(){
    cout << "( " << x << " , " << y<< " )" << endl;
}
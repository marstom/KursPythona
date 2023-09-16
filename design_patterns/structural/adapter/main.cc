
#include <iostream>
using namespace std;

class Klasa {
public:
    ~Klasa() {
        cout<< "Klasa destruct" << endl;
    }

    static Klasa *create(){
        return new Klasa();
    }


    void show(){
        cout << num << endl;
    }

private:
    int num;
    Klasa() {
        cout<< "Klasa create" << endl;
        this->num = 2;
    }
};

int main() {

    Klasa *cc = Klasa::create();
    cc->show();
    cout << "TOmek" << endl;
    
    delete cc;

    return 0;
}
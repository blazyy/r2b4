// An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
// Page 67

#include <iostream>
#include <vector>
using namespace std;

// Solution
// I'm just going to use a Python list instead of a LinkedList.
// Dequeue is going to be O(n) in that case, which is alright I guess. If a LinkedList was used, dequeue and enqueue could be both implemented in O(1)
class Shelter{
private:
    vector <int> cats;
    vector <int> dogs;
    int counter = 0; // To keep track of order
public:
    void enqueue(char animal){
        if (animal == 'd') dogs.push_back(counter++);
        else if (animal == 'c') cats.push_back(counter++);
        else {
            cout << "Invalid animal!" << endl;
            return;
        }
    }
    int dequeueAny(){
        int to_return;
        if(cats.size() == 0){
            if(dogs.size() == 0) return -1;
            else{
                to_return = dogs.front();
                dogs.erase(dogs.begin());
            }
        }
        else{
            if(dogs.size() == 0){
                to_return = cats.front();
                cats.erase(cats.begin());
            }
            else{
                if(cats.front() < dogs.front()){
                    to_return = cats.front();
                    cats.erase(cats.begin());
                }
                to_return = dogs.front();
                dogs.erase(dogs.begin());
            }
        }
        return to_return;
    }
    int dequeueDog(){
        if(dogs.size() == 0) return -1;
        int to_return = dogs.front();
        dogs.erase(dogs.begin());
        return to_return;
    }
    int dequeueCat(){
        if(cats.size() == 0) return -1;
        int to_return = cats.front();
        cats.erase(cats.begin());
        return to_return;
    }
    void print(){
        cout << "cats: ";
        for(auto cat : cats) cout << cat << " ";
        cout << endl;
        cout << "dogs: ";
        for(auto dog : dogs) cout << dog << " ";
        cout << endl;
    }
};

int main(void){
    Shelter shelter;
    shelter.enqueue('c');
    shelter.enqueue('d');
    shelter.enqueue('d');
    shelter.enqueue('c');
    shelter.enqueue('d');
    shelter.enqueue('c');
    shelter.enqueue('c');
    shelter.enqueue('c');

    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueDog() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueAny() << endl;
    shelter.print();
    cout << "dequeued " << shelter.dequeueCat() << endl;
    shelter.print();
}

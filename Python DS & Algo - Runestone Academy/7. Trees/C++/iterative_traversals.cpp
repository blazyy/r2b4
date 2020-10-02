#include<iostream>
#include<stack>
using namespace std;

class BinaryTree{
private:
    char root;
    BinaryTree * left = NULL;
    BinaryTree * right = NULL;
public:
    BinaryTree(char data){
        root = data;
    }
    void insert_left(char data){
        left = new BinaryTree(data);
    }
    void insert_right(char data){
        right = new BinaryTree(data);
    }
    BinaryTree * get_left(){
        return left;
    }
    BinaryTree * get_right(){
        return right;
    }
    char get_root(){
        return root;
    }
    void inorder(){
        if(left)
            (*left).inorder();
        cout << root << " ";
        if(right)
            (*right).inorder();
    }
    void preorder(){
        cout << root << " ";
        if(left)
            (*left).preorder();
        if(right)
            (*right).preorder();
    }
    void postorder(){
        if(left)
            (*left).postorder();
        if(right)
            (*right).postorder();
        cout << root << " ";
    }
};

void inorder_iterative(BinaryTree * root_node){
    stack <BinaryTree *> Stack;
    BinaryTree * current = root_node;
    while(true){
        if(current){
            Stack.push(current);
            current = (*current).get_left();
        }
        else if(Stack.size() > 0){
            current = Stack.top();
            Stack.pop();
            cout << (*current).get_root() << " ";
            current = (*current).get_right();
        }
        else break;
    }
}

void preorder_iterative(BinaryTree * root_node){
    stack <BinaryTree *> Stack;
    BinaryTree * current = root_node;
    while(true){
        if(current){
            cout << (*current).get_root() << " ";
            Stack.push(current);
            current = (*current).get_left();
        }
        else if(Stack.size() > 0){
            current = Stack.top();
            Stack.pop();
            current = (*current).get_right();
        }
        else break;
    }
}

void postorder_iterative(BinaryTree * root_node){
    stack <BinaryTree *> Stack;
    BinaryTree * current = root_node;
    while(true){
        while(current){
            if((*current).get_right())
                Stack.push((*current).get_right());
            Stack.push(current);
            current = (*current).get_left();
        }

        current = Stack.top();
        Stack.pop();

        if(Stack.size() > 0 && (*current).get_right() == Stack.top()){
            Stack.pop();
            Stack.push(current);
            current = (*current).get_right();
        }

        else{
            cout << (*current).get_root() << " ";
            current = NULL;
        }

        if(Stack.size() == 0) break;
    }
}

int main(void){
    BinaryTree * tree = new BinaryTree('1');
    (*tree).insert_left('2');
    (*tree).insert_right('3');
    (*tree).get_left() -> insert_left('4');
    (*tree).get_left() -> insert_right('5');
    (*tree).get_right() -> insert_left('6');
    (*tree).get_right() -> insert_right('7');

    // (*tree).inorder();
    // cout << endl;
    // inorder_iterative(tree);

    // (*tree).preorder();
    // cout << endl;
    // preorder_iterative(tree);

    (*tree).postorder();
    cout << endl;
    postorder_iterative(tree);
}

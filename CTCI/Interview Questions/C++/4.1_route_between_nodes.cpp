// Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <stack>
#include <queue>
using namespace std;

struct Node{
    char val;
    bool visited = false;
    Node(char value){
        val = value;
    }
};

class Graph{
private:
    unordered_map <char, vector<Node>> graph;
    Node * root = NULL;
public:
    Graph(vector <vector <Node>> connections){
        add_connections(connections);
    }
    void add_connections(vector <vector <Node>> connections){
        for(auto vertex_pair : connections){
            graph[vertex_pair[0].val].push_back(vertex_pair[1]); // Connection from node1 to node2
            graph[vertex_pair[1].val].push_back(vertex_pair[0]); // Connection from node2 to node1
        }
    }
    void print(){
        for(auto const& pair : graph){ // For each pair of vertex and it's adjacent vertices
            cout << pair.first << ": ";
            for(auto adjacent : pair.second)
                cout << adjacent.val << " ";
            cout << endl;
        }
    }
    // Unlike Python, C++ does not have an equality operator for two different objects. We have to implement that on our own.
    // So, being the levelheaded programmer I am, I go ahead and decide that this program will only work for nodes with unique values.
    bool is_connected(Node node1, Node node2){
        for(auto adjacent : graph[node1.val])
            if(adjacent.val == node2.val)
                return true;
        return false;
    }
    Node * get_nearest_unvisited_neighbour(Node node){
        if(graph[node.val].size() == 0) return NULL;
        Node * nearest = NULL;
        for(auto neighbour : graph[node.val])
            if(!neighbour.visited && (nearest == NULL || neighbour.val < (*nearest).val))
                nearest = &neighbour;
        return nearest;
    }
    vector <Node> get_all_unvisited_neighbours(Node node){
        vector <Node> unvisited_neighbours;
        for(auto neighbour : graph[node.val])
            if(!neighbour.visited)
                unvisited_neighbours.push_back(neighbour);
        return unvisited_neighbours;
    }
};

void unvisit_nodes(vector <Node> nodes){
    for(auto node : nodes)
        node.visited = false;
}

bool is_connected_bfs(Graph graph, Node node1, Node node2){
    Node * neighbour;
    queue <Node> node_queue;
    node1.visited = true;
    node_queue.push(node1);
    while(!node_queue.empty()){
        Node current = node_queue.front();
        node_queue.pop();
        int i = 0;
        for(auto neighbour : graph.get_all_unvisited_neighbours(current)){
            cout << "comparing " << neighbour.val << " and " << node2.val << endl;
            if(neighbour.val == node2.val)
                return true;
            neighbour.visited = true;
            node_queue.push(neighbour);
        }
    }
    return false;
}

bool is_connected_dfs(Graph graph, Node node1, Node node2){
    if(node1.val == node2.val)
        return true;
    Node * neighbour;
    stack <Node> node_stack;
    node_stack.push(node1);
    node1.visited = true;
    while(node_stack.size() > 0){
        cout << "stack size: " << node_stack.size() << endl;
        cout << "stack top val: " << node_stack.top().val << endl;
        Node current = node_stack.top();
        cout << "current: " << current.val << endl;
        neighbour = graph.get_nearest_unvisited_neighbour(current);
        cout << "neighbour: " << neighbour -> val << endl;
        if(neighbour == NULL)
            node_stack.pop();
        else{
            node_stack.push((*neighbour));
            cout << "top after neighhbour push: " << node_stack.top().val << endl;
            (*neighbour).visited = true;
            if((*neighbour).val == node2.val)
                return true;
        }
    }
    return false;
}

int main(void){
    Node node_a = Node('A'); Node node_b = Node('B'); Node node_c = Node('C'); Node node_d = Node('D'); Node node_e = Node('E'); Node node_f = Node('F');
    Node unconnected_node = Node('X');
    vector <vector <Node>> connections = {{node_a, node_b}, {node_b, node_c}, {node_b, node_d}, {node_c, node_d}, {node_e, node_f}, {node_f, node_c}};
    Graph graph = Graph(connections);
    graph.print();
    // cout << "Node A and Node B connected? " << graph.is_connected(node_a, node_b) << endl;
    // cout << "Node A and Node F connected? " << graph.is_connected(node_a, node_f) << endl;
    cout << endl;
    cout << "Node A and Node B connected? " << is_connected_bfs(graph, node_a, node_b) << endl;
    unvisit_nodes({node_a, node_b, node_c, node_d, node_e, node_f});
    cout << "Node A and Node B connected? " << is_connected_bfs(graph, node_a, node_f) << endl;
    cout << "Node A and Node B connected? " << is_connected_bfs(graph, node_a, unconnected_node) << endl;
}

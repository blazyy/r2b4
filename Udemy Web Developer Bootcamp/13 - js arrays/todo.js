window.setTimeout(function() {
    var todos = []
    while(true){
        let option = prompt("What would you like to do?");
        if(option === "new"){
            let new_todo = prompt("Enter the new todo");
            todos.push(new_todo);
            console.log("'" + new_todo + "'" + " added to the list.");
        }
        else if(option === "list"){
            if(todos.length === 0)
                alert("There are no todos available!");
            else{
                console.log('**********');
                for(let i = 0; i < todos.length; i++)
                    console.log(i + 1 + ": " + todos[i]);
                console.log('**********');
            }
        }
        else if(option === "delete"){
            if(todos.length === 0)
                alert("There are no todos to delete!");
            else{
                let index = Number(prompt("Enter the number of the todo to delete: "));
                if(index < 1 || index > todos.length){
                    alert("Invalid number!");
                    continue;
                }
                todos.splice(index - 1, 1);
                console.log("Todo " + index + " removed.");
            }
        }
        else if(option === "quit"){
            console.log("You have quit the app. Have a good day!");
            break;
        }
        else
            alert("That isn't a valid choice. Try again.");
    }
}, 500);

// Check off specific todos by clicking
$("ul").on("click", "li", function() {
    $(this).toggleClass("grayed");
});

// Click on 'X' to delete todo.
$("ul").on("click", "span", function(event) {
    $(this).parent().fadeOut(500, function() {
        $(this).remove();
    });
    event.stopPropagation(); //stops custom function from getting applied on parent elements
});

$("input").on("keypress", function(event) {
    if (event.which === 13) {
        let new_todo = $(this).val();
        $(this).val("");
        $("ul").append("<li><span><i class='fa fa-trash'></i></span> " + new_todo + "</li>");
    }
});

$(".fa-plus").on("click", function() {
    $("input").fadeToggle();
});

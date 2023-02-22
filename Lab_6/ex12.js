let x = 5;
let y = 2;

function printer(callback, p1, p2){
    let result = callback(p1, p2);
    console.log(result);
}

printer(function(p1, p2){
    return p1 + p2;
}, x, y);

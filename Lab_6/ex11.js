function add(p1, p2) {
    return p1 + p2
}
function printer(){
    let result = callback(p1, p2)
    console.log(result)
}
let x = 5;
let y = 2;
printer(add, x, y);
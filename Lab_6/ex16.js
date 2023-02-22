const person = {
    name: "Zara",
    age: 19,
    address: "Swords",
    sayHello: function() {
        console.log("Hello, my name is " + this.name);
    }
};

person.sayHello()
//*** Kelvin Weather ***

// adding Kelvin.
const kelvin = 293;
// changing K to C.
let celsius = kelvin - 273;
// changing C to F.
let fahrenheit = (celsius * (9 / 5)) + 32;
// rounding it down.
fahrenheit = Math.floor(fahrenheit);
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);
let newton = celsius * (33 / 100);
newton = Math.floor(newton);
console.log(`The temperature is ${newton} degrees Newton.`);
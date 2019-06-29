// *** Magic Eight Ball ***

let userName = 'Einat';
userName ? console.log(`Hello, ${userName}!`) : console.log('Hello');

let userQuestion = 'Should I stay or should I go?';
console.log(`${userName}'s question: ${userQuestion}`);

const randomNumber = Math.floor(Math.random() * 8);

let eightBall = '';

switch (randomNumber) {
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidely so';
    break;
  case 2:
    eightBall = 'OK';
    break;
  case 3:
    eightBall = 'Go away';
    break;
  case 4:
    eightBall = 'Noooooo';
    break;
  case 5:
    eightBall = 'Yesssss';
    break;
  case 6:
    eightBall = 'No idea';
    break;
  case 7:
    eightBall = 'You choose';
    break;
  case 8:
    eightBall = 'Whatttt';
    break;
}
console.log(`Number ${randomNumber} says ${eightBall}.`);


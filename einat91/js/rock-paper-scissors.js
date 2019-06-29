// *** Rock, Paper, or Scissors ***

const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
    return userInput;
  } else {
    console.log('error!');
  }
}
console.log(getUserChoice('scisSORS'));

const getComputerChoice = (Math.floor(Math.random() * 3)) => {
  switch (getComputerChoice) {
    case 0:
      return 'rock';
      break;
    case 1:
      return 'paper';
      break;
    case 2:
      return 'scissors';
      break;
  }
}
  

  
}
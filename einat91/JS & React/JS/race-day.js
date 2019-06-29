//*** Race Day ***

let raceNumber = Math.floor(Math.random() * 1000);
const early = false;
const age = 18;

if ((age > 18) && (early)) {
  raceNumber += 1000;
  console.log(`Your race number is ${raceNumber}. Your race will start at 9:30am.`);
} else if ((age > 18) && (!early)) {
  console.log(`Your race number is ${raceNumber}. Your race will start at 11:00am.`);
} else if (age < 18) {
  console.log(`Your race number is ${raceNumber}. Your race will start at 12:30pm.`);
} else {
  console.log('Please go to the registration desk');
}


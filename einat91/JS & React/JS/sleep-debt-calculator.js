// *** Sleep Debt Calculator ***

const getSleepHours = day => {
  //day = day.toLowerCase();
  switch (day) {
    case ('Monday'):
      return 8;
      break;
    case ('Tuesday'):
      return 8;
      break;
    case ('Wednesday'):
      return 8;
      break;
    case ('Thursday'):
      return 8;
      break;
    case ('Friday'):
      return 12;
      break;
    case ('Saturday'):
      return 12;
    case ('Sunday'):
      return 8;
      break;
  }
};

console.log(getSleepHours('Monday'));

const getActualSleepHours = () =>
  getSleepHours('Monday') +
  getSleepHours('Tuesday') +
  getSleepHours('Wednesday') +
  getSleepHours('Thursday') +
  getSleepHours('Friday') +
  getSleepHours('Saturday') +
  getSleepHours('Sunday');


console.log(getSleepHours());

const getIdealSleepHours = () => {
  const idealHours = 8;
  return idealHours * 7;

};

console.log(getIdealSleepHours());

const calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();
  if (getActualSleepHours === getIdealSleepHours) {
    console.log('Perfect amount of sleep');
  } else if (getActualSleepHours > getIdealSleepHours) {
    console.log('You sleep too much');
  } else {
    console.log('You should get some rest');
  }
};

console.log(calculateSleepDebt());


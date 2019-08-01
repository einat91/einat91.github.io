//Tip Calculator

const tipCalculator = (quality, total) => {
    switch (quality) {
        case 'bad':
            return total * .05;
        case 'ok':
            return total * .15;
        case 'good':
            return total * .20;
        case 'excellent':
            return total * .30;
        default:
            return total * .18;

    }
}

console.log(tipCalculator('good', 100))

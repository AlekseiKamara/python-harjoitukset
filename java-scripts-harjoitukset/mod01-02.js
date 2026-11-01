"use strict";

console.log("I'm printing to console!");

"use strict";

const name = prompt("Kirjoita nimesi.");

document.querySelector("#greeting").innerHTML =
  "Hei, " + name + "!";

"use strict";

const number1 = parseInt(prompt("Anna ensimmäinen kokonaisluku."));
const number2 = parseInt(prompt("Anna toinen kokonaisluku."));
const number3 = parseInt(prompt("Anna kolmas kokonaisluku."));

const sum = number1 + number2 + number3;
const product = number1 * number2 * number3;
const average = sum / 3;

document.querySelector("#result").innerHTML =
  "Summa: " + sum + "<br>" +
  "Tulo: " + product + "<br>" +
  "Keskiarvo: " + average;

  
"use strict";

const year = parseInt(prompt("Anna vuosiluku."));

if (year % 400 === 0) {
    document.querySelector("#year").innerHTML =
        year + " on karkausvuosi.";
} else if (year % 100 === 0) {
    document.querySelector("#year").innerHTML =
        year + " ei ole karkausvuosi.";
} else if (year % 4 === 0) {
    document.querySelector("#year").innerHTML =
        year + " on karkausvuosi.";
} else {
    document.querySelector("#year").innerHTML =
        year + " ei ole karkausvuosi.";
}

"use strict";

const answer = confirm("Lasketaanko neliöjuuri?");

if (answer === true) {
    const number = prompt("Anna luku.");

    if (number < 0) {
        document.querySelector("#math").innerHTML =
            "Negatiivisen luvun neliöjuurta ei ole määritelty.";
    } else {
        document.querySelector("#math").innerHTML =
            "Neliöjuuri on " + Math.sqrt(number);
    }
} else {
    document.querySelector("#math").innerHTML =
        "Neliöjuurta ei lasketa.";
}
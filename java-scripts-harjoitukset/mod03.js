//Tehtävä 1
"use strict";
let luvut = [];

for (let i = 0; i < 5; i++) {
    let luku = Number(prompt("Anna luku:"));
    luvut.push(luku);
}

for (let i = 4; i >= 0; i--) {
    console.log(luvut[i]);
}

//Tehtävä 4
"use strict";
let luvut2 = [];
let luku = Number(prompt("Anna luku (nolla lopettaa):"));

while (luku !== 0) {
    luvut2.push(luku);
    luku = Number(prompt("Anna luku (nolla lopettaa):"));
}

luvut2.sort(function(a, b) {
    return b - a;
});

for (let i = 0; i < luvut2.length; i++) {
    console.log(luvut2[i]);
}

//Tehtävä 5
"use strict";
let luvut3 = [];
let luku1 = Number(prompt("Anna luku:"));

while (!luvut3.includes(luku1)) {
    luvut3.push(luku1);
    luku1 = Number(prompt("Anna luku:"));
}

alert("Luku on jo annettu!");

luvut3.sort(function(a, b) {
    return a - b;
});

for (let i = 0; i < luvut3.length; i++) {
    console.log(luvut3[i]);
}

//Tehtävä 2
"use strict";

let nimet = [];
let maara = Number(prompt("Montako osallistujaa?"));

for (let i = 0; i < maara; i++) {
    let nimi = prompt("Anna nimi:");
    nimet.push(nimi);
}

nimet.sort();

let tulos = "<ol>";

for (let i = 0; i < nimet.length; i++) {
    tulos += "<li>" + nimet[i] + "</li>";
}

tulos += "</ol>";

document.querySelector("#human").innerHTML = tulos;

//Tehtävä 3
"use strict";
let koirat = [];

for (let i = 0; i < 6; i++) {
    let nimi = prompt("Anna koiran nimi:");
    koirat.push(nimi);
}

koirat.sort();
koirat.reverse();

let vastaus = "<ul>";

for (let i = 0; i < koirat.length; i++) {
    vastaus += "<li>" + koirat[i] + "</li>";
}

vastaus += "</ul>";

document.querySelector("#dog").innerHTML = vastaus;
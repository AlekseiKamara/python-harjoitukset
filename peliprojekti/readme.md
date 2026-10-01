**Vankilanpakopeli**

*Pelin idea*

Peli alkaa siitä, että olet vankilassa vankisellissa. Ideana on paeta vankilasta löytäneiden esineiden kautta. 
Erilaiset esineet voivat auttaa sinua pakeneeman.

*Peli tavoite* 

Pelaajan tavoiteena on löytää tarvittavat esineet ja päästä niiden avulla vankilan pihalla. Pelissä voi olla useampi tapa päästä ulos esimerkiksi avaimen tai ruuvinmeisselin avulla.

Pelissä on erilaisia reittiä joita voi edetä ensimmäinen eli helpoin on vankiselli, käytävä ja piha, siihen tarvitaan avaimen, joka voi saada vanisellista.

Seuraava vankiselli, käytävä, varasto, valvomo ja piha. Siihen tarvitaan ruuvimeisseliä, jonka voi saada varastossa.

*Toimintaperiaate*

Peli toimii komentorivillä terminaalin kautta. Pelaaja vlitsee toimintoja kirjoittamalla komentoja.

Pelin alussa pelaajalta kysytään nimi ja ikä. Sen jälkeen peli alkaa vankisellistä. Pelaaja voi liikkua huoneesta toiseen, tutkia huoneita ja ottaa niisä olevia esineitä.

Pelin etenemiseen vaikuttaa pelaajan inventaario. Esimerkiksi avainta tarvitaan tietyn oven avaamiseen ja ruuvimeisseliä voidaan käyttää toisen oven avaamisen.

Ruusimeisselin kunto arvotaan satunnaisesti pelin alussa.

Peli voidaan tallentaa save.json-tiedostoon. Tallennukseen jäävär pelaajan nimi, ikä, sijainti ja inventaario esineet. Tallenettu peli voidaan myöhemmin ladata.

*Toiminnallisuudet*

Peli on kehitetty Python-ohjelmoinilla. Pelaaja kirjoittaa konsoliin haluamansa komennon, jonka perusteella peli suoritetaan.

Pelissä sinä voit, muun muassa katsoa huonetta, liikkua huoneesta toiseen, ottaa huoneista esineitä, tarkastella inventaariota, tallentaa pelin, ladata aikaisemmin tallennetun pelin ja lopettaa pelin.

Pelin huoneita ovat vankiselli, käytävä, varasto, valvomo ja piha. Eri huoneissa on erilaisia esineitä, joita pelaaja voi käyttää pelin aikana.

Esineitä ovat avain, vesipullo ja ruuvimeisseli. Ruuvimeisselin kunto arvotaan pelin alussa satunnaisesti.

*Kestävä kehitys*

Kestävän kehityksen näkökulmasta on huomioitu tekemällä peli tietokoneella digitaalisesti. Pelin tekemiseen ja pelaamisen ei käytetty mitään paperipohjaista tai fyysistä materiaaleja.

Peliä voi pelata myös kevyellä teitokoneella eli raskas grafikka ei ole vaativin elementti. Peliä voi myös jakaa muille sähköisesti eikä fyysisesti. Pelissä on myös vesipullo esineenä, jonka voi saada käytävältä. Jos ottaa sen inventaarion se jää sinulla kuin pääset pois vankilasta eli säästä vettä.

Tekijä:
Aleksei Kämärä
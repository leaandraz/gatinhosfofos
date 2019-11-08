

// let animes = ['Death Note', 'Boku no Hero', 'Dragol Ball', 'Cavaleiros do Zodiaco', 'Naruto', 'Super Onze', 'Nazo no Konojo'];
// let i = 0;


// ======while========

// while (i < animes.length){
//     console.log(animes[i]);
//     i++
// }

// ======while========


// ======FOR========

// for (let e = 0; e < animes.length; e++){
//     console.log(animes[e]);
// }

// ======FOR========


// let usuario = "leaandraz";
// let senha = "1234";
// let tentativas = 0;

// while (tentativas <=2 ){
//     let promptUsuario = prompt ("Digite seu usuário");
//     let promptSenha = prompt ("Digite sua senha");
// if (promptUsuario == usuario && promptSenha == senha){
//     alert ("Você logou");
//     tentativas = 3;
// }else {
//     alert ("Ops, algo está errado!"); 
//     tentativas++;
//     if (tentativas == 2) {
//         alert ("não rolou, bloqueado!");
//     }
// }
// }

// Função como fazer

// function parOuImpar (n){
//     if (n%2 == 0){
//         alert ("é par!");
//     }else {
//         alert ("é ímpar");
//     }
// }

// Função como fazer


// Construir uma escada de 5 degraus no console 
// Dicas: tem que usar laço
// "FOR" normal é mais fácil de usar nesse caso
// usar e pesquisar +=
// o que acontece se eu definir uma variavel com String vazia? Exemplo: VAR X = ""

// #
// ##
// ###
// ####
// #####

// explicação com FOR e spring "" vazia

// let material = prompt ("Qual material você quer?");
// let degraus = Number(prompt("Quantos degraus você quer?"));
// let escada = "";
// for (let i = 0; i < degraus; i++){
//     escada += material;
//     console.log(escada)
// }

////////////

// explicação com Array 

let material = prompt("Digite o material");
let quat_degraus = Number(prompt("Digite quantos degraus quer"));
let array_degraus = [];
let valor_indice = "";

for (let i = 0; i < quat_degraus; i++){
    valor_indice += material;
    array_degraus.push (valor_indice);
}

for (let i = 0; i < quat_degraus; i++){
    console.log(array_degraus[i])
}

/////////////////


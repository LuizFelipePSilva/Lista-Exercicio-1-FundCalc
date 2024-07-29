
// Questão 1
// Função para verificar se um número é primo
function ePrimo(num) {
  if (num <= 1) return false;
  if (num <= 3) return true;
  if (num % 2 === 0 || num % 3 === 0) return false;
  for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
  }
  return true;
}

// Função para encontrar a soma dos n primeiros números primos
function somaPrimos(n) {
  let soma = 0;
  let contagem = 0;
  let num = 2;
  while (count < n) {
      if (ePrimo(num)) {
          soma += num;
          contagem++;
      }
      num++;
  }
  return soma;
}

// Exemplo de uso
console.log(somaPrimos(10)); // Soma dos 10 primeiros números primos


//Questão 2
function numerosRandomicos(a, b) {
  let numbers = [];
  for (let i = 0; i < 100; i++) {
      let num = Math.random() * (b - a) + a;
      numbers.push(num);
  }
  return numbers;
}

// Exemplo de uso
console.log(numerosRandomicos(1, 100));

//Questão 3
// Função para calcular o somatório de k^3 de 1 a n
function somaDosCubos(n) {
  let soma = 0;
  for (let k = 1; k <= n; k++) {
      soma += Math.pow(k, 3);
  }
  return soma;
}

// Função para calcular a fórmula do somatório de k^3
function formulaSomaDosCubos(n) {
  return Math.pow((n * (n + 1)) / 2, 3);
}

// Exemplo de uso
let n = 5;
console.log(somaDosCubos(n)); // Calculado pelo código
console.log(formulaSomaDosCubos(n)); // Calculado pela fórmula

const plotly = require('plotly')('username', 'apiKey'); // Substitua com suas credenciais de Plotly
const linspace = require('linspace');

function G(x) {
    if (x < 0) {
        return -x - (x - 3) - (2 * x - 7) - (x - 9);
    } else if (x >= 0 && x < 3) {
        return x - (x - 3) - (2 * x - 7) - (x - 9);
    } else if (x >= 3 && x < 3.5) {
        return x + (x - 3) - (2 * x - 7) - (x - 9);
    } else if (x >= 3.5 && x < 9) {
        return x + (x - 3) + (2 * x - 7) - (x - 9);
    } else {
        return x + (x - 3) + (2 * x - 7) + (x - 9);
    }
}

const xValues = linspace(-10, 10, 400);
const yValues = xValues.map(G);

const data = [
    {
        x: xValues,
        y: yValues,
        type: 'scatter'
    }
];

const layout = {
    title: 'Gráfico da Função G(x)',
    xaxis: { title: 'x' },
    yaxis: { title: 'G(x)' },
    width: 800,
    height: 600
};

plotly.plot(data, layout, function (err, msg) {
    if (err) {
        console.error(err);
    } else {
        console.log('Gráfico criado:', msg.url);
    }
});



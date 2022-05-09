var data = [1, 11, 12, 2, 3, 4];

function solution() {
  var sor = data.sort(function (a, b) {
    // 오름차순
    return a - b;
  });
  console.log(sor);
}

solution();

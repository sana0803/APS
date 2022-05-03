function solution(n) {
  var answer = [];
  // var txt = String(n).split("").reverse().join("");
  // console.log(txt, typeof txt);
  console.log(String(n).split("").reverse());
  console.log(
    (n + "")
      .split("")
      .reverse()
      .map((v) => parseInt(v))
  );
  return (n + "")
    .split("")
    .reverse()
    .map((v) => parseInt(v));
}

solution(12345);

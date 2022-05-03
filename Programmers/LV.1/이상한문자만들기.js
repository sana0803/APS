const s = "try hello world";
// 짝수번째는 대문자, 홀수번째는 소문자로 바꿔 리턴

function solution(s) {
  var answer = "";
  const word = s.split(" ");

  for (let i = 0; i < word.length; i++) {
    for (let j in word[i]) {
      answer =
        j % 2
          ? (answer += word[i][j].toLowerCase())
          : (answer += word[i][j].toUpperCase());
    }
    answer += " ";
  }
  console.log(answer);
  return answer.slice(0, -1);
}

solution(s);

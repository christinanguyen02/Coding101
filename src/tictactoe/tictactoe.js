var isPlayerXMoving = true;
var board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
];

var ScoreX = 0;
var ScoreO = 0;

document.addEventListener("click", ticTacToeClickHandler);

function ticTacToeClickHandler(event) {
  var targetElement = event.target;
  var parentElement = targetElement.parentElement;
  var row, column;

  if (targetElement.nodeName == "BUTTON") {
    row = parseInt(targetElement.dataset.row);
    column = parseInt(targetElement.dataset.column);

    board[row][column] = isPlayerXMoving ? 1 : -1;

    parentElement.innerHTML = isPlayerXMoving ? "x" : "o";
    parentElement.classList.add(isPlayerXMoving ? "piece-x" : "piece-o");

    if (gameOver()) {
      alert(
        "Game over. " +
          (isPlayerXMoving ? "Player X" : "Player O") +
          " has won."
      );
      if (isPlayerXMoving) {
        ScoreX = ScoreX + 1;
        localStorage.setItem("X", ScoreX);
        document.getElementById("scoreX").innerHTML =
          "Player X: " + localStorage.getItem("X");
      } else {
        ScoreO = ScoreO + 1;
        localStorage.setItem("O", ScoreO);
        document.getElementById("scoreO").innerHTML =
          "Player O: " + localStorage.getItem("O");
      }
    } else {
      isPlayerXMoving = !isPlayerXMoving;
    }
  }
}

function gameOver() {
  var sum;

  for (var i = 0; i < 3; i++) {
    sum = 0;

    for (var j = 0; j < 3; j++) {
      sum += board[i][j];
    }

    if (Math.abs(sum) == 3) {
      return true;
    }
  }

  for (var j = 0; j < 3; j++) {
    sum = 0;

    for (var i = 0; i < 3; i++) {
      sum += board[i][j];
    }

    if (Math.abs(sum) == 3) {
      return true;
    }
  }

  sum = 0;

  for (var i = 0; i < 3; i++) {
    sum += board[i][i];
  }

  if (Math.abs(sum) == 3) {
    return true;
  }

  sum = 0;

  for (var i = 0; i < 3; i++) {
    sum += board[i][2 - i];
  }

  if (Math.abs(sum) == 3) {
    return true;
  }

  return false;
}

// function clearBoard() {
//   location.reload();
// }

document.getElementById("replay").addEventListener("click", function () {
  for (let i = 1; i <= 9; i++) {
    document.getElementById(i.toString()).innerHTML = "";
    document.getElementById(i.toString()).classList.remove("x");
    document.getElementById(i.toString()).classList.remove("o");
    gameEnded = false;
  }
});

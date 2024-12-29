const board = [
  '·····',
  '·····',
  '·····',
  '·oo@·',
  '·····'
]

// console.log(moveTrain(board, 'U'))
// // El tren se mueve hacia arriba

// console.log(moveTrain(board, 'R'))
// // ➞ 'crash'
// // El tren se mueve hacia la derecha y la cabeza se choca con muro



function moveTrain(board, mov) {

  
  board.forEach((e, i) => {
    board[i] = e.split("")
  })
  
  let chars = ["@", "o", "o"]
  let row, col
  let aux = 0
  let head_found = false


  for (let i = 0; i < board.length; i++) {
    
    for (let j = 0; j < board[0].length; j++) {
      if (mov == "U") {
        // HEAD -> TAIL -> MIDDLE
        if (board[i][j] == "@" && head_found == false){

          board[i-1][j] = "@"
          board[i][j] = "·"
          row = i
          col = j
          j=-1
          head_found = true
          aux++
        } else if ((board[i][j] == "o") && aux != (chars.length - 1) && head_found == true) {

          board[row][col] = board[i][j]
          board[i][j] = "·"
          row = i
          col = j
          j++
          aux++
        } else if (((board[i][j] == "o") && head_found == true && aux == (chars.length - 1) && board[i][j-1] == "o")){
          break
        }
        else if ((board[i][j] == "o") && aux == (chars.length - 1) && head_found == true) {

          board[row][col] = board[i][j]
          board[i][j] = "·"
        }
      }

      if (mov == "R") {
        
        if (board[i][j] == "@" && head_found == false){

          if (j == board[0].length - 1){
            console.log("crash")
            return
          }

          board[i][j+1] = "@"
          board[i][j] = "·"
          row = i
          col = j
          head_found = true
          j = -1
          aux++
        } else if ((board[i][j] == "o") && aux != (chars.length - 1) && head_found == true) {


          board[row][col] = board[i][j]
          board[i][j] = "·"
          row = i
          col = j
          j++
          aux++
        } 
        
        else if ((board[i][j] == "o") && head_found == true && aux == (chars.length - 1) && board[i][j-1] == "o") {
          break

        } else if ((board[i][j] == "o") && head_found == true && aux == (chars.length - 1)) {
          
          board[row][col] = board[i][j]
          board[i][j] = "·"
        }
        
      }

    }
  }

  board.forEach((e, i) => {
    board[i] = e.join("")
  })
}

moveTrain(board, "R")

board.forEach(e=>{
  console.log(e)
})
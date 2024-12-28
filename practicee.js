function drawRace(indices, length) {
  let race = []
  
  for (let i = 0, indented = indices.length; indented > 0; indented--, i++) {
    race.push(" ".repeat(indented)+ "~".repeat(length) + ` /${i + 1}`)
  }
  
  let indent = indices.length
  indices.forEach((el, i) => {
    let temp = race[i].split("")

    if (el > 0) {
      temp[el+indent] = "r"
      race[i] = temp.join("")
    } else if (el < 0) {
      let index = race[i].length + el - 3
      temp[index] = "r"
      race[i] = temp.join("")
    }
    
    indent--
  })

  race.forEach(e=>{
    console.log(e)
  })
}

drawRace([3, 7, -2], 12)
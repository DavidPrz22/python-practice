function createXmasTree(height, ornament) {
  /* Code here */

  let base_height = 2

  let width = (height * 2) - 1
  let middle = Math.round(width / 2) - 1

  let str = ""
  let expand = 0 
  
  for (let i = 0; i < height; i++){

    for (let j = 0; j < width; j++){

      if (j >= middle - expand && j <= middle + expand ) {
        str = str.concat(ornament)
      } else {
        str = str.concat("_")
      }
    }

    expand++
    str = str.concat("\n")
  }

  for (let i = 0; i < base_height; i++){
    str = str.concat("_".repeat(middle) + "#"+ "_".repeat(middle) + "\n")
  }
  return str
}


console.log(createXmasTree(6, "~"))
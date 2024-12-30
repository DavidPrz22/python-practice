let record = {C:5, D:0}


const instructions = [
  'MOV 5 A', //
  'INC A 2', //
  'INC Z 2', //
  'JMP D 2', //
  'DEC Z 2', //
  'DEC A', //
]


instructions.forEach((element, index) => {

  let instruction = element.split(" ")
  process_instruction(instruction)

  if (instruction[0] == "JMP") {

    let x_value = instruction[1]
    let y_value = instruction[2]

    if (record[x_value] != 0) return

    for (let i = y_value - 1; i <= index; i++) {
      let repeated_instruction = instructions[i].split(" ")
      process_instruction(repeated_instruction)
    }

    record[x_value] += 1
  }
})

function process_instruction(instruction) {
  if (instruction[0] == "MOV") {

    let x_value = instruction[1]
    let y_record = instruction[2]

    if (instruction.length != 3) {
      console.log("incomplete instruction MOV x y")
      return
    }

    if (record[x_value]) {
      record[y_record] = record[x_value]
    } else {

      if (!isNaN(new Number(x_value))) {
        record[y_record] = Number(x_value)
      } else {
        record[y_record] = x_value
      }
    }

  }

  if (instruction[0] == "INC") {

    if (instruction.length < 2 || instruction.length > 3) {
      console.log("incomplete DEC x (or:y)")
      return
    }
    if (instruction.length == 2) {
      let x_value = instruction[1]

      if (record[x_value]) {
        record[x_value] += 1
      } else {
        record[x_value] = 0
      }
    } else if (instruction.length == 3) {

      let x_value = instruction[1]
      let y_value = instruction[2]

      if (record[x_value]) {

        if (!isNaN(new Number(y_value))) {
          record[x_value] += Number(y_value)
        } else {
          console.log(`Can not increase with non-digit characters on instruction ${index}`)
          return
        }
      } else {
        record[x_value] = Number(y_value)
      }
    }

  }

  if (instruction[0] == "DEC") {

    
    if (instruction.length < 2 || instruction.length > 3) {
      console.log("Instruction DEC X (or:Y)")
      return
    }

    if (instruction.length == 2) {

      let x_value = instruction[1]
      
      if (record[x_value]) {
        record[x_value]--
      } else {
        record[x_value] = 0
      }
    } else if (instruction.length == 3) {

      let x_value = instruction[1]
      let y_value = instruction[2]

      if (record[x_value]) {

        if (!isNaN(new Number(y_value))) {
          record[x_value] -= Number(y_value)
        } else {
          console.log(`Can not decrease with non-digit characters on instruction ${index}`)
          return
        }
      } else {
        record[x_value] = Number(y_value)
      }
    }

  }
}

console.log(record)
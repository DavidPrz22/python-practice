// Santa Claus tiene una agenda mágica 📇 donde guarda las direcciones de los niños para entregar los regalos. El problema: la información de la agenda está mezclada y malformateada. Las líneas contienen un número de teléfono mágico, el nombre de un niño y su dirección, pero todo está rodeado de caracteres extraños.

// Santa necesita tu ayuda para encontrar información específica de la agenda. Escribe una función que, dado el contenido de la agenda y un número de teléfono, devuelva el nombre del niño y su dirección.

// Ten en cuenta que en la agenda:

//     Los números de teléfono están formateados como +X-YYY-YYY-YYY (donde X es uno o dos dígitos, e Y es un dígito).
//     El nombre de cada niño está siempre entre < y >

// La idea es que escribas una funcióna que, pasándole el teléfono completo o una parte, devuelva el nombre y dirección del niño. Si no encuentra nada o hay más de un resultado, debes devolver null.

// const agenda = `+34-600-123-456 Calle Gran Via 12 <Juan Perez>
// Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
// <Carlos Ruiz> +1-800-555-0199 Fifth Ave New York`

// findInAgenda(agenda, '34-600-123-456')
// // { name: "Juan Perez", address: "Calle Gran Via 12" }

// findInAgenda(agenda, '600-987')
// // { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }

// findInAgenda(agenda, '111')
// // null
// // Explicación: No hay resultados

// findInAgenda(agenda, '1')
// // null
// // Explicación: Demasiados resultados


const agenda = `+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York`


function findInAgenda(agenda, number) {

  let formatted_agenda = []

  // MAGIC PHONE NUMBERS
  const phones_matches = [...agenda.matchAll(/\+(\d{1,2}-\d{3}-\d{3}-\d{3,4})/g)];
  const phones = phones_matches.map(match => match[1]);

  // KIDS NAMES
  const names_matches = [...agenda.matchAll(/<([a-zA-Z0-9 ]+)>/g)]
  const names = names_matches.map(match => match[1])
  //DIRECTIONS
  let temp = agenda.replace(/\+\d{1,2}-\d{3}-\d{3}-\d{3,4}/g,"\n")
                      .replace(/<[a-zA-Z0-9 ]+>/g,"\n")
                        .split('\n')

  let directions = []

  for (i of temp) {
    let dir = i.trim()
    if (dir) {
      directions.push(dir)
    }
  }

  phones.forEach((_, i)=> {
    formatted_agenda.push({[phones[i]]: {name: names[i], direction: directions[i]}})
  });
  
  for ( i of formatted_agenda) {
    let key = Object.keys(i)[0]
    
    if (key.includes(number)) {
      
      return i[key]
    }
  }

  return null
}

console.log(findInAgenda(agenda, '34-600-123-456'))
// { name: "Juan Perez", address: "Calle Gran Via 12" }

console.log(findInAgenda(agenda, '600-987'))
// { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }


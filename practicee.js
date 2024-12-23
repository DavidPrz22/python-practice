const gifts1 = [3, 1, 2, 3, 4, 2, 5]

const gifts2 = [6, 5, 5, 5, 5]

const gifts3 = []


// No hay regalos, la lista queda vacía
// No hay regalos, la lista queda vacía

function prepareGifts(gifts) {
    // Code here
    let gift_arr = []
  
    gifts.forEach(e =>{
      if (!gift_arr.includes(e)){
        gift_arr.push(e)
      }
    })
    return gift_arr.sort()
  }

const preparedGifts1 = prepareGifts(gifts1)
console.log(preparedGifts1) // [1, 2, 3, 4, 5]

const preparedGifts2 = prepareGifts(gifts2)
console.log(preparedGifts2) // [5, 6]

const preparedGifts3 = prepareGifts(gifts3)
console.log(preparedGifts3) // []
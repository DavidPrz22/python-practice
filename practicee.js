const inventory = [
  { name: 'book', quantity: 10, category: 'education' },
  { name: 'book', quantity: 5, category: 'education' },
  { name: 'paint', quantity: 3, category: 'art' }
]

function organizeInventory(inventory) {
  // Code here
  let object = {}

  inventory.forEach(e => {
    object[e["category"]] = {}
  })

  inventory.forEach(element => {
      const { name, quantity, category } = element;

      let temp = {}
      temp[name] = quantity

      if (object[category][name]) {

        object[category][name] += temp[name]

      } else {

        Object.assign(object[category], temp)
      }
    });

  return object
}

console.log(organizeInventory(inventory))
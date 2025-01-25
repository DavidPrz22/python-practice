// En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.

// Dos árboles binarios son espejos si:

//     Las raíces de ambos árboles tienen el mismo valor.
//     Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.

// Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):

// const tree = {
//   value: '⭐️',
//   left: {
//     value: '🎅'
//     // left: {...}
//     // right: { ... }
//   },
//   right: {
//     value: '🎁'
//     // left: { ... }
//     // right: { ...&nbsp;}
//   }
// }

// Santa necesita tu ayuda para verificar si los árboles están sincronizados para que la estrella pueda seguir brillando. Debes devolver un array donde la primera posición indica si los árboles están sincronizados y la segunda posición devuelve el valor de la raíz del primer árbol.

// const tree1 = {
//   value: '🎄',
//   left: { value: '⭐' },
//   right: { value: '🎅' }
// }

// const tree2 = {
//   value: '🎄',
//   left: { value: '🎅' }
//   right: { value: '⭐' },
// }

// isTreesSynchronized(tree1, tree2) // [true, '🎄']

// /*
//   tree1             tree2
//    🎄                🎄
//    / \               / \
//  ⭐   🎅          🎅   ⭐
// */

// const tree3 = {
//   value: '🎄',
//   left: { value: '🎅' },
//   right: { value: '🎁' }
// }

// isTreesSynchronized(tree1, tree3) // [false, '🎄']

// const tree4 = {
//   value: '🎄',
//   left: { value: '⭐' },
//   right: { value: '🎅' }
// }

// isTreesSynchronized(tree1, tree4) // [false, '🎄']

// isTreesSynchronized(
//   { value: '🎅' },
//   { value: '🧑‍🎄' }
// ) // [false, '🎅']


// const first_tree = {
//   value: '🎄',

//   left: {
//     value: '⭐'
//   },

//   right: {
//     value: '🎅'
//   }
// }

// const second_tree = {
//   value: '🎄',

//   left: {
//     value: '🎅'
//   },

//   right: {
//     value: '⭐'
//   }
// }


// function isTreesSynchronized(tree1, tree2) {

//   if (!tree1) {
//     return
//   }

//   let first = isTreesSynchronized(tree1.left, tree2.right) 
//   let second = isTreesSynchronized(tree1.right, tree2.left)

//   if (first && second) {

//     if (tree1.value == tree2.value)
//       return [true, tree1.value]

//     return [false, tree1.value]

//   } else {

//     if (tree1.left && tree2.left) {

//       return [false, tree1.value]

//     } else {

//       if (tree1.value == tree2.value) {
//         return true
//       }

//       return false

//     }
//   }
  
// }

// console.log(isTreesSynchronized(
//   { value: '🎅' },
//   { value: '🧑‍🎄' }
// ))


const binaryTree = {
  value: 10,
  left: {

      value: 5,
        left: {
          value: 3,
          left: null,
          right: null,
        },
        right: {
          value: 7,
          left: null,
          right: null,
        },
  },
  right: {

      value: 15,
        left: {
          value: 12,
          left: null,
          right: null,
        },

        right: {
            value: 18,
            left: null,
            right: null,
        },
  },
};

function allocate_branches(binaryTree, level, levels) {

  if (!binaryTree)
    return
  
  allocate_branches(binaryTree.left, level + 1, levels)
  allocate_branches(binaryTree.right, level + 1, levels)

  while (level >= levels.length) {
    levels.push([])
  }

  levels[level].push(binaryTree.value)

  if (level == 0)
    return levels
  
}

const levels = allocate_branches(binaryTree, 0, [])

levels.forEach(element => {
  console.log(element.join(" "))
});
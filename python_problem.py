"""
¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta 1, 2, 5, 10 de peso y se representan así:

    _
1: |_|
    _____
2: |_____|
    _____
5: |     |
   |_____|
     _________
10: |         |
    |_________|

// Representación en JavaScript:
const boxRepresentations = {
    1: [" _ ", "|_|"] ,
    2: [" ___ ", "|___|"],
    5: [" _____ ", "|     |", "|_____|"],
    10: [" _________ ", "|         |", "|_________|"]
}

Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas posibles y que, además, las apiles de menos peso (arriba) a más peso (abajo). Siempre alineadas a la izquierda.

Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.

distributeWeight(1)
// Devuelve:
//  _
// |_|

distributeWeight(2)
// Devuelve:
//  ___
// |___|

distributeWeight(3)
// Devuelve:
//  _
// |_|_
// |___|

distributeWeight(4)
// Devuelve:
//  ___
// |___|
// |___|

distributeWeight(5)
// Devuelve:
//  _____
// |     |
// |_____|

distributeWeight(6)
// Devuelve:
//  _
// |_|___
// |     |
// |_____|

Nota: ¡Ten cuidado con los espacios en blanco! No añadas espacios en blanco a la derecha de una caja si no son necesarios.

"""

boxRepresentations = {
    "1": [" _ ", "|_|"],
    "2": [" ___ ", "|___|"],
    "5": [" _____ ", "|     |", "|_____|"],
    "10": [" _________ ", "|         |", "|_________|"],
}


def main():

    for i in distribute_weight(18):
        print(i)


def distribute_weight(weight):

    # DETERMINE DISTRIBUTION OF BOXES TO PRINT FROM LIGHTEST TO HEAVIEST
    boxes_capacity = [10, 5, 2, 1]
    boxes_distributed = []
    remaining_weight = weight

    boxes_capacity_index = 0
    while True:

        box_factor = remaining_weight - boxes_capacity[boxes_capacity_index]

        if box_factor > 0:

            boxes_distributed.append(str(boxes_capacity[boxes_capacity_index]))
            remaining_weight -= boxes_capacity[boxes_capacity_index]
        elif box_factor < 0:

            boxes_capacity_index += 1

        elif box_factor == 0:
            boxes_distributed.append(str(boxes_capacity[boxes_capacity_index]))
            break

    boxes_distributed.reverse()

    # PRINT EVERY BOX TO LEFT-ORIENTED
    final_boxes = []

    for i, index in enumerate(boxes_distributed):

        if len(boxes_distributed) > 1:
            for j, box_part in enumerate(boxRepresentations[index]):

                if j == 0 and i == 0:

                    final_boxes.append(box_part)
                elif j == 0:

                    new_box_part_top = (
                        prev_box_bottom + box_part[len(prev_box_bottom) :]
                    )
                    final_boxes.append(new_box_part_top)

                elif j == len(boxRepresentations[index]) - 1:

                    if i == len(boxes_distributed) - 1:
                        final_boxes.append(box_part)
                    else:
                        prev_box_bottom = box_part
                else:
                    final_boxes.append(box_part)
        else:
            final_boxes = boxRepresentations[index]

    return final_boxes


if __name__ == "__main__":
    main()

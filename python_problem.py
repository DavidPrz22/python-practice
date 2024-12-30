"""
Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel a distribuir regalos dentro de un gran almacén. El robot se mueve en un plano 2D y partimos desde el origen (0, 0).

Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a estar justo donde empezó.

Las órdenes básicas del robot son:

    L: Mover hacia la izquierda
    R: Mover hacia la derecha
    U: Mover hacia arriba
    D: Mover hacia abajo

Pero también tiene ciertos modificadores para los movimientos:

    *: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
    !: El siguiente movimiento se invierte (ej: R!L se considera como RR)
    ?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R significa R)

Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento invertido y no el original. Por ejemplo, !U?U invierte el movimiento de U, por lo que contabiliza que se hizo el movimiento D pero no el U. Así !U?U se traduce como D?U y, por lo tanto, se haría el movimiento U final.

Debes devolver:

    true: si el robot vuelve a estar justo donde empezó
    [x, y]: si el robot no vuelve a estar justo donde empezó, devolver la posición donde se detuvo

"""



def main():
    print(isRobotBack('R'))      # [1, 0]
    print(isRobotBack('RL'))     # true
    print(isRobotBack('RLUD'))   # true
    print(isRobotBack('*RU'))    # [2, 1]
    print(isRobotBack('R*U'))    # [1, 2]
    print(isRobotBack('LLL!R'))  # [-4, 0]
    print(isRobotBack('R?R'))    # [1, 0]
    print(isRobotBack('U?D'))    # true
    print(isRobotBack('R!L'))    # [2, 0]
    print(isRobotBack('U!D'))    # [0, 2]
    print(isRobotBack('R?L'))    # true
    print(isRobotBack('U?U'))    # [0, 1]
    print(isRobotBack('*U?U'))   # [0, 2]
    print(isRobotBack('U?D?U'))  # true



def isRobotBack(instructions: str):

    origin = [0, 0]
    plane = [0, 0]
    movement = list(convert_instructions(instructions))

    for mov in movement:
        
        match mov:
            case "R":
                plane[0] += 1
            case "L":
                plane[0] -= 1
            case "U":
                plane[1] += 1
            case "D":
                plane[1] -= 1

    if plane == origin:
        return True
    else:
        return plane


def convert_instructions(instructions: list):
    converted = ""

    for index in range(len(instructions)):

        if instructions[index] == "*":
            converted += instructions[index + 1]

        elif instructions[index] == "!":
            match instructions[index + 1]:
                case "R":
                    converted += "L"
                case "L":
                    converted += "R"
                case "D":
                    converted += "U"
                case "U":
                    converted += "D"

        elif instructions[index - 1] == "!" or instructions[index - 1] == "?":
            pass
        
        elif instructions[index] == "?":
            if not instructions[index + 1] in converted[:]:
                converted += instructions[index + 1]
        else:
            converted += instructions[index]
    
    return converted

if __name__ == "__main__":
    main()

r = int(input())
x1 = r//100
x3 = r%10
x2 = r%100 // 10
match x1:
    case 1:
        print ('сто', end=' ')
    case 2:
        print ('двести', end=' ')
    case 3:
        print('триста', end=' ')
    case 4:
        print('четыреста', end=' ')
    case 5:
        print('пятьсот', end=' ')
    case 6:
        print('шестьсот', end=' ')
    case 7:
        print('семьсот', end=' ')
    case 8:
        print('восемьсот', end=' ')
    case 9:
        print('девятьсот', end=' ')
match x2:
    case 1:
        match x3:
            case 1:
                print('одиннадцать')
            case 2:
                print('двенадцать')
            case 3:
                print('тринадцать')
            case 4:
                print('четырнадцать')
            case 5:
                print('пятнадцать')
            case 6:
                print('шестнадцать')
            case 7:
                print('семнадцать')
            case 8:
                print('восемнадцать')
            case 9:
                print('девятнадцать')
    case 2:
        print ('двадцать', end=' ')
    case 3:
        print('тридцать', end=' ')
    case 4:
        print('сорок', end=' ')
    case 5:
        print('пятьдесят', end=' ')
    case 6:
        print('шестьдесят', end=' ')
    case 7:
        print('семьдесят', end=' ')
    case 8:
        print('восемьдесят', end=' ')
    case 9:
        print('девяносто', end=' ')
if x2 != 1:
    match x3:
        case 1:
            print ('один', end=' ')
        case 2:
         print ('два', end=' ')
        case 3:
            print('три', end=' ')
        case 4:
            print('четыре', end=' ')
        case 5:
            print('пять', end=' ')
        case 6:
            print('шесть', end=' ')
        case 7:
            print('семь', end=' ')
        case 8:
            print('восемь', end=' ')
        case 9:
            print('девять', end=' ')




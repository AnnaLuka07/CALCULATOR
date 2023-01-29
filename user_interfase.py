import logg
#import mod_calc
import excep

def view_data(data):
    print(data)

def get_value():
    return float(input('Input rational number: '))

def menu_calk():
    while True:
        op = input( '___________________________\n'
                    '***************************\n'
                    'Choice types of operation  \n'
                    '---------------------------\n'
                    '1 - sum                    \n'
                    '2 - subtraction            \n'
                    '3 - multiplication         \n'
                    '4 - division               \n'
                    '5 - exponentiation         \n'
                    '6 - remaind                \n'
                    '7 - integer                \n'
                    '0 - menu                   \n'
                    '00 - EXIT                  \n'
                    '___________________________\n'
                    '***************************\n'
                    'Your selection: ')
        if op in ['1','2','3','4','5','6','7']:
            return op
        elif op == '0':
            return menu_calk()
        elif op == '00':
            logg.logging.info("Stop program")
            exit()
        else:
            logg.logging.error('Err')
            print('Error. Input correct number!!!')
            menu_calk()


def menu_select():
    type_numb = input(  '________________________\n'
                        '************************\n'
                        'Choice type of number   \n'
                        '------------------------\n'
                        '1 - rational numbers    \n'
                        '2 - complex numbers     \n'
                        '0 - menu                \n'
                        '00 - EXIT               \n'
                        '________________________\n'
                        '************************\n'
                        'Your selection: ')

    if type_numb in ['1','2']:
        return type_numb
    elif type_numb == '0':
        return menu_select()
    elif type_numb == '00':
        logg.logging.info("Stop program")
        exit()
    else:
        logg.logging.error('Err')
        print('Error.')
        


def get_complex_numb():
    z = complex(input('Input complex number: '))
    return z





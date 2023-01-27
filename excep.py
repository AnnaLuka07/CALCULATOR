
import mod_calc
import user_interfase as us
import logg


def button_click():
    type_numb = us.menu_select()
    op = us.menu_calk()
    if type_numb == '1' and op in ['1','2','3','4','5','6','7']:
        a = us.get_value()
        b = us.get_value()
        mod_calc.init(a, b)
        result = mod_calc.operation(a, b, op)
        us.view_data(result)
    elif type_numb == '1' and op not in ['1','2','3','4','5','6','7']:
        logg.logging.error('Err')
        print('Error. Input correct namber!!!')
    elif type_numb == '2':
        if op in ['1','2','3','4','5']:
            a = us.get_value()
            b = us.get_value()
            c = complex (a, b)
            k = us.get_value()
            n = us.get_value()
            z = complex (k, n)
            result = mod_calc.operation(c, z, op)
            us.view_data(result)
        else:
            print('Remaind not available. Input correct operation! ')
        



import mod_calc
import user_interfase as us
import logg


def button_click():
    type_numb = us.menu_select()
    if type_numb not in  ['1','2','0','00']:
        print('Input correct number!')
    else:
        op = us.menu_calk()
        if type_numb == '1' and op in ['1','2','3','4','5','6','7']:
            a = us.get_value()
            b = us.get_value()
            mod_calc.init(a, b)
            result = mod_calc.operation(a, b, op)
            us.view_data(result)
        elif type_numb == '1' and op not in ['1','2','3','4','5','6','7']:
            logg.logging.error('Err')
            print('Error. Input correct number!!!')
        elif type_numb == '2'and op in ['1','2','3','4','5']:
            z1 = us.get_complex_numb()
            z2 = us.get_complex_numb()
            result = mod_calc.operation(z1, z2, op)
            us.view_data(result)
        elif type_numb == '2'and op in ['6','7']:
            logg.logging.error('Err')
            print('Error. The operation is not available!!! Input correct operation!')
        else:
            logg.logging.error('Err')
            print('Error. Input correct number!!!')
        


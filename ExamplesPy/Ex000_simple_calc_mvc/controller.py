import model 
import view


def button_click():
    val_a = view.get_value_int()
    val_b = view.get_value_int()
    val_symbol = view.get_value_symbol()
    model.init(val_a, val_b)
    result = model.do_action(val_symbol)
    view.view_data(result, val_symbol)

